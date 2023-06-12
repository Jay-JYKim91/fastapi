from pydantic import BaseSettings


class Settings(BaseSettings):
    PAGER: str
    database_username: str
    secret_key: str


settings = Settings()
