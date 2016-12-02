from django.http import HttpResponse, Http404, HttpResponseRedirect
import codecs
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.conf import settings
import numpy as np, pandas as pd
import geopandas as gpd
from os.path import join
from io import BytesIO
from matplotlib.colors import Normalize
from pysal.esda.mapclassify import Fisher_Jenks
import geopandas.tools
from shapely.geometry import Point
from .forms import InputForm
from .models import AREA_DICT

#creates poverty map
def poverty(request):

    filename = join(settings.STATIC_ROOT, 'myapp/Community_Areas.geojson')
    community_df = gpd.read_file(filename)
    community_df.rename(columns = {"area_numbe" : "Area_Number"}, inplace = True)
    community_df.rename(columns = {"community" : "Area_Name"}, inplace = True)
    community_df["Area_Number"] = community_df["Area_Number"].astype(int)
    community_df.index = community_df.index + 1
    file_name = join(settings.STATIC_ROOT, 'myapp/Census.csv')
    poverty_df = pd.read_csv(file_name)
    poverty_df.index = poverty_df.index + 1
    poverty_df["INCOME"] = poverty_df["INCOME"].astype(int)
    mapped_poverty = pd.merge(community_df, poverty_df, how = "inner", left_on = "Area_Number", right_index = True)

    ax = mapped_poverty.plot(column = "INCOME", scheme = "fisher_jenks", k = 8, cmap = "gnuplot", legend = True, alpha = 0.4, linewidth = 0.2, figsize = (16,10))
    ax.set_title("Per Capita Income by Neighborhood", fontsize = 24)
    ax.set_axis_off()
    figfile = ax.get_figure()
    figfile = BytesIO()

    try: ax.figure.savefig(figfile, format = 'png')
    except ValueError: raise Http404("No such color")
    figfile.seek(0)

    return HttpResponse(figfile.read(), content_type="image/png")

#displays poverty and housing maps on home page
def display_index(request):

        params = {'title' : "Poverty, Affordable Housing, and Health Outcomes in Chicago",
                  'pic_source' : reverse_lazy("finalapp:poverty"),
                  'pic_source2' : reverse_lazy("finalapp:map10")}

        return render(request, 'index.html', params)

#creates the assault map
def embedded_map(request):

   file_name = join(settings.STATIC_ROOT,'myapp/Health.csv')
   assault_df = pd.read_csv(file_name, usecols = ["Area_Number", "Area_Name", "Assault"])
   assault_df.index = assault_df.index + 1
   assault_df.dropna(inplace = True)
   assault_df["Area_Name"] = assault_df["Area_Name"]
   assault_df["Assault"] = assault_df["Assault"].astype(float)

   filename = join(settings.STATIC_ROOT, 'myapp/Community_Areas.geojson')
   community_df = gpd.read_file(filename)
   community_df.rename(columns = {"area_numbe" : "Area_Number"}, inplace = True)
   community_df.rename(columns = {"community" : "Area_Name"}, inplace = True)
   community_df["Area_Number"] = community_df["Area_Number"].astype(int)
   community_df.index = community_df.index + 1

   mapped_health = pd.merge(community_df, assault_df, how = "inner", left_on = "Area_Number", right_index = True)
   ax = mapped_health.plot(column = "Assault", scheme = "fisher_jenks", k = 9, cmap = "BuGn", legend = True, alpha = 0.7, linewidth = 0.2, figsize = (16,10))
   ax.set_title("Cause of Death by Neighborhood, Assault", fontsize = 20)
   ax.set_axis_off()
   figfile = ax.get_figure()
   figfile = BytesIO()

   try: ax.figure.savefig(figfile, format = 'png')
   except ValueError: raise Http404("No such color")
   figfile.seek(0)

   return HttpResponse(figfile.read(), content_type="image/png")

