from typing import Optional

from pydantic import BaseModel


class ClothingSize(BaseModel):
    pass


class ClothingSizeByHeight(ClothingSize):
    min: Optional[int]
    max: Optional[int]


class ClothingSizeByAge(BaseModel):
    min: Optional[int]
    max: Optional[int]

