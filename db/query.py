from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import Product


async def orm_add_product(session: AsyncSession, data: dict):
    new_product = Product(
        name=data["name"],
        description=data["description"],
        price=data["price"],
        image=data["image"],
    )
    session.add(new_product)
    await session.commit()


async def orm_get_product(session: AsyncSession, product_id: int):
    query = select(Product).where(Product.id == product_id)
    result = await session.execute(query)
    return result.scalars()

async def orm_get_products(session: AsyncSession):
    query = select(Product)
    result = await session.execute(query)
    return result.scalars().all()


async def orm_update_product(session: AsyncSession, product_id: int ,data: dict):
    query = update(Product).where(Product.id == product_id).values(
        name=data["name"],
        description=data["description"],
        price=data["price"],
        image=data["image"],
    )
    result = await session.execute(query)
    return session.commit()


async def orm_delete_product(session: AsyncSession, product_id: int):
    query = delete(Product).where(Product.id == product_id)
    result = await session.execute(query)
    return session.commit()