#creates the diabetes map
def embedded_map2(request):

   file_name = join(settings.STATIC_ROOT,'myapp/Health.csv')
   diabetes_df = pd.read_csv(file_name, usecols = ["Area_Number", "Area_Name", "Diabetes"])
   diabetes_df.index = diabetes_df.index + 1
   diabetes_df.dropna(inplace = True)
   diabetes_df["Area_Name"] = diabetes_df["Area_Name"]
   diabetes_df["Diabetes"] = diabetes_df["Diabetes"].astype(float)
   filename = join(settings.STATIC_ROOT, 'myapp/Community_Areas.geojson')
   community_df = gpd.read_file(filename)
   community_df.rename(columns = {"area_numbe" : "Area_Number"}, inplace = True)
   community_df.rename(columns = {"community" : "Area_Name"}, inplace = True)
   community_df["Area_Number"] = community_df["Area_Number"].astype(int)
   community_df.index = community_df.index + 1
   mapped_health = pd.merge(community_df, diabetes_df, how = "inner", left_on = "Area_Number", right_index = True)
   ax = mapped_health.plot(column = "Diabetes", scheme = "fisher_jenks", k = 7, cmap = "OrRd", legend = True, alpha = 0.7, linewidth = 0.2, figsize = (16,10))
   ax.set_title("Cause of Death by Neighborhood, Diabetes", fontsize = 20)
   ax.set_axis_off()
   figfile = ax.get_figure()
   figfile = BytesIO()
   try: ax.figure.savefig(figfile, format = 'png')
   except ValueError: raise Http404("No such color")
   figfile.seek(0)

   return HttpResponse(figfile.read(), content_type="image/png")

#creates the firearm map
def embedded_map3(request):

   file_name = join(settings.STATIC_ROOT,'myapp/Health.csv')
   firearm_df = pd.read_csv(file_name, usecols = ["Area_Number", "Area_Name", "Firearm"])
   firearm_df.index = firearm_df.index + 1
   firearm_df.dropna(inplace = True)
   firearm_df["Area_Name"] = firearm_df["Area_Name"]
   firearm_df["Firearm"] = firearm_df["Firearm"].astype(float)
   filename = join(settings.STATIC_ROOT, 'myapp/Community_Areas.geojson')
   community_df = gpd.read_file(filename)
   community_df.rename(columns = {"area_numbe" : "Area_Number"}, inplace = True)
   community_df.rename(columns = {"community" : "Area_Name"}, inplace = True)
   community_df["Area_Number"] = community_df["Area_Number"].astype(int)
   community_df.index = community_df.index + 1
   mapped_health = pd.merge(community_df, firearm_df, how = "inner", left_on = "Area_Number", right_index = True)
   ax = mapped_health.plot(column = "Firearm", scheme = "fisher_jenks", k = 9, cmap = "PuBu", legend = True, alpha = 0.6, linewidth = 0.2, figsize = (16,10))
   ax.set_title("Cause of Death by Neighborhood, Firearm", fontsize = 20)
   ax.set_axis_off()
   figfile = ax.get_figure()
   figfile = BytesIO()
   try: ax.figure.savefig(figfile, format = 'png')
   except ValueError: raise Http404("No such color")
   figfile.seek(0)

   return HttpResponse(figfile.read(), content_type="image/png")

