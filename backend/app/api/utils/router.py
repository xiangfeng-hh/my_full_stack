from fastapi import APIRouter


router = APIRouter()

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@router.get("/health-check/")
async def health_check() -> bool:
    return True
