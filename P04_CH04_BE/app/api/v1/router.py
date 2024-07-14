from fastapi import APIRouter

from app.api.v1.endpoints import products, chat

api_router = APIRouter()
api_router.include_router(products.router, prefix="/products", tags=["products"])
api_router.include_router(chat.router, prefix="/chat", tags=["chat"])