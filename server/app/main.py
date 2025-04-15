from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from fastapi.exceptions import RequestValidationError
from httpx import HTTPError
from pydantic import ValidationError
from starlette.exceptions import HTTPException

from app.config import exception_config as exh
from app.config.settings import config
from app.core.logging import logger
from app.service.scheduler.manager import SchedulerManager
from app.service.scheduler.resource_hub_scheduler import ResourceHubScheduler
from app.service.platforms.superteam.superteam_bounty_listing import SuperteamBountyListingResourceHub

from app.controllers.contract import contract_router
from app.controllers.chat import chat_router


ORIGINS = ["*"]


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize schedulers
    logger.info("Initializing schedulers...")
    
    # Create scheduler manager
    scheduler_manager = SchedulerManager()
    
    # Initialize and configure resource hub scheduler
    resource_scheduler = ResourceHubScheduler()
    resource_scheduler.register_resource_hub(SuperteamBountyListingResourceHub)
    scheduler_manager.register_scheduler(resource_scheduler)
    
    # Create and start all schedules
    logger.info("Creating schedules...")
    scheduler_manager.create_all_schedules()
    
    logger.info("Starting schedulers...")
    scheduler_manager.start_all()
    
    logger.info("S E R V E R   S T A R T I N G . . . . . . . . . .")
    yield

    # Shut Down Event
    logger.info("Shutting down schedulers...")
    scheduler_manager.shutdown_all()
    
    logger.info("S E R V E R   S H U T D O W N . . . . . . . . . .")


def create_application() -> FastAPI:
    logger.info("Creating FastAPI application...")
    app = FastAPI(
        title=config.PROJECT_NAME,
        description=config.PROJECT_DESCRIPTION,
        version=config.PROJECT_VERSION,
        lifespan=lifespan
    )

    if config.ENVIRONMENT == "production":
        app.openapi_url = None

    app.add_middleware(
        CORSMiddleware,
        allow_origins=ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    logger.info("Adding exception handlers...")
    #  I N C L U D E   E X C E P T I O N S  H A N D L E R S

    app.add_exception_handler(RequestValidationError, exh.req_validation_handler)
    app.add_exception_handler(ValidationError, exh.validation_handler)
    app.add_exception_handler(AttributeError, exh.attribute_error_handler)

    app.add_exception_handler(HTTPError, exh.http_error_handler)
    app.add_exception_handler(HTTPException, exh.http_exception_handler)

    logger.info("Including routers...")
    # Include routers
    app.include_router(contract_router, prefix="/contract", tags=["contract"])
    app.include_router(chat_router, prefix="/chat", tags=["chat"])

    logger.info("Application setup complete")
    return app


if __name__ == "__main__":
    import uvicorn

    logger.info("Starting server with uvicorn...")
    uvicorn.run(
        "app.main:create_application",
        factory=True,
        log_level=config.LOG_LEVEL.lower(),
        access_log=True,
        reload=True,  # has to be false for tracing to work
    )

