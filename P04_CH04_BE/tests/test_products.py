from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_product_and_read_product(db_session):
    product_data = {
        "name": "New Product",
        "description": "This is a new product",
        "price": 100,
        "image_url": "https://example.com/image.jpg",
        "category_id": 2
    }

    expected_response = {
        "name": "New Product",
        "description": "This is a new product",
        "price": 100,
        "image_url": "https://example.com/image.jpg",
        "id": 1,
        "category_id": 2
    }
    response = client.post("/api/v1/products/", json=product_data)
    assert response.status_code == 200
    assert response.json() == expected_response

    #### read product
    response = client.get("/api/v1/products/1")
    assert response.status_code == 200
    assert response.json() == expected_response

    ### update product
    update_data = {
        "name": "Updated Product",
        "description": "This is an updated product",
        "price": 200,
        "image_url": "https://example.com/updated_image.jpg",
        "category_id": 3
    }
    expected_response = {
        "name": "Updated Product",
        "description": "This is an updated product",
        "price": 200,
        "image_url": "https://example.com/updated_image.jpg",
        "id": 1,
        "category_id": 3
    }
    response = client.put("/api/v1/products/1", json=update_data)
    assert response.status_code == 200
    assert response.json() == expected_response

    ### delete product
    response = client.delete("/api/v1/products/1")
    assert response.status_code == 200
    assert response.json() == expected_response
    
    ### read product again
    response = client.get("/api/v1/products/1")
    assert response.status_code == 404