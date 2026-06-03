from pydantic_settings import BaseSettings, SettingsConfigDict

class APISettings(BaseSettings):
    debug: bool = False
    project_name: str = "LetsMakeIt"
    project_description: str = "Full-stack project."

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

class DBSettings(BaseSettings):
    sqlalchemy_database_url: str
    secret_key: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
    
class Settings(APISettings, DBSettings):
    pass

settings: Settings = Settings()