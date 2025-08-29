from django import forms
from .models import CSVUpload


class CSVUploadForm(forms.Form):
    """Form for uploading CSV files"""
    csv_file = forms.FileField(
        label='Select CSV File',
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': '.csv'
        })
    )
    table_name = forms.CharField(
        max_length=100,
        label='Table Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter a name for your table'
        }),
        help_text='Enter a unique name for the SQL table'
    )
    
    def clean_csv_file(self):
        """Validate that the uploaded file is a CSV"""
        file = self.cleaned_data['csv_file']
        
        if not file.name.endswith('.csv'):
            raise forms.ValidationError('Please upload a CSV file.')
        
        return file
    
    def clean_table_name(self):
        """Validate table name - preserve exact case as entered by user"""
        table_name = self.cleaned_data['table_name']
        
        # Remove special characters and spaces, replace with underscores
        import re
        table_name = re.sub(r'[^a-zA-Z0-9_]', '_', table_name)
        
        # Ensure it starts with a letter
        if not table_name[0].isalpha():
            table_name = 'table_' + table_name
        
        # Return with exact case preserved
        return table_name


class RenameTableForm(forms.Form):
    """Form for renaming tables"""
    new_table_name = forms.CharField(
        max_length=100,
        label='New Table Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter new table name'
        }),
        help_text='Enter a new unique name for the table'
    )
    
    def __init__(self, *args, current_table_id=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.current_table_id = current_table_id
    
    def clean_new_table_name(self):
        """Validate new table name - preserve exact case as entered by user"""
        table_name = self.cleaned_data['new_table_name']
        
        # Remove special characters and spaces, replace with underscores
        import re
        table_name = re.sub(r'[^a-zA-Z0-9_]', '_', table_name)
        
        # Ensure it starts with a letter
        if not table_name[0].isalpha():
            table_name = 'table_' + table_name
        
        # Check if the new name already exists (excluding current table)
        existing_query = CSVUpload.objects.filter(table_name=table_name)
        if self.current_table_id:
            existing_query = existing_query.exclude(id=self.current_table_id)
        
        if existing_query.exists():
            raise forms.ValidationError(f'Table name "{table_name}" already exists. Please choose a different name.')
        
        # Return with exact case preserved
        return table_name
