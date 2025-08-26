from django.urls import path
from . import views

app_name = 'csv_upload'

urlpatterns = [
    path('', views.upload_csv, name='upload'),
    path('table/<int:table_id>/', views.view_table, name='view_table'),
    path('delete/<int:table_id>/', views.delete_table, name='delete_table'),
]
