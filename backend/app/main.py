import os
from os import path

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT

from .const import MODE, BASE_URL
from .routers import (
    user,
    auth
)

app = FastAPI()

app.include_router(auth.router)
app.include_router(user.router)

if MODE != "production":
    origins = [
        BASE_URL
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
)

dist_dir = path.abspath(path.join(path.dirname(__file__), "../../frontend/build"))

app.mount("/static/", StaticFiles(directory=dist_dir + "/static"), name="static")

@app.get("/", response_class=FileResponse)
def read_index(request: Request, Authorize: AuthJWT = Depends()):
    path = dist_dir + "/index.html"
    return FileResponse(path)

@app.get("/{catchall:path}", response_class=FileResponse)
def read_index(request: Request):
    # check first if requested file exists
    path = request.path_params["catchall"]
    file = dist_dir + "/" + path

    print("look for: ", path, file)
    if os.path.exists(file):
        return FileResponse(file)

    # otherwise return index files
    index = dist_dir + "/index.html"
    return FileResponse(index)
