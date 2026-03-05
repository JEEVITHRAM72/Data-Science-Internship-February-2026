from fastapi import FastAPI, Query

app = FastAPI()

# Temporary product data (acts like a database)
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 499, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Notebook", "price": 99, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "USB Hub", "price": 799, "category": "Electronics", "in_stock": False},
    {"id": 4, "name": "Pen Set", "price": 49, "category": "Stationery", "in_stock": True},
    {"id": 5, "name": "Laptop Stand", "price": 399, "category": "Accessories", "in_stock": False},
    {"id": 6, "name": "Mechanical Keyboard", "price": 1300, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Normal Keyboard", "price": 1300, "category": "Electronics", "in_stock": True},
    {"id": 8, "name": "Webcam", "price": 599, "category": "Electronics", "in_stock": True},
]

# Home endpoint
@app.get("/")
def home():
    return {"message": "Welcome to the E-commerce API"}


# Q1 – Get all products
@app.get("/products")
def get_products():
    return {
        "products": products,
        "total": len(products)
    }


# Optional filter endpoint (category / price / stock)
@app.get("/products/filter")
def filter_products(
    category: str = Query(None, description="Filter by category"),
    max_price: int = Query(None, description="Maximum price"),
    in_stock: bool = Query(None, description="Filter by stock availability")
):
    filtered_products = products

    if category:
        filtered_products = [
            p for p in filtered_products
            if p["category"].lower() == category.lower()
        ]

    if max_price:
        filtered_products = [
            p for p in filtered_products
            if p["price"] <= max_price
        ]

    if in_stock is not None:
        filtered_products = [
            p for p in filtered_products
            if p["in_stock"] == in_stock
        ]

    return {
        "filtered_products": filtered_products,
        "count": len(filtered_products)
    }


# Endpoint to get product by ID
@app.get("/products/{product_id}")
def get_product_by_id(product_id: int):
    for item in products:
        if item["id"] == product_id:
            return {"product": item}

    return {"error": "Product not found"}


# Q2 – Category endpoint
@app.get("/products/category/{category}")
def get_products_by_category(category: str):

    category_products = [
        p for p in products
        if p["category"].lower() == category.lower()
    ]

    if not category_products:
        return {"error": "No products found in this category"}

    return {
        "products": category_products,
        "total": len(category_products)
    }


# Q3 – In-stock products
@app.get("/products/instock")
def get_instock_products():

    available_products = [
        p for p in products if p["in_stock"]
    ]

    return {
        "in_stock_products": available_products,
        "count": len(available_products)
    }


# Q4 – Store summary
@app.get("/store/summary")
def store_summary():

    total_products = len(products)

    in_stock_count = sum(
        1 for p in products if p["in_stock"]
    )

    out_of_stock_count = total_products - in_stock_count

    categories = list(
        {p["category"] for p in products}
    )

    return {
        "store_name": "My E-commerce Store",
        "total_products": total_products,
        "in_stock": in_stock_count,
        "out_of_stock": out_of_stock_count,
        "categories": categories
    }


# Q5 – Search products
@app.get("/products/search/{keyword}")
def search_products(keyword: str):

    results = [
        p for p in products
        if keyword.lower() in p["name"].lower()
    ]

    if not results:
        return {"message": "No products matched your search"}

    return {
        "matched_products": results,
        "count": len(results)
    }


# Bonus – Best deal & premium pick
@app.get("/products/deals")
def product_deals():

    cheapest_product = min(products, key=lambda p: p["price"])
    expensive_product = max(products, key=lambda p: p["price"])

    return {
        "best_deal": cheapest_product,
        "premium_pick": expensive_product
    }