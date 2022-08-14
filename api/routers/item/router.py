from fastapi import APIRouter

from . import views

router = APIRouter(prefix='/item', tags=['Item'])
router.add_api_route(path='/', endpoint=views.create, methods=['POST'])
router.add_api_route(path='/', endpoint=views.list_all, methods=['GET'])
router.add_api_route(path='/{id:int}', endpoint=views.read, methods=['GET'])
router.add_api_route(path='/{id:int}', endpoint=views.update, methods=['PUT'])
router.add_api_route(path='/{id:int}', endpoint=views.delete, methods=['DELETE'])
