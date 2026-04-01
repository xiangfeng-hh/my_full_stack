import sentry_sdk  # noqa: I001
from fastapi import FastAPI
from fastapi.routing import APIRoute
from starlette.middleware.cors import CORSMiddleware


from app.core.config import settings




def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"


if settings.SENTRY_DSN and settings.ENVIRONMENT != "local":
    sentry_sdk.init(dsn=str(settings.SENTRY_DSN), enable_tracing=True)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
)

# Set all CORS enabled origins
if settings.all_cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.all_cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )



from app.api.login.router import router as login
from app.api.utils.router import router as utils
from app.api.users.router import router as users
from app.api.items.router import router as items
app.include_router(login, prefix=settings.API_V1_STR, tags=["登录"])
app.include_router(utils, prefix=f"{settings.API_V1_STR}/utils", tags=["工具"])
app.include_router(users, prefix=f"{settings.API_V1_STR}/users", tags=["用户"])
app.include_router(items, prefix=f"{settings.API_V1_STR}/items", tags=["items"])

