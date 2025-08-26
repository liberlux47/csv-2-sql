from django import forms


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
        """Validate table name"""
        table_name = self.cleaned_data['table_name']
        
        # Remove special characters and spaces, replace with underscores
        import re
        table_name = re.sub(r'[^a-zA-Z0-9_]', '_', table_name)
        
        # Ensure it starts with a letter
        if not table_name[0].isalpha():
            table_name = 'table_' + table_name
        
        return table_name.lower()