#creates the stroke map
def embedded_map4(request):

   file_name = join(settings.STATIC_ROOT,'myapp/Health.csv')
   stroke_df = pd.read_csv(file_name, usecols = ["Area_Number", "Area_Name", "Stroke"])
   stroke_df.index = stroke_df.index + 1
   stroke_df.dropna(inplace = True)
   stroke_df["Area_Name"] = stroke_df["Area_Name"]
   stroke_df["Stroke"] = stroke_df["Stroke"].astype(float)
   filename = join(settings.STATIC_ROOT, 'myapp/Community_Areas.geojson')
   community_df = gpd.read_file(filename)
   community_df.rename(columns = {"area_numbe" : "Area_Number"}, inplace = True)
   community_df.rename(columns = {"community" : "Area_Name"}, inplace = True)
   community_df["Area_Number"] = community_df["Area_Number"].astype(int)
   community_df.index = community_df.index + 1
   mapped_health = pd.merge(community_df, stroke_df, how = "inner", left_on = "Area_Number", right_index = True)
   ax = mapped_health.plot(column = "Stroke", scheme = "fisher_jenks", k = 8, cmap = "RdPu", legend = True, alpha = 0.6, linewidth = 0.2, figsize = (16,10))
   ax.set_title("Cause of Death by Neighborhood, Stroke", fontsize = 20)
   ax.set_axis_off()
   figfile = ax.get_figure()
   figfile = BytesIO()
   try: ax.figure.savefig(figfile, format = 'png')
   except ValueError: raise Http404("No such color")
   figfile.seek(0)

   return HttpResponse(figfile.read(), content_type="image/png")

#creates the breast cancer map
def embedded_map5(request):

   file_name = join(settings.STATIC_ROOT,'myapp/Health.csv')
   breast_df = pd.read_csv(file_name, usecols = ["Area_Number", "Area_Name", "Breast_Cancer"])
   breast_df.index = breast_df.index + 1
   breast_df.dropna(inplace = True)
   breast_df["Area_Name"] = breast_df["Area_Name"]
   breast_df["Breast_Cancer"] = breast_df["Breast_Cancer"].astype(float)
   filename = join(settings.STATIC_ROOT, 'myapp/Community_Areas.geojson')
   community_df = gpd.read_file(filename)
   community_df.rename(columns = {"area_numbe" : "Area_Number"}, inplace = True)
   community_df.rename(columns = {"community" : "Area_Name"}, inplace = True)
   community_df["Area_Number"] = community_df["Area_Number"].astype(int)
   community_df.index = community_df.index + 1
   mapped_health = pd.merge(community_df, breast_df, how = "inner", left_on = "Area_Number", right_index = True)
   ax = mapped_health.plot(column = "Breast_Cancer", scheme = "fisher_jenks", k = 8, cmap = "YlGn", legend = True, alpha = 0.6, linewidth = 0.2, figsize = (16,10))
   ax.set_title("Cause of Death by Neighborhood, Breast Cancer", fontsize = 20)
   ax.set_axis_off()
   figfile = ax.get_figure()
   figfile = BytesIO()
   try: ax.figure.savefig(figfile, format = 'png')
   except ValueError: raise Http404("No such color")
   figfile.seek(0)

   return HttpResponse(figfile.read(), content_type="image/png")

#creates the coloectal cancer map
def embedded_map6(request):

   file_name = join(settings.STATIC_ROOT,'myapp/Health.csv')
   colorectal_df = pd.read_csv(file_name, usecols = ["Area_Number", "Area_Name", "Colorectal_Cancer"])
   colorectal_df.index = colorectal_df.index + 1
   colorectal_df.dropna(inplace = True)
   colorectal_df["Area_Name"] = colorectal_df["Area_Name"]
   colorectal_df["Colorectal_Cancer"] = colorectal_df["Colorectal_Cancer"].astype(float)
   filename = join(settings.STATIC_ROOT, 'myapp/Community_Areas.geojson')
   community_df = gpd.read_file(filename)
   community_df.rename(columns = {"area_numbe" : "Area_Number"}, inplace = True)
   community_df.rename(columns = {"community" : "Area_Name"}, inplace = True)
   community_df["Area_Number"] = community_df["Area_Number"].astype(int)
   community_df.index = community_df.index + 1
   mapped_health = pd.merge(community_df, colorectal_df, how = "inner", left_on = "Area_Number", right_index = True)
   ax = mapped_health.plot(column = "Colorectal_Cancer", scheme = "fisher_jenks", k = 7, cmap = "YlGn", legend = True, alpha = 0.6, linewidth = 0.2, figsize = (16,10))
   ax.set_title("Cause of Death by Neighborhood, Colorectal Cancer", fontsize = 20)
   ax.set_axis_off()
   figfile = ax.get_figure()
   figfile = BytesIO()
   try: ax.figure.savefig(figfile, format = 'png')
   except ValueError: raise Http404("No such color")
   figfile.seek(0)

   return HttpResponse(figfile.read(), content_type="image/png")

