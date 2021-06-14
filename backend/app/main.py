from os import path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from starlette.responses import JSONResponse

from .const import MODE, BASE_URL

app = FastAPI()

if MODE != "production":
    origins = [
        BASE_URL
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
)

dist_dir = path.abspath(path.join(path.dirname(__file__), "../../frontend/build"))

app.mount("/static/", StaticFiles(directory=dist_dir + "/static"), name="static")

@app.get("/", response_class=FileResponse)
def read_index(request: Request):
    path = dist_dir + "/index.html"
    return FileResponse(path)

# FIXME: 疎通確認用コード
@app.post("/test/")
def post_test(request: Request):
    return JSONResponse(status_code=200, content={"message": "successful POST"})
