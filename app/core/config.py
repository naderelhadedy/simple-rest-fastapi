"""
config module
"""

import os
from typing import List, ClassVar

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

ENV: str = "dev"


class Configs(BaseSettings):
    """
    Configs class
    """
    # base
    API: ClassVar[str] = "/api"
    API_V1_STR: ClassVar[str] = "/api/v1"
    PROJECT_NAME: ClassVar[str] = "simple-rest-fast-api"
    DB_ENGINE_MAPPER: dict = {
        "mydb": "postgresql",
    }
    ENV_DATABASE_MAPPER: dict = {
        "dev": "mydb",
    }

    # CORS
    BACKEND_CORS_ORIGINS: ClassVar[List[str]] = ["*"]

    # database
    DB: str = os.getenv("DB")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = int(os.getenv("DB_PORT"))
    DB_ENGINE: str = DB_ENGINE_MAPPER.get(DB)

    DATABASE_URI: ClassVar[str] = "{db_engine}://{user}:{password}@{host}:{port}/{database}".format(
        db_engine=DB_ENGINE,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=ENV_DATABASE_MAPPER[ENV],
    )
