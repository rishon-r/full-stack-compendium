from fastapi import APIRouter # Imports the APIRouter class from FastAPI
from fastapi import HTTPException, status # For providing the valid status code/exceptions as a result of a request
from app.schemas import IssueCreate, IssueOut, IssueUpdate
from app.storage import load_data, save_data
import uuid

# APIRouter is like a mini version of your main app — it lets you group related routes together
# Below line of code creates a router instance with two important settings
# prefix="/api/v1/issues" prepends "/api/v1/issues" to every route defined on this router
# This helps as we don't need to specify this on every endpoint
# Notice the /v1 — this is API versioning, meaning if you ever make breaking changes you can create a v2 without breaking existing users on v1
# ags=["issues"] — this is purely for documentation purposes — it groups all routes in this router under an "issues" section in your auto generated Swagger docs
router = APIRouter(prefix="/api/v1/issues", tags = ["issues"])

# Why use APIRouter instead of just app: 
# Imagine an app with hundreds of endpoints — putting them all in main.py would be a mess. 
# APIRouter lets you organize routes into separate files

@router.get("/", response_model=list[IssueOut]) # Same as @app.get() but uses router instead of app. The full path of this endpoint becomes /api/v1/issues/ because the prefix gets added automatically
# In FastAPI, response_model is a parameter that defines the expected shape of the response data. 
# With response_model=list[IssueOut], we are validating that the response matches the IssueOut model. 
# It will serialize the response to JSON and filter out any extra fields
async def get_issues():
  '''
  Retrieves all issues
  '''
  # Notice the async keyword — this makes the function asynchronous, taking advantage of FastAPI and ASGI's async capabilities
  # Means this function can handle other requests while waiting for things like database queries

  # We call load_data() to read from the JSON file each time - this ensures we always have the latest data
  issues = load_data()

  return issues

@router.post("", response_model=IssueOut, status_code=status.HTTP_201_CREATED) # status_code=status.HTTP_201_CREATED - Returns 201 instead of default 200
def create_issue(payload: IssueCreate): # payload: IssueCreate - FastAPI automatically parses the JSON body and validates it
    """
    Create new issue
    The issue is persisted to data/issues.json
    """
    issues = load_data()

    issue = {
        "id": str(uuid.uuid4()), # uuid.uuid4() - Generates a unique ID like "550e8400-e29b-41d4-a716-446655440000". No counter needed!
        "title": payload.title,
        "description": payload.description,
        "priority": payload.priority.value, # .value on enums - Converts the enum to its string value for JSON storage
        "status": "open", # Status is hardcoded to open
    }

    issues.append(issue)
    save_data(issues) # save_data(issues) - Persists to the JSON file immediately

    return issue

@router.get("/{issue_id}", response_model=IssueOut)
def get_issue(issue_id: str):
   """Retrieve a specific issue by ID"""
   issues = load_data()
   for issue in issues:
      if issue["id"]==issue_id:
         return issue
   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")
  
  
@router.put("/{issue_id}", response_model=IssueOut)
def update_issue(issue_id: str, payload: IssueUpdate):
    """Update an existing issue by ID."""
    issues = load_data()

    for issue in issues:
        if issue["id"] == issue_id:
            if payload.title is not None:
                issue["title"] = payload.title
            if payload.description is not None:
                issue["description"] = payload.description
            if payload.priority is not None:
                issue["priority"] = payload.priority.value
            if payload.status is not None:
                issue["status"] = payload.status.value

            save_data(issues)
            return issue

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Issue not found"
    )

@router.delete("/{issue_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_issue(issue_id: str):
    """Delete an issue by ID."""
    issues = load_data()

    for i, issue in enumerate(issues):
        if issue["id"] == issue_id:
            issues.pop(i)
            save_data(issues)
            return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Issue not found"
    )