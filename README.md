# FinalProject

###

1. Questions:

  Maps:
  a. Per capita income by neighborhood
  b. Prevalence of cause of death by neighborhood--what is the concentration of fatal causes in each area?
  c. Affordable housing concentration map
  d. Infant mortality rates by neighborhood


  Cause of death table:
  10 causes are documented by the city: assault(homicide), breast cancer in women, cancer, colorectal cancer, diabetes, firearm-related, infant mortality rate, lung cancer, prostate cancer in men, stroke. Infant mortality rate is considered separately from the other nine causes.

2. Datasources:
    Affordable housing sites: https://data.cityofchicago.org/Community-Economic-Development/Affordable-Rental-Housing-Developments/s6ha-ppgi

    Socioeconomic indicators: https://data.cityofchicago.org/Health-Human-Services/Census-Data-Selected-socioeconomic-indicators-in-C/kn9c-c2s2

    Health and mortality data: https://data.cityofchicago.org/Health-Human-Services/Public-Health-Statistics-Selected-public-health-in/iqnk-2tcu

    Community area map: https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Community-Areas-current-/cauq-8yn6

    All data files contain a community area number, one for each neighborhood in Chicago (N=77), this will be the index for all analysis in our webapp.

    Download: all data files were exported as CSV files. The community area boundary file was exported as a GeoJson file.

3. Code structure:

    Use SQL to create a database that has three tables, one for each of the datasources.

    sqlite3 data.sqlite

    CREATE TABLE health (Area_Number REAL PRIMARY KEY NOT NULL, Area_Name TEXT, Birth_Rate REAL, General_Fertility_Rate REAL, Low_Birth_Weight REAL, Prenatal_Care REAL, Preterm_Births REAL, Teen_Birth_Rate REAL, Assault REAL, Breast_Cancer REAL, Cancer REAL, Colorectal_Cancer REAL, Diabetes REAL, Firearm REAL, Infant_Mortality_Rate REAL, Lung_Cancer REAL, Prostate_Cancer REAL, Stroke REAL, Childhood_Blood_Lead REAL, Childhood_Lead_Poisoning REAL, Gonorrhea_in_Females REAL, Gonorrhea_in_Males REAL, Tuberculosis REAL, Below_Poverty_Level REAL, Crowded_Housing REAL, Dependency REAL, No_High_School_Diploma REAL, Per_Capita_Income INTEGER, Unemployment REAL);
    .mode csv
    .import Health.csv health

    CREATE TABLE census (Area_Number REAL PRIMARY KEY NOT NULL, Area_Name TEXT, PERCENT_HOUSING_CROWDED REAL, PERCENT_HOUSEHOLDS_BELOW_POVERTY REAL, PERCENT_UNEMPLOYED REAL, PERCENT_WITHOUT_HIGH_SCHOOL_DIPLOMA REAL, PERCENT_AGED REAL, INCOME REAL, HARDSHIP_INDEX REAL);
    .mode csv
    .import Census.csv census

    CREATE TABLE housing (Area_Number REAL, Area_Name TEXT, Property_Type TEXT, Property_Name TEXT, Address TEXT,	Zip_Code REAL, Phone_Number REAL, Management_Company TEXT, Units REAL, X_Coordinate REAL, Y_Coordinate REAL, Latitude REAL, Longitude	REAL, Location REAL);
    .mode csv
    .import Housing.csv housing


4. Site layout

  We created a webapp that runs on Django.It is called finalapp, stored in the mysite folder.

  To access it, go to the link http://127.0.0.1:8000/finalapp/display_index/ after running the server.
  On the site you can go the 5 different sections using the navigation bar.
  All the data that we use in the views is stored under the static folder.
