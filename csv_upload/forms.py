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


class ColumnPropertiesForm(forms.Form):
    """Form for configuring column properties"""
    
    DATA_TYPE_CHOICES = [
        ('TEXT', 'Text (VARCHAR)'),
        ('INTEGER', 'Integer'),
        ('REAL', 'Real (Float)'),
        ('BOOLEAN', 'Boolean'),
        ('DATE', 'Date'),
        ('DATETIME', 'DateTime'),
        ('BLOB', 'Binary Data'),
    ]
    
    ON_DELETE_CHOICES = [
        ('CASCADE', 'CASCADE - Delete related records'),
        ('SET NULL', 'SET NULL - Set foreign key to null'),
        ('RESTRICT', 'RESTRICT - Prevent deletion'),
        ('SET DEFAULT', 'SET DEFAULT - Set to default value'),
        ('NO ACTION', 'NO ACTION - No action'),
    ]
    
    data_type = forms.ChoiceField(
        choices=DATA_TYPE_CHOICES,
        label='Data Type',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    nullable = forms.BooleanField(
        label='Allow NULL values',
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    
    primary_key = forms.BooleanField(
        label='Primary Key',
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    
    unique = forms.BooleanField(
        label='Unique Constraint',
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    
    auto_increment = forms.BooleanField(
        label='Auto Increment',
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        help_text='Only applicable for INTEGER primary keys'
    )
    
    default_value = forms.CharField(
        label='Default Value',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter default value (optional)'
        }),
        help_text='Leave empty for no default value'
    )
    
    max_length = forms.IntegerField(
        label='Max Length',
        required=False,
        min_value=1,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g., 255'
        }),
        help_text='Only applicable for TEXT fields'
    )
    
    # Foreign Key fields
    is_foreign_key = forms.BooleanField(
        label='Is Foreign Key',
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    
    foreign_table = forms.CharField(
        label='Referenced Table',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter table name'
        }),
        help_text='Name of the table this foreign key references'
    )
    
    foreign_column = forms.CharField(
        label='Referenced Column',
        required=False,
        initial='id',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter column name'
        }),
        help_text='Column in the referenced table (usually "id")'
    )
    
    on_delete = forms.ChoiceField(
        choices=ON_DELETE_CHOICES,
        label='On Delete Action',
        required=False,
        initial='CASCADE',
        widget=forms.Select(attrs={'class': 'form-select'}),
        help_text='What happens when the referenced record is deleted'
    )
    
    def __init__(self, *args, column_name=None, existing_properties=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.column_name = column_name
        
        # Pre-populate form with existing properties if provided
        if existing_properties:
            for field_name, value in existing_properties.items():
                if field_name in self.fields and value is not None:
                    self.fields[field_name].initial = value
    
    def clean(self):
        cleaned_data = super().clean()
        
        # Validation rules
        primary_key = cleaned_data.get('primary_key')
        nullable = cleaned_data.get('nullable')
        auto_increment = cleaned_data.get('auto_increment')
        data_type = cleaned_data.get('data_type')
        is_foreign_key = cleaned_data.get('is_foreign_key')
        foreign_table = cleaned_data.get('foreign_table')
        foreign_column = cleaned_data.get('foreign_column')
        max_length = cleaned_data.get('max_length')
        
        # Primary keys cannot be nullable
        if primary_key and nullable:
            self.add_error('nullable', 'Primary key columns cannot be nullable')
        
        # Auto increment only for INTEGER primary keys
        if auto_increment and data_type != 'INTEGER':
            self.add_error('auto_increment', 'Auto increment is only valid for INTEGER fields')
        
        if auto_increment and not primary_key:
            self.add_error('auto_increment', 'Auto increment is only valid for primary key fields')
        
        # Foreign key validation
        if is_foreign_key:
            if not foreign_table:
                self.add_error('foreign_table', 'Referenced table is required for foreign keys')
            if not foreign_column:
                self.add_error('foreign_column', 'Referenced column is required for foreign keys')
        
        # Max length only for TEXT fields
        if max_length and data_type != 'TEXT':
            self.add_error('max_length', 'Max length is only applicable for TEXT fields')
        
        return cleaned_data
    
    def get_column_properties(self):
        """Return the column properties as a dictionary"""
        if not self.is_valid():
            return None
        
        properties = {
            'data_type': self.cleaned_data['data_type'],
            'nullable': self.cleaned_data['nullable'],
            'primary_key': self.cleaned_data['primary_key'],
            'unique': self.cleaned_data['unique'],
            'auto_increment': self.cleaned_data['auto_increment'],
            'default_value': self.cleaned_data['default_value'] or None,
            'max_length': self.cleaned_data['max_length'],
        }
        
        # Add foreign key properties if applicable
        if self.cleaned_data['is_foreign_key']:
            properties.update({
                'foreign_key': True,
                'foreign_table': self.cleaned_data['foreign_table'],
                'foreign_column': self.cleaned_data['foreign_column'],
                'on_delete': self.cleaned_data['on_delete'],
            })
        else:
            properties.update({
                'foreign_key': False,
                'foreign_table': None,
                'foreign_column': None,
                'on_delete': None,
            })
        
        return properties
