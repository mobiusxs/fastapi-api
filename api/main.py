from fastapi import FastAPI

from api.routers import item


app = FastAPI(
    debug=False,
    title='API Title',
    description='API Description',
    version='0.1.0',
    openapi_prefix='',
    root_path='',
    docs_url='/',
)

app.include_router(item.router)
