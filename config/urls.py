from django.contrib import admin
from django.urls import path
from pages.views import home_page_view  # This imports your logic

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page_view, name='home'),  # The empty '' means the home page
]