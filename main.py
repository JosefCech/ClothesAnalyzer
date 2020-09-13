# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from src.processor.transformation import transformation, make_analysis

data = transformation("./data/data.csv")
# celkova cena, celkova potencionalni cena, celkovy prodej , zisk
analytics = make_analysis(data)

[print(f"{i} - {analytics[i]}") for i in analytics]