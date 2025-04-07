from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from fastapi.exceptions import RequestValidationError
from httpx import HTTPError
from pydantic import ValidationError
from starlette.exceptions import HTTPException

# from app.controllers.agent_controller import agent_router
from app.config import exception_config as exh
from app.config.settings import config
from app.service.platforms.scheduler import ResourceHubScheduler


ORIGINS = ["*"]


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start Up Event
    resource_hub_scheduler = ResourceHubScheduler()
    resource_hub_scheduler.create_schedules()

    resource_hub_scheduler.start()

    print("\nS E R V E R   S T A R T I N G . . . . . . . . . .\n")
    yield

    # Shut Down Event
    
    resource_hub_scheduler.shutdown()
    
    print("\nS E R V E R   S H U T D O W N . . . . . . . . . .\n")


def create_application() -> FastAPI:
    app = FastAPI(
        title=config.PROJECT_NAME,
        description=config.PROJECT_DESCRIPTION,
        version=config.PROJECT_VERSION,
        lifespan=lifespan
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


    #  I N C L U D E   E X C E P T I O N S  H A N D L E R S

    app.add_exception_handler(RequestValidationError, exh.req_validation_handler)
    app.add_exception_handler(ValidationError, exh.validation_handler)
    app.add_exception_handler(AttributeError, exh.attribute_error_handler)

    app.add_exception_handler(HTTPError, exh.http_error_handler)
    app.add_exception_handler(HTTPException, exh.http_exception_handler)


    #  I N C L U D E   R O U T E R S

    # app.include_router(agent_router, prefix="/agent", tags=["agent"])

    return app


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:create_application",
        factory=True,
        access_log=True,
        reload=True,  # has to be false for tracing to work
    )

