import csv
from typing import List
from uuid import uuid4

from src.data.clothing_size import ClothingSizeByHeight
from src.data.piece_of_clothing import SoldPieceOfClothing


def _transformation_size(size_str: str):
    if size_str.find("-") != -1:
        size = size_str.split("-")
        return ClothingSizeByHeight(min=int(size[0]), max=int(size[1]))
    else:
        return ClothingSizeByHeight(min=int(size_str), max=int(size_str))


def _transformation_price(price_str: str):
    try:
        return float(price_str)
    except Exception:
        return None


def _transformation_int(int_str):
    try:
        return int(int_str)
    except Exception:
        return None


def transformation(file_name: str):
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            data = []
            first_row = True
            for row in reader:
                if len(row) == 0:
                    continue
                if first_row:
                    fields = row
                    first_row = False
                    continue
                data_row = {"id": uuid4()}
                for i in range(len(fields)):
                    if fields[i] == "size":
                        data_row[fields[i]] = _transformation_size(row[i])
                    elif fields[i] in ["purchase_price", "original_price", "selling_price", "post_fee"]:
                        data_row[fields[i]] = _transformation_price(row[i])
                    elif fields[i] == "pieces":
                        data_row[fields[i]] = _transformation_int(row[i])
                    else:
                        data_row[fields[i]] = row[i]
                if data_row["selling_price"] is not None:
                    data.append(SoldPieceOfClothing(**data_row))
            return data
    except Exception as e:
        print(e)


def make_analysis(data: List):
    analysis = {"gifts": 0}
    CALC_FIELDS = ["purchase_price", "original_price", "selling_price", "post_fee"]
    for item in data:
        for field in CALC_FIELDS:
            field_value = getattr(item, field)
            if field_value is not None:
                if f"{field}_total" in analysis:
                    analysis[f"{field}_total"] += field_value
                else:
                    analysis[f"{field}_total"] = field_value
                if field == "selling_price" and field_value == 0:
                    analysis["gifts"] += 1

    analysis["total_discount"] = analysis['purchase_price_total'] - analysis['original_price_total']
    analysis["total_discount_percent"] = 1 - analysis['purchase_price_total'] / analysis['original_price_total']
    analysis["total_reward"] = analysis['selling_price_total'] - analysis["post_fee_total"]
    analysis["total_reward_percent"] = analysis['selling_price_total'] / (
                analysis["post_fee_total"] + analysis["purchase_price_total"])
    analysis["total_real_price"] = analysis['purchase_price_total'] - analysis["total_reward"]
    analysis["total_discount_against_original"] = 1 - analysis["total_real_price"] / analysis['original_price_total']
    return analysis
