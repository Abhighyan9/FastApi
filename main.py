from fastapi import FastAPI
from models import Product


app = FastAPI()

@app.get("/")       
def greet():
    return "First API"

products = [
    Product(id=1, name="Laptop", description="A high-performance laptop", price=999.99, quantity=10),
    Product(id=2, name="Mobile", description="A powerful smartphone", price=499.99, quantity=20),
    Product(id=3, name="Tablet", description="A versatile tablet", price=299.99, quantity=15)
]

@app.get("/products")

def get_all_products():
    return products

@app.get("/products/{id}")  
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return {"message": "Product not found"}