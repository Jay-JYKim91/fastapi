from pydantic import BaseSettings


class Settings(BaseSettings):
    pager: str
    database_username: str
    secret_key: str


settings = Settings()
