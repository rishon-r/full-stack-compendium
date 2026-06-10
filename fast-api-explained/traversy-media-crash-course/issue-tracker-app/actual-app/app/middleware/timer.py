import time
from fastapi import Request

"""
Middleware refers to code that runs before and/or after each request
Every backend framework will typically have a means of supporting middleware
Middleware is typically used to handle authentication, write to log files or modify the request/response
"""

async def timing_middleware(request: Request, call_next): # request: Request - The incoming request object, call_next - A function that, when called, will pass the request to the next middleware or route handler
    start = time.perf_counter() # time.perf_counter() - High-resolution timer to measure elapsed time
    response = await call_next(request)
    response.headers["X-Process-Time"] = f"{time.perf_counter() - start:.4f}s"
    return response
    # Everything before await call_next(request) runs before the request is processed,
    # and everything after runs after the response is generated. That is why we add the header after calling call_next.
    # So the request is made, the response is generated, and then we add our custom header before sending it back to the client

