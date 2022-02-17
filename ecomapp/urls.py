from django.conf import settings
from django.conf.urls.static import static

from .import views
from django.urls import path



urlpatterns = [

    path('index/',views.index),
    path('index_list/',views.index_list),
    path('pro_page/',views.pro_page),
    path('index_base/',views.index_base),
    path('sofa_list/',views.sofa_list),
    path('add_sofa/',views.add_sofa),
    path('view_sofa/',views.view_sofa),
    path('detail_sofa/',views.detail_sofa),
    path('dining_create/',views.dining_create),
    path('dining_list/',views.dining_list),
    path('view_dining/',views.view_dining),
    path('armchair_create/',views.armchair_create),
    path('armchair_list/',views.armchair_list),
    path('view_armchair/',views.view_armchair),
    path('create_bed/', views.create_bed),
    path('bed_list/', views.bed_list),
    path('view_bed/', views.view_bed),
    path('cus_reg/',views.cus_reg),
    path('admin_reg/',views.admin_reg),
    path('login/',views.login),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)