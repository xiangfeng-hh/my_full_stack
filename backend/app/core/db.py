from sqlmodel import Session, create_engine, select

from app.api.users import crud
from app.core.config import settings
from app.api.models  import User, UserCreate

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))

# 确保初始化数据库之前已导入所有 SQLModel 模型（app.api.models）
# 否则，SQLModel 可能无法正确初始化关系
# 更多详情请参考：https://github.com/fastapi/full-stack-fastapi-template/issues/28



def init_db(session: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next lines
    # from sqlmodel import SQLModel

    # This works because the models are already imported and registered from app.api.models 
    # SQLModel.metadata.create_all(engine)

    user = session.exec(
        select(User).where(User.email == settings.FIRST_SUPERUSER)
    ).first()
    if not user:
        user_in = UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud.create_user(session=session, user_create=user_in)
