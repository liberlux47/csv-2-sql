from django.urls import path
from . import views

app_name = 'csv_upload'

urlpatterns = [
    path('', views.upload_csv, name='upload'),
    path('table/<int:table_id>/', views.view_table, name='view_table'),
    path('edit/<int:table_id>/', views.edit_table, name='edit_table'),
    path('edit/<int:table_id>/column/<str:column_name>/', views.configure_column, name='configure_column'),
    path('delete/<int:table_id>/', views.delete_table, name='delete_table'),
    path('api/table/<int:table_id>/update-cell/', views.update_cell, name='update_cell'),
    path('api/table/<int:table_id>/reload/', views.reload_table_data, name='reload_table_data'),
]