#creates the lung cancer map
def embedded_map7(request):

   file_name = join(settings.STATIC_ROOT,'myapp/Health.csv')
   lung_df = pd.read_csv(file_name, usecols = ["Area_Number", "Area_Name", "Lung_Cancer"])
   lung_df.index = lung_df.index + 1
   lung_df.dropna(inplace = True)
   lung_df["Area_Name"] = lung_df["Area_Name"]
   lung_df["Lung_Cancer"] = lung_df["Lung_Cancer"].astype(float)
   filename = join(settings.STATIC_ROOT, 'myapp/Community_Areas.geojson')
   community_df = gpd.read_file(filename)
   community_df.rename(columns = {"area_numbe" : "Area_Number"}, inplace = True)
   community_df.rename(columns = {"community" : "Area_Name"}, inplace = True)
   community_df["Area_Number"] = community_df["Area_Number"].astype(int)
   community_df.index = community_df.index + 1
   mapped_health = pd.merge(community_df, lung_df, how = "inner", left_on = "Area_Number", right_index = True)
   ax = mapped_health.plot(column = "Lung_Cancer", scheme = "fisher_jenks", k = 7, cmap = "YlGn", legend = True, alpha = 0.6, linewidth = 0.2, figsize = (16,10))
   ax.set_title("Cause of Death by Neighborhood, Lung Cancer", fontsize = 20)
   ax.set_axis_off()
   figfile = ax.get_figure()
   figfile = BytesIO()
   try: ax.figure.savefig(figfile, format = 'png')
   except ValueError: raise Http404("No such color")
   figfile.seek(0)

   return HttpResponse(figfile.read(), content_type="image/png")

#creates the prostate cancer map
def embedded_map8(request):

    file_name = join(settings.STATIC_ROOT,'myapp/Health.csv')
    prostate_df = pd.read_csv(file_name, usecols = ["Area_Number", "Area_Name", "Prostate_Cancer"])
    prostate_df.index = prostate_df.index + 1
    prostate_df.dropna(inplace = True)
    prostate_df["Area_Name"] = prostate_df["Area_Name"]
    prostate_df["Prostate_Cancer"] = prostate_df["Prostate_Cancer"].astype(float)
    filename = join(settings.STATIC_ROOT, 'myapp/Community_Areas.geojson')
    community_df = gpd.read_file(filename)
    community_df.rename(columns = {"area_numbe" : "Area_Number"}, inplace = True)
    community_df.rename(columns = {"community" : "Area_Name"}, inplace = True)
    community_df["Area_Number"] = community_df["Area_Number"].astype(int)
    community_df.index = community_df.index + 1
    mapped_health = pd.merge(community_df, prostate_df, how = "inner", left_on = "Area_Number", right_index = True)
    ax = mapped_health.plot(column = "Prostate_Cancer", scheme = "fisher_jenks", k = 9, cmap = "YlGn", legend = True, alpha = 0.6, linewidth = 0.2, figsize = (16,10))
    ax.set_title("Cause of Death by Neighborhood, Prostate Cancer", fontsize = 20)
    ax.set_axis_off()
    figfile = ax.get_figure()
    figfile = BytesIO()
    try: ax.figure.savefig(figfile, format = 'png')
    except ValueError: raise Http404("No such color")
    figfile.seek(0)

    return HttpResponse(figfile.read(), content_type="image/png")

