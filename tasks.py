from invoke import task


@task
def run(ctx):
    ctx.run('uvicorn api:app --host localhost --port 80 --reload')


@task
def db(ctx):
    ctx.run('alembic -c alembic/alembic.ini revision --autogenerate')
    ctx.run('alembic -c alembic/alembic.ini upgrade head')
