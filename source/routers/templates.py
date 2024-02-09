from fastapi.responses import JSONResponse
from fastapi import (
    APIRouter,
    Depends,
    status,
)

from source.repositories import TemplateRepository
from source.dependencies import (
    SessionReadOnly,
    Session,
)
from source.scheme import (
    TemplateCreateRequest,
    TemplateManyResponse,
    TemplateResponse,
)
from source.usecases import (
    TemplateGetByIdUseCase,
    TemplateCreateUseCase,
    TemplateDeleteUseCase,
    TemplateGetAllUseCase,
    TemplateUpdateUseCase,
)


templates = APIRouter()


@templates.get("/")
async def get_all_templates(session: SessionReadOnly = Depends()) -> TemplateManyResponse:
    templates = await TemplateGetAllUseCase(
        TemplateRepository(session)
    ).execute()
    return JSONResponse(templates.model_dump(), status_code=status.HTTP_200_OK)


@templates.get("/{template_id}")
async def get_template(template_id: int, session: SessionReadOnly = Depends()) -> TemplateResponse:
    template = await TemplateGetByIdUseCase(
        TemplateRepository(session)
    ).execute(template_id)
    return JSONResponse(template.model_dump(), status_code=status.HTTP_200_OK)


@templates.post("/")
async def create_template(data: TemplateCreateRequest, session: Session = Depends()) -> TemplateResponse:
    template = await TemplateCreateUseCase(
        TemplateRepository(session)
    ).execute(data)
    print(template)
    return JSONResponse(template.model_dump(), status_code=status.HTTP_201_CREATED)


@templates.delete("/{template_id}")
async def delete_template(template_id: int, session: Session = Depends()) -> TemplateResponse:
    template = await TemplateDeleteUseCase(
        TemplateRepository(session)
    ).execute(template_id)
    return JSONResponse(template.model_dump(), status_code=status.HTTP_200_OK)


@templates.put("/{template_id}")
async def delete_template(template_id: int, data: TemplateCreateRequest, session: Session = Depends()) -> TemplateResponse:
    template = await TemplateUpdateUseCase(
        TemplateRepository(session)
    ).execute(template_id, data)
    return JSONResponse(template.model_dump(), status_code=status.HTTP_200_OK)
