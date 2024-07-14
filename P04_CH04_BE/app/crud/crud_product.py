from sqlalchemy.orm import Session
from app.db import models

def get(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()
    # select * from products where id = product_id

def get_multi(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Product).offset(skip).limit(limit).all()
    # select * from products limit limit offset skip

def create(db: Session, obj_in):
    db_product = models.Product(**obj_in.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
    # insert into products (category_id, name, description, price, image_url) values (obj_in.category_id, obj_in.name, obj_in.description, obj_in.price, obj_in.image_url)

def update(db: Session, db_obj, obj_in):
    db_obj_data = db_obj.__dict__
    update_data = obj_in.dict(exclude_unset=True)
    for field in db_obj_data:
        if field in update_data:
            setattr(db_obj, field, update_data[field])
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
    # update products set category_id = obj_in.category_id, name = obj_in.name, description = obj_in.description, price = obj_in.price, image_url = obj_in.image_url where id = db_obj.id


def remove(db: Session, product_id: int):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    db.delete(db_product)
    db.commit()
    return db_product
    # delete from products where id = product_id