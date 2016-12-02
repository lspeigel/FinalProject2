import sqlite3
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

con = sqlite3.connect("data.sqlite")

df = pd.read_sql_query("select health.Area_Name, health.Breast_Cancer, health.Assault, health.Colorectal_Cancer, health.Diabetes, health.Firearm, health.Infant_Mortality_Rate, health.Lung_Cancer, health.Prostate_Cancer, health.Stroke, census.INCOME from health inner join census on health.Area_Number = census.Area_Number group by health.Area_Name", con)

print(df)