#creates the cancer map
def embedded_map9(request):

    file_name = join(settings.STATIC_ROOT,'myapp/Health.csv')
    cancer_df = pd.read_csv(file_name, usecols = ["Area_Number", "Area_Name", "Cancer"])
    cancer_df.index = cancer_df.index + 1
    cancer_df.dropna(inplace = True)
    cancer_df["Area_Name"] = cancer_df["Area_Name"]
    cancer_df["Cancer"] = cancer_df["Cancer"].astype(float)
    filename = join(settings.STATIC_ROOT, 'myapp/Community_Areas.geojson')
    community_df = gpd.read_file(filename)
    community_df.rename(columns = {"area_numbe" : "Area_Number"}, inplace = True)
    community_df.rename(columns = {"community" : "Area_Name"}, inplace = True)
    community_df["Area_Number"] = community_df["Area_Number"].astype(int)
    community_df.index = community_df.index + 1
    mapped_health = pd.merge(community_df, cancer_df, how = "inner", left_on = "Area_Number", right_index = True)
    ax = mapped_health.plot(column = "Cancer", scheme = "fisher_jenks", k = 9, cmap = "YlGn", legend = True, alpha = 0.6, linewidth = 0.2, figsize = (16,10))
    ax.set_title("Cause of Death by Neighborhood, Cancer", fontsize = 20)
    ax.set_axis_off()
    figfile = ax.get_figure()
    figfile = BytesIO()
    try: ax.figure.savefig(figfile, format = 'png')
    except ValueError: raise Http404("No such color")
    figfile.seek(0)

    return HttpResponse(figfile.read(), content_type="image/png")

#display all cause of death maps
def display_pic(request):

    params = {'title' : "Top Nine Causes of Death by Neighborhood",
              'pic_source' : reverse_lazy("finalapp:map"),
              'pic_source2' : reverse_lazy("finalapp:map2"),
              'pic_source3' : reverse_lazy("finalapp:map3"),
              'pic_source4' : reverse_lazy("finalapp:map4"),
              'pic_source5' : reverse_lazy("finalapp:map5"),
              'pic_source6' : reverse_lazy("finalapp:map6"),
              'pic_source7' : reverse_lazy("finalapp:map7"),
              'pic_source8' : reverse_lazy("finalapp:map8"),
              'pic_source9' : reverse_lazy("finalapp:map9")}

    return render(request, 'view_map.html', params)

#creates the housing map
def embedded(request):

    filename = join(settings.STATIC_ROOT, 'myapp/Community_Areas.geojson')
    community_df = gpd.read_file(filename)
    community_df.rename(columns = {"area_numbe" : "Area_Number"}, inplace = True)
    community_df.rename(columns = {"community" : "Community_Area"}, inplace = True)
    community_df["Area_Number"] = community_df["Area_Number"].astype(int)
    community_df.index = community_df.index + 1

    file_name = join(settings.STATIC_ROOT,'myapp/Housing.csv')
    housing_df = pd.read_csv(file_name, usecols = [0,11,12])
    housing_df.index = housing_df.index + 1
    housing_df.dropna(inplace = True)
    housing_df["Area_Number"] = housing_df["Area_Number"].astype(int)
    geometry = [Point(xy) for xy in zip(housing_df.Longitude, housing_df.Latitude)]

    housing_coords = gpd.GeoDataFrame(housing_df, crs = community_df.crs, geometry=geometry)
    located_housing = gpd.tools.sjoin(housing_coords, community_df, how = 'left', op = 'within')
    located_housing.to_crs(epsg = 2790)
    located_housing.rename(columns = {"index_right" : "area"}, inplace = True)

    count = located_housing.groupby("Community_Area").count()[["Latitude"]]
    count.rename(columns = {"Latitude" : "Count"}, inplace = True)
    housing_number = pd.merge(community_df, count, how = "left", left_on = "Community_Area", right_index = True)
    housing_number.fillna(0, inplace = True)
    bx = housing_number.plot(column = "Count", scheme = "fisher_jenks", k = 9, cmap = "Greens", legend = True, alpha = 0.6, linewidth = 0.2, figsize = (16,10))
    bx.set_title("Affordable Housing Sites by Neighborhood", fontsize = 25)
    bx.set_axis_off()
    figfile = bx.get_figure()
    figfile = BytesIO()
    try: bx.figure.savefig(figfile, format = 'png')
    except ValueError: raise Http404("No such color")
    figfile.seek(0)

    return HttpResponse(figfile.read(), content_type="image/png")

