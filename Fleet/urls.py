from django.contrib import admin
from django.urls import path
from ccc.views import login_view, landing_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login_view, name='login_page'),
    path('', landing_view, name='index_page')
]

admin.site.site_header = 'DataFleet Administration'
admin.site.site_title = 'DataFleet Administration'