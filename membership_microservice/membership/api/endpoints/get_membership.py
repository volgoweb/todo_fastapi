from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from membership.api.schemas import MyMembershipResponse

router = APIRouter()
auth = HTTPBearer()


@router.get("/memberships/my", response_model=MyMembershipResponse)
def get_my_membership(auth_info: HTTPAuthorizationCredentials = Depends(auth)):
    return MyMembershipResponse(
        is_premium=auth_info.credentials == "premium",
        plan="Premium",
    )
