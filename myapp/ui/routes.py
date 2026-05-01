from fastapi import APIRouter, HTTPException, status

from myapp.core.domain import BountyClaim, LostItemCreate, LostItemRead
from myapp.core.service import BountyService

router = APIRouter()
service = BountyService()


@router.post("/bounties", response_model=LostItemRead, status_code=status.HTTP_201_CREATED)
def create_bounty(payload: LostItemCreate) -> LostItemRead:
    try:
        return service.create_bounty(payload)
    except ValueError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error)) from error


@router.get("/bounties", response_model=list[LostItemRead])
def list_bounties() -> list[LostItemRead]:
    return [LostItemRead.model_validate(item) for item in service.list_bounties()]


@router.post("/bounties/{item_id}/claim", response_model=LostItemRead)
def claim_bounty(item_id: str, payload: BountyClaim) -> LostItemRead:
    try:
        return LostItemRead.model_validate(service.claim_bounty(item_id, payload))
    except ValueError as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error)) from error