#creates the infant mortality map
def embedded2(request):

    file_name = join(settings.STATIC_ROOT,'myapp/Health.csv')
    infant_df = pd.read_csv(file_name, usecols = ["Area_Number", "Area_Name", "Infant_Mortality_Rate"])
    infant_df.index = infant_df.index + 1
    infant_df.dropna(inplace = True)
    infant_df["Area_Name"] = infant_df["Area_Name"]
    infant_df["Infant_Mortality_Rate"] = infant_df["Infant_Mortality_Rate"].astype(float)
    filename = join(settings.STATIC_ROOT, 'myapp/Community_Areas.geojson')
    community_df = gpd.read_file(filename)
    community_df.rename(columns = {"area_numbe" : "Area_Number"}, inplace = True)
    community_df.rename(columns = {"community" : "Area_Name"}, inplace = True)
    community_df["Area_Number"] = community_df["Area_Number"].astype(int)
    community_df.index = community_df.index + 1
    mapped_health = pd.merge(community_df, infant_df, how = "inner", left_on = "Area_Number", right_index = True)
    ax = mapped_health.plot(column = "Infant_Mortality_Rate", scheme = "fisher_jenks", k = 7, cmap = "Oranges", legend = True, alpha = 0.7, linewidth = 0.2, figsize = (16,10))
    ax.set_title("Infant Mortality by Neighborhood", fontsize = 20)
    ax.set_axis_off()
    figfile = ax.get_figure()
    figfile = BytesIO()
    try: ax.figure.savefig(figfile, format = 'png')
    except ValueError: raise Http404("No such color")
    figfile.seek(0)

    return HttpResponse(figfile.read(), content_type="image/png")

#display infant mortality map
def display_map2(request):

    params = {'title' : "Infant Mortality by Neighborhood",
              'pic_source' : reverse_lazy("finalapp:map11")}

    return render(request, 'infant.html', params)

#creates the data table and dropdown menu
def form(request):

    area = request.GET.get('area', '')
    if not area: area = request.POST.get('area','Hyde Park')

    filename = join(settings.STATIC_ROOT, 'myapp/Health.csv')
    df = pd.read_csv(filename,  usecols = ["Area_Number", "Area_Name", "Assault", "Breast_Cancer", "Colorectal_Cancer", "Diabetes", "Firearm", "Infant_Mortality_Rate", "Lung_Cancer", "Prostate_Cancer", "Stroke"])
    df.rename(columns = {"Area_Number" : "Area Number"}, inplace = True)
    df.rename(columns = {"Area_Name" : "Area Name"}, inplace = True)
    df.rename(columns = {"Breast_Cancer" : "Breast Cancer"}, inplace = True)
    df.rename(columns = {"Colorectal_Cancer" : "Colorectal Cancer"}, inplace = True)
    df.rename(columns = {"Infant_Mortality_Rate" : "Infant Mortality Rate"}, inplace = True)
    df.rename(columns = {"Lung_Cancer" : "Lung Cancer"}, inplace = True)
    df.rename(columns = {"Prostate_Cancer" : "Prostate Cancer"}, inplace = True)

    df.index=df.index + 1
    if area: df = df[df["Area Name"] == (area)]

    table = df.to_html(float_format = "%.3f", classes = "table table-striped", index_names = False)
    table = table.replace('border="1"','border="0"')
    table = table.replace('style="text-align: right;"', "")

    params = {'title' : 'Mortality Rates by Neighborhood',
            'form_action' : reverse_lazy('finalapp:form'),
              'form_method' : 'get',
              'form' : InputForm({"area":area}),
              "area" : AREA_DICT[area],
              'html_table' : table}

    return render(request, 'form.html', params)
