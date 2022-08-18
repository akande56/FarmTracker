import imp
from django.contrib import admin
from django.urls import re_path, include
from django.views.generic import TemplateView
from contrib.views import char_count, PostView

urlpatterns = [
    #admin
    re_path("admin/", admin.site.urls),
    
    # # authentication
    re_path(r'^api-auth/', include('rest_framework.urls')),
    re_path(r'^rest-auth/', include('rest_auth.urls')),
    re_path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),

    # app
    re_path(r'^api-farmer/', include('farmers.urls')),
    re_path(r'^api-inspector/', include('inspectors.urls')),

    re_path("char_count", char_count, name="char_count"),
    re_path("post/", PostView.as_view(), name='post'),

    # hompage 
    re_path(".*", TemplateView.as_view(template_name="index.html")),

]
