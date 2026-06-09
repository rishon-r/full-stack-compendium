from fastapi import FastAPI
from app.routes.issues import router as issues_router # impoertinf the issue router object

app = FastAPI() # Creating an app instance

# app.include_router(issues_router) registers/connects your issues_router to the main app so that all the routes defined in your router become part of your main application
# Without this line, your issues_router and all its endpoints exist but are completely disconnected from your app — no one can reach them
app.include_router(issues_router)