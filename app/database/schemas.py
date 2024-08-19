from pydantic import BaseModel

class ProductSchema(BaseModel):
    product_title: str
    product_price: float
    path_to_image: str
