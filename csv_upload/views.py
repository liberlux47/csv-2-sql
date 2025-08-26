from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
import pandas as pd
import json
import io
from .models import CSVUpload, CSVData
from .forms import CSVUploadForm


def upload_csv(request):
    """Main view for CSV upload and display"""
    form = CSVUploadForm()
    csv_upload = None
    table_data = None
    columns = None
    
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                csv_file = form.cleaned_data['csv_file']
                table_name = form.cleaned_data['table_name']
                
                # Check if table name already exists
                if CSVUpload.objects.filter(table_name=table_name).exists():
                    messages.error(request, f'Table "{table_name}" already exists. Please choose a different name.')
                else:
                    # Process the CSV file
                    csv_upload = process_csv_file(csv_file, table_name)
                    messages.success(request, f'CSV file uploaded successfully! Created table: {table_name}')
                    
                    # Get the data for display
                    table_data = get_table_data(csv_upload)
                    columns = csv_upload.get_columns()
                    
            except Exception as e:
                messages.error(request, f'Error processing CSV file: {str(e)}')
    
    # Get all existing tables for selection
    existing_tables = CSVUpload.objects.all().order_by('-uploaded_at')
    
    context = {
        'form': form,
        'csv_upload': csv_upload,
        'table_data': table_data,
        'columns': columns,
        'existing_tables': existing_tables,
    }
    
    return render(request, 'csv_upload/upload.html', context)


def process_csv_file(csv_file, table_name):
    """Process uploaded CSV file and store in database"""
    # Read CSV file using pandas
    content = csv_file.read().decode('utf-8')
    df = pd.read_csv(io.StringIO(content))
    
    # Clean column names (remove special characters, spaces)
    import re
    df.columns = [re.sub(r'[^a-zA-Z0-9_]', '_', col).lower().strip('_') for col in df.columns]
    
    # Create column information
    columns_info = {}
    for col in df.columns:
        # Determine data type
        if df[col].dtype == 'object':
            columns_info[col] = 'TEXT'
        elif df[col].dtype in ['int64', 'int32']:
            columns_info[col] = 'INTEGER'
        elif df[col].dtype in ['float64', 'float32']:
            columns_info[col] = 'REAL'
        else:
            columns_info[col] = 'TEXT'
    
    # Create CSVUpload record
    csv_upload = CSVUpload.objects.create(
        filename=csv_file.name,
        table_name=table_name,
    )
    csv_upload.set_columns(columns_info)
    csv_upload.save()
    
    # Store each row of data
    for index, row in df.iterrows():
        # Convert row to dictionary, handling NaN values
        row_dict = {}
        for col, value in row.items():
            if pd.isna(value):
                row_dict[col] = None
            else:
                row_dict[col] = str(value)
        
        CSVData.objects.create(
            csv_upload=csv_upload,
            row_number=index + 1,
            row_data=json.dumps(row_dict)
        )
    
    return csv_upload


def get_table_data(csv_upload):
    """Get table data for display"""
    data_rows = CSVData.objects.filter(csv_upload=csv_upload).order_by('row_number')
    table_data = []
    
    for data_row in data_rows:
        table_data.append(data_row.get_row_data())
    
    return table_data


def view_table(request, table_id):
    """View a specific table"""
    csv_upload = get_object_or_404(CSVUpload, id=table_id)
    table_data = get_table_data(csv_upload)
    columns = csv_upload.get_columns()
    
    context = {
        'csv_upload': csv_upload,
        'table_data': table_data,
        'columns': columns,
    }
    
    return render(request, 'csv_upload/view_table.html', context)


def delete_table(request, table_id):
    """Delete a table"""
    csv_upload = get_object_or_404(CSVUpload, id=table_id)
    
    if request.method == 'POST':
        table_name = csv_upload.table_name
        csv_upload.delete()
        messages.success(request, f'Table "{table_name}" deleted successfully.')
        return redirect('csv_upload:upload')
    
    return render(request, 'csv_upload/confirm_delete.html', {'csv_upload': csv_upload})
