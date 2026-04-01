import uuid

from fastapi import APIRouter, HTTPException
from sqlmodel import col, func, select

from app.api.deps import CurrentUser, SessionDep
from app.api.models import (
    Item,
    Message,
    ItemCreate,
    ItemPublic,
    ItemsPublic,
    ItemUpdate,
)


router = APIRouter()


@router.get("/", response_model=ItemsPublic)
def read_items(
    session: SessionDep, current_user: CurrentUser, skip: int = 0, limit: int = 100
):
    """
    检索 items
    """

    if current_user.is_superuser:
        count_statement = select(func.count()).select_from(Item)
        count = session.exec(count_statement).one()
        statement = (
            select(Item).order_by(col(Item.created_at).desc()).offset(skip).limit(limit)
        )
        items = session.exec(statement).all()
    else:
        count_statement = (
            select(func.count())
            .select_from(Item)
            .where(Item.owner_id == current_user.id)
        )
        count = session.exec(count_statement).one()
        statement = (
            select(Item)
            .where(Item.owner_id == current_user.id)
            .order_by(col(Item.created_at).desc())
            .offset(skip)
            .limit(limit)
        )
        items = session.exec(statement).all()

    return ItemsPublic(data=items, count=count)


@router.post("/", response_model=ItemPublic)
def create_item(*, session: SessionDep, current_user: CurrentUser, item_in: ItemCreate):
    """
    创建item
    """
    item = Item.model_validate(item_in, update={"owner_id": current_user.id})
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


def prev_check(item: Item, current_user: CurrentUser):
    if not item:
        raise HTTPException(status_code=404, detail="Item不存在")
    if not current_user.is_superuser and (item.owner_id != current_user.id):
        raise HTTPException(status_code=403, detail="没权限")


@router.put("/{id}", response_model=ItemPublic)
def update_item(
    session: SessionDep, current_user: CurrentUser, id: uuid.UUID, item_in: ItemUpdate
):
    """
    更新 item
    """
    item = session.get(Item, id)
    prev_check(item, current_user)

    update_dict = item_in.model_dump(exclude_unset=True)
    item.sqlmodel_update(update_dict)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@router.delete("/{id}")
def delete_item(
    session: SessionDep, current_user: CurrentUser, id: uuid.UUID
) -> Message:
    """
    删除item
    """
    item = session.get(Item, id)
    prev_check(item, current_user)
    session.delete(item)
    session.commit()
    return Message(message="删除成功")


@router.get("/{id}", response_model=ItemPublic)
def read_item(session: SessionDep, current_user: CurrentUser, id: uuid.UUID):
    """
    获取 item by ID
    """
    item = session.get(Item, id)
    prev_check(item, current_user)
    return item
