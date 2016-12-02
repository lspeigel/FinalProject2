import matplotlib
import numpy as np
import geopandas as gpd, pandas as pd
import matplotlib.pyplot as plt



health_df = pd.read_csv("Health.csv", usecols = ["Area_Number", "Area_Name", "Assault", "Breast_Cancer", "Colorectal_Cancer", "Diabetes", "Firearm", "Infant_Mortality_Rate", "Lung_Cancer", "Prostate_Cancer", "Stroke"])
health_df.index = health_df.index + 1
health_df.dropna(inplace = True)
health_df["Area_Name"] = health_df["Area_Name"]
health_df["Firearm"] = health_df["Firearm"].astype(float)
health_df["Breast_Cancer"] = health_df["Breast_Cancer"].astype(float)



community_df = gpd.read_file("Community_Areas.geojson")
community_df.rename(columns = {"area_numbe" : "Area_Number"}, inplace = True)
community_df.rename(columns = {"community" : "Area_Name"}, inplace = True)
community_df["Area_Number"] = community_df["Area_Number"].astype(int)
community_df.index = community_df.index + 1

#cause of death by neighborhood
mapped_health = pd.merge(community_df, assault_df, how = "inner", right_on = "Area_Number", left_index = True)

ax = mapped_health.plot(column = "Assault", scheme = "fisher_jenks", k = 7, cmap = "summer", legend = True, alpha = 0.4, linewidth = 0.2, figsize = (12,8))

ax.set_title("Cause of Death by Neighborhood, Assault", fontsize = 18)
ax.set_axis_off()




#map of affordable housing sites by neighborhood
housing_df = pd.read_csv("Housing.csv", usecols = [0,11,12])
housing_df.index = housing_df.index + 1
housing_df.dropna(inplace = True)
housing_df["Area_Number"] = housing_df["Area_Number"].astype(int)

geometry = [Point(xy) for xy in zip(housing_df.Longitude, housing_df.Latitude)]

housing_coords = gpd.GeoDataFrame(housing_df, crs = community_df.crs, geometry=geometry)
located_housing = gpd.tools.sjoin(housing_coords, community_df, how = 'left', op = 'within')

located_housing.rename(columns = {"index_right" : "area"}, inplace = True)
located_housing.to_crs(epsg = 2790)
count = located_housing.groupby("Community_Area").count()[["Latitude"]]
count.rename(columns = {"Latitude" : "Count"}, inplace = True)

housing_number = pd.merge(community_df, count, how = "left", left_on = "Community_Area", right_index = True)
housing_number.fillna(0, inplace = True)

bx = housing_number.plot(column = "Count", scheme = "fisher_jenks", k = 9, cmap = "Greens", legend = True, alpha = 0.6, linewidth = 0.2, figsize = (16,10))
bx.set_title("Affordable Housing Sites by Neighborhood", fontsize = 16)
bx.set_axis_off()
