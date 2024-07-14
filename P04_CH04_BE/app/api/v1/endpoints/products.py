from fastapi import APIRouter, HTTPException, Path, Body, Depends
from typing import List

from app import crud, schemas
from app.api import deps

router = APIRouter()

@router.post("/", response_model=schemas.Product)
def create_product(
    *,
    product_in: schemas.ProductCreate,
    db=Depends(deps.get_db)
):
    """
    새로운 product 생성
    """
    product = crud.crud_product.create(db=db, obj_in=product_in)
    return product

@router.get("/")
def read_product_list(
    *,
    page: int = 0,
    limit: int = 10,
    db=Depends(deps.get_db)
):
    """
    product 리스트 조회
    """
    products = crud.crud_product.get_multi(db, skip=page, limit=limit)

    return products

@router.get("/{product_id}", response_model=schemas.Product)
def read_product(
    *,
    db=Depends(deps.get_db),
    product_id: int = Path(..., description="아이템 ID")
):
    db_product = crud.crud_product.get(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product
    
@router.put("/{product_id}", response_model=schemas.Product)
def update_product(
    *,
    db=Depends(deps.get_db),
    product_id: int,
    product_in: schemas.ProductUpdate
):
    """
    Product 정보 업데이트
    """
    product = crud.crud_product.get(db=db, product_id=product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="product not found")
    product = crud.crud_product.update(db=db, db_obj=product, obj_in=product_in)
    return product

@router.delete("/{product_id}", response_model=schemas.Product)
def delete_product(
    *,
    db=Depends(deps.get_db),
    product_id: int
):
    """
    product 삭제
    """
    product = crud.crud_product.get(db=db, product_id=product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="product not found")
    product = crud.crud_product.remove(db=db, product_id=product_id)
    return product
