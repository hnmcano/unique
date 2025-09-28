from fastapi import APIRouter

router = APIRouter()

@router.get("/product")
def get_user():
    return {"product":"Product_profile"}

