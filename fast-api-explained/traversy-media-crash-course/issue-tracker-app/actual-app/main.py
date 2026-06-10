from fastapi import FastAPI
from app.routes.issues import router as issues_router # impoertinf the issue router object
from app.midleware.timer import timing_middleware

app = FastAPI() # Creating an app instance

# app.middleware("http") returns a decorator that registers a function as HTTP middleware
# (timing_middleware) immediately applies that decorator to the timing_middleware function
# i.e the below line registers timing_middleware as an HTTP middleware on the FastAPI app
app.middleware("http")(timing_middleware)

# app.include_router(issues_router) registers/connects your issues_router to the main app so that all the routes defined in your router become part of your main application
# Without this line, your issues_router and all its endpoints exist but are completely disconnected from your app — no one can reach them
app.include_router(issues_router)

