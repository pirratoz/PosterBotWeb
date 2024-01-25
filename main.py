from uvicorn import run as uvicorn_run
from fastapi import FastAPI

from source.docs import Tags
from source.routers import (
    publications,
    templates,
    chats,
    moders,
)
from source.dependencies import (
    DatabaseConnector,
    SessionReadOnly,
    Session,
)


def include_routers(app: FastAPI) -> None:
    app.include_router(publications, prefix="/publications", tags=[Tags.publications])
    app.include_router(templates, prefix="/templates", tags=[Tags.templates])
    app.include_router(chats, prefix="/chats", tags=[Tags.chats])
    app.include_router(moders, prefix="/moders", tags=[Tags.moders])


def include_dependency(app: FastAPI, db: DatabaseConnector) -> None:
    app.dependency_overrides[SessionReadOnly] = db.get_session_read_only
    app.dependency_overrides[Session] = db.get_session


def main() -> None:
    app = FastAPI()
    db = DatabaseConnector()

    include_routers(app)

    include_dependency(app, db)

    uvicorn_run(app)


if __name__ == "__main__":
    main()
