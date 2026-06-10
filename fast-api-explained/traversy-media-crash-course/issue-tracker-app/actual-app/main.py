from fastapi import FastAPI
from app.routes.issues import router as issues_router # impoertinf the issue router object
from app.midleware.timer import timing_middleware # importing our middleware function
from fastapi.middleware.cors import CORSMiddleware # this is for CORS, more on this later

app = FastAPI() # Creating an app instance

# app.middleware("http") returns a decorator that registers a function as HTTP middleware
# (timing_middleware) immediately applies that decorator to the timing_middleware function
# i.e the below line registers timing_middleware as an HTTP middleware on the FastAPI app
app.middleware("http")(timing_middleware)

# CORS (Cross-Origin Resource Sharing) middleware
#
# WHY THIS EXISTS: Browsers enforce the "Same-Origin Policy" — a security rule that
# blocks webpages from making requests to a different origin than the one they loaded from.
# An "origin" is the combination of protocol + domain + port, so:
#   http://localhost:3000 (your frontend)
#     vs
#   http://localhost:8000 (this API)
# ...are considered different origins, and the browser will block requests between them.
#
# HOW CORS FIXES IT: The server sends back special HTTP headers telling the browser
# "I trust this other origin, let the request through." Without these headers, the
# browser refuses the response — even if the server processed it fine.
#
# WHAT EACH SETTING DOES:
#   allow_origins      → Access-Control-Allow-Origin header
#                        ["*"] means any domain can call this API from a browser.
#                        In production, restrict to e.g. ["https://myapp.com"]
#
#   allow_credentials  → Access-Control-Allow-Credentials header
#                        True allows cookies and Authorization headers to be included
#                        in requests. Note: browsers block credentials when origin is "*",
#                        so remember to set a specific origin in production.
#
#   allow_methods      → Access-Control-Allow-Methods header
#                        ["*"] permits all HTTP verbs (GET, POST, PUT, DELETE, etc.)
#
#   allow_headers      → Access-Control-Allow-Headers header
#                        ["*"] permits any headers (e.g. Content-Type, Authorization)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # TODO: restrict to your frontend's domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# app.include_router(issues_router) registers/connects your issues_router to the main app so that all the routes defined in your router become part of your main application
# Without this line, your issues_router and all its endpoints exist but are completely disconnected from your app — no one can reach them
app.include_router(issues_router)

