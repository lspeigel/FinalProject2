from django.conf.urls import url
from . import views

app_name = 'finalapp'
urlpatterns = [


    url(r'^poverty/$', views.poverty, name = "poverty"), #poverty map
    url(r'^display_index/$', views.display_index, name="index"), #home page
    url(r'^form/$', views.form, name = "form"), #mortality rates by neighborhood
    url(r'^map/$', views.embedded_map, name = "map"),#assault map
    url(r'^map2/$', views.embedded_map2, name = "map2"),#diabetes map
    url(r'^map3/$', views.embedded_map3, name = "map3"),#firearm map
    url(r'^map4/$', views.embedded_map4, name = "map4"), #stroke map
    url(r'^map5/$', views.embedded_map5, name = "map5"),#breast cancer
    url(r'^map6/$', views.embedded_map6, name = "map6"),#colorectal cancer
    url(r'^map7/$', views.embedded_map7, name = "map7"), #lung cancer
    url(r'^map8/$', views.embedded_map8, name = "map8"), #prostate cancer
    url(r'^map9/$', views.embedded_map9, name = "map9"), #cancer map
    url(r'^display_pic/$', views.display_pic, name="pic"), #cause of death maps page
    url(r'^map10/$', views.embedded, name = "map10"),#housing map
    url(r'^map11/$', views.embedded2, name = "map11"),#infant mortality map
    url(r'^display_map2/$', views.display_map2, name="maps2"), #infant mortality page


    ]
