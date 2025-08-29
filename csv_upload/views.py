from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
import pandas as pd
import json
import io
import re

# Absolute imports to avoid IDE issues
from csv_upload.models import CSVUpload, CSVData
from csv_upload.forms import CSVUploadForm


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
    """View a specific table with enhanced features"""
    csv_upload = get_object_or_404(CSVUpload, id=table_id)
    
    # Get filter and sorting parameters
    filter_text = request.GET.get('filter', '')
    sort_by = request.GET.get('sort', 'row_number')
    sort_order = request.GET.get('order', 'asc')
    page_size = int(request.GET.get('page_size', 10))
    page_number = request.GET.get('page', 1)
    
    # Get base queryset
    data_rows = CSVData.objects.filter(csv_upload=csv_upload)
    
    # Apply filtering
    if filter_text:
        # Filter across all row data (JSON search)
        data_rows = data_rows.filter(row_data__icontains=filter_text)
    
    # Apply sorting
    if sort_by != 'row_number':
        # For JSON field sorting, we'll sort in Python after fetching
        # This is not optimal for large datasets but works for our use case
        all_rows = list(data_rows)
        columns = csv_upload.get_columns()
        
        if sort_by in columns:
            try:
                all_rows.sort(
                    key=lambda x: json.loads(x.row_data).get(sort_by, ''),
                    reverse=(sort_order == 'desc')
                )
                # Create a custom queryset-like list for pagination
                data_rows = all_rows
            except:
                # Fallback to row_number sorting
                data_rows = data_rows.order_by('row_number')
        else:
            data_rows = data_rows.order_by('row_number')
    else:
        order_by = 'row_number' if sort_order == 'asc' else '-row_number'
        data_rows = data_rows.order_by(order_by)
    
    # Pagination
    if isinstance(data_rows, list):
        # For sorted data, implement manual pagination
        total_rows = len(data_rows)
        start_idx = (int(page_number) - 1) * page_size
        end_idx = start_idx + page_size
        paginated_rows = data_rows[start_idx:end_idx]
        
        # Create a mock paginator object for template consistency
        class MockPaginator:
            def __init__(self, object_list, per_page, total):
                self.object_list = object_list
                self.per_page = per_page
                self.count = total
                self.num_pages = (total + per_page - 1) // per_page
        
        class MockPage:
            def __init__(self, object_list, number, paginator):
                self.object_list = object_list
                self.number = int(number)
                self.paginator = paginator
                
            def has_previous(self):
                return self.number > 1
                
            def has_next(self):
                return self.number < self.paginator.num_pages
                
            def previous_page_number(self):
                return self.number - 1 if self.has_previous() else None
                
            def next_page_number(self):
                return self.number + 1 if self.has_next() else None
        
        paginator = MockPaginator(data_rows, page_size, total_rows)
        page_obj = MockPage(paginated_rows, page_number, paginator)
    else:
        # Use Django's built-in paginator
        paginator = Paginator(data_rows, page_size)
        page_obj = paginator.get_page(page_number)
    
    # Convert paginated data to table format
    table_data = []
    for data_row in page_obj.object_list:
        if hasattr(data_row, 'get_row_data'):
            table_data.append({
                'id': data_row.id,
                'row_number': data_row.row_number,
                'data': data_row.get_row_data()
            })
        else:
            # Handle case where data_row might be from sorted list
            table_data.append({
                'id': data_row.id,
                'row_number': data_row.row_number,
                'data': data_row.get_row_data()
            })
    
    columns = csv_upload.get_columns()
    
    # Available page size options
    page_size_options = [5, 10, 25, 50, 100]
    
    context = {
        'csv_upload': csv_upload,
        'table_data': table_data,
        'columns': columns,
        'page_obj': page_obj,
        'paginator': page_obj.paginator,
        'filter_text': filter_text,
        'sort_by': sort_by,
        'sort_order': sort_order,
        'page_size': page_size,
        'page_size_options': page_size_options,
        'total_records': page_obj.paginator.count,
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


def update_cell(request, table_id):
    """API endpoint to update a single cell value"""
    if request.method == 'POST':
        try:
            csv_upload = get_object_or_404(CSVUpload, id=table_id)
            data = json.loads(request.body)
            
            row_id = data.get('row_id')
            column = data.get('column')
            new_value = data.get('value')
            
            # Get the specific row
            csv_data = get_object_or_404(CSVData, id=row_id, csv_upload=csv_upload)
            
            # Update the specific column in the row data
            row_data = csv_data.get_row_data()
            row_data[column] = new_value
            csv_data.set_row_data(row_data)
            csv_data.save()
            
            return JsonResponse({
                'success': True,
                'message': f'Cell updated successfully',
                'row_id': row_id,
                'column': column,
                'new_value': new_value
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'Error updating cell: {str(e)}'
            }, status=400)
    
    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)


def reload_table_data(request, table_id):
    """API endpoint to reload table data with filters and pagination"""
    csv_upload = get_object_or_404(CSVUpload, id=table_id)
    
    # Get parameters
    filter_text = request.GET.get('filter', '')
    sort_by = request.GET.get('sort', 'row_number')
    sort_order = request.GET.get('order', 'asc')
    page_size = int(request.GET.get('page_size', 10))
    page_number = int(request.GET.get('page', 1))
    
    # Get filtered and sorted data (reuse logic from view_table)
    data_rows = CSVData.objects.filter(csv_upload=csv_upload)
    
    if filter_text:
        data_rows = data_rows.filter(row_data__icontains=filter_text)
    
    # Apply sorting
    if sort_by != 'row_number':
        all_rows = list(data_rows)
        columns = csv_upload.get_columns()
        
        if sort_by in columns:
            try:
                all_rows.sort(
                    key=lambda x: json.loads(x.row_data).get(sort_by, ''),
                    reverse=(sort_order == 'desc')
                )
                data_rows = all_rows
            except:
                data_rows = data_rows.order_by('row_number')
        else:
            data_rows = data_rows.order_by('row_number')
    else:
        order_by = 'row_number' if sort_order == 'asc' else '-row_number'
        data_rows = data_rows.order_by(order_by)
    
    # Pagination
    if isinstance(data_rows, list):
        total_rows = len(data_rows)
        start_idx = (page_number - 1) * page_size
        end_idx = start_idx + page_size
        paginated_rows = data_rows[start_idx:end_idx]
        total_pages = (total_rows + page_size - 1) // page_size
    else:
        paginator = Paginator(data_rows, page_size)
        page_obj = paginator.get_page(page_number)
        paginated_rows = page_obj.object_list
        total_rows = paginator.count
        total_pages = paginator.num_pages
    
    # Convert to table format
    table_data = []
    for data_row in paginated_rows:
        table_data.append({
            'id': data_row.id,
            'row_number': data_row.row_number,
            'data': data_row.get_row_data()
        })
    
    return JsonResponse({
        'success': True,
        'table_data': table_data,
        'total_records': total_rows,
        'total_pages': total_pages,
        'current_page': page_number,
        'page_size': page_size
    })
