from pydantic import BaseSettings


class Settings(BaseSettings):
    database_password: str
    database_username: str
    secret_key: str


settings = Settings()
