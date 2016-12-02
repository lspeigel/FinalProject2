import sqlite3

sqlite3 data.sqlite

CREATE TABLE health (Area_Number REAL PRIMARY KEY NOT NULL, Area_Name TEXT, Birth_Rate REAL, General_Fertility_Rate REAL, Low_Birth_Weight REAL, Prenatal_Care REAL, Preterm_Births REAL, Teen_Birth_Rate REAL, Assault REAL, Breast_Cancer REAL, Cancer REAL, Colorectal_Cancer REAL, Diabetes REAL, Firearm REAL, Infant_Mortality_Rate REAL, Lung_Cancer REAL, Prostate_Cancer REAL, Stroke REAL, Childhood_Blood_Lead REAL, Childhood_Lead_Poisoning REAL, Gonorrhea_in_Females REAL, Gonorrhea_in_Males REAL, Tuberculosis REAL, Below_Poverty_Level REAL, Crowded_Housing REAL, Dependency REAL, No_High_School_Diploma REAL, Per_Capita_Income INTEGER, Unemployment REAL);
.mode csv
.import Health.csv health


CREATE TABLE census (Firstrow = 2, Area_Number REAL PRIMARY KEY NOT NULL, Area_Name TEXT, PERCENT_HOUSING_CROWDED REAL, PERCENT_HOUSEHOLDS_BELOW_POVERTY REAL, PERCENT_UNEMPLOYED REAL, PERCENT_WITHOUT_HIGH_SCHOOL_DIPLOMA REAL, PERCENT_AGED REAL, INCOME REAL, HARDSHIP_INDEX REAL);
.mode csv
.import Census.csv census


CREATE TABLE housing (Area_Number REAL, Area_Name TEXT, Property_Type TEXT, Property_Name TEXT, Address TEXT,	Zip_Code REAL, Phone_Number REAL, Management_Company TEXT, Units REAL, X_Coordinate REAL, Y_Coordinate REAL, Latitude REAL, Longitude	REAL, Location REAL);
.mode csv
.import Housing.csv housing
