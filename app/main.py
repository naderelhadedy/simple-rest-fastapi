"""
main start file
"""

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import uvicorn

from app.api.v1.routes import routers as v1_routers
from app.core.config import Configs
from app.core.container import Container
from app.util.class_object import singleton


@singleton
class AppCreator:
    """
    App Creator class
    """
    def __init__(self):
        # set app default
        self.app = FastAPI(
            title=Configs.PROJECT_NAME,
            openapi_url=f"{Configs.API}/openapi.json",
            version="0.0.1",
        )

        # set db and container
        self.container = Container()
        self.db = self.container.db()

        # set cors
        if Configs.BACKEND_CORS_ORIGINS:
            self.app.add_middleware(
                CORSMiddleware,
                allow_origins=[str(origin) for origin in Configs.BACKEND_CORS_ORIGINS],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )

        # set routes
        @self.app.get("/")
        def root():
            """
            root view
            """
            return "service is working"

        self.app.include_router(v1_routers, prefix=Configs.API_V1_STR)


app_creator = AppCreator()
app = app_creator.app
db = app_creator.db
container = app_creator.container

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
