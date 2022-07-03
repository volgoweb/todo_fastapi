from fastapi import Depends, APIRouter

from membership.api.endpoints import healthcheck, get_membership


router = APIRouter()
router.include_router(healthcheck.router)
router.include_router(get_membership.router)
