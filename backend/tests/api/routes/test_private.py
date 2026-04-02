from fastapi.testclient import TestClient
from sqlmodel import Session, select

from app.core.config import settings
from app.api.models  import User

