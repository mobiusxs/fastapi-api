from . import models
from . import schemas


async def create(data: schemas.Item):
    item = models.Item(**data.dict())
    item.save()


async def list_all():
    return models.Item.all()


async def read(id: int):
    return models.Item.find(id)


async def update(id: int, data: schemas.Item):
    item = models.Item.find(id)
    if item:
        item.update(**data.dict())


async def delete(id: int):
    item = models.Item.find(id)
    if item:
        item.delete()
