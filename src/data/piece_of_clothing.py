from typing import Optional
from uuid import uuid4

from pydantic import BaseModel

from src.data.clothing_size import ClothingSize


class SaleItem(BaseModel):
    id: str
    name: str
    long_name: Optional[str]


class PieceOfClothing(SaleItem):
    size: ClothingSize


class AdvertisePieceOfClothing(PieceOfClothing):
    pass


class SoldPieceOfClothing(BaseModel):
    original_price: Optional[float]
    purchase_price: Optional[float]
    selling_price: Optional[float]
    post_fee: Optional[float]
    date_of_sale: Optional[str]
    pieces: Optional[int]

    def is_sent_by_post(self):
        return self.post_fee is not None

