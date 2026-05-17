"""Day 1 — verify our setup works end-to-end."""
import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()  # reads .env into os.environ


class AppConfig(BaseModel):
    """Typed config — every AI project I build will have one of these."""
    openai_api_key: str
    app_env: str = "dev"


def main() -> None:
    config = AppConfig(
        openai_api_key=os.getenv("OPENAI_API_KEY", ""),
        app_env=os.getenv("APP_ENV", "dev"),
    )
    print(f"✅ Config loaded. Env: {config.app_env}")
    print(f"✅ API key starts with: {config.openai_api_key[:10]}...")
    print(f"✅ Pydantic validated the config — no missing fields.")


if __name__ == "__main__":
    main()