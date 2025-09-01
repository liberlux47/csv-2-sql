from django.db import models
import json


class CSVUpload(models.Model):
    """Model to store CSV upload metadata"""
    filename = models.CharField(max_length=255)
    table_name = models.CharField(max_length=100, unique=True)
    columns = models.TextField()  # JSON string of column names and types with properties
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def get_columns(self):
        """Return columns as a Python object"""
        return json.loads(self.columns)
    
    def set_columns(self, columns_dict):
        """Set columns from a Python object"""
        self.columns = json.dumps(columns_dict)
    
    def get_column_names(self):
        """Return just the column names as a list"""
        columns = self.get_columns()
        if isinstance(list(columns.values())[0], dict):
            # New format with properties
            return list(columns.keys())
        else:
            # Old format - just data types
            return list(columns.keys())
    
    def get_column_properties(self, column_name):
        """Get properties for a specific column"""
        columns = self.get_columns()
        column_data = columns.get(column_name, {})
        
        if isinstance(column_data, str):
            # Old format - convert to new format
            return {
                'data_type': column_data,
                'nullable': True,
                'primary_key': False,
                'foreign_key': None,
                'foreign_table': None,
                'on_delete': 'CASCADE',
                'unique': False,
                'default_value': None,
                'max_length': None,
                'auto_increment': False
            }
        else:
            # New format with properties
            return column_data
    
    def set_column_properties(self, column_name, properties):
        """Set properties for a specific column"""
        columns = self.get_columns()
        columns[column_name] = properties
        self.set_columns(columns)
    
    def __str__(self):
        return f"{self.filename} -> {self.table_name}"


class CSVData(models.Model):
    """Model to store CSV data rows"""
    csv_upload = models.ForeignKey(CSVUpload, on_delete=models.CASCADE, related_name='data_rows')
    row_data = models.TextField()  # JSON string of row data
    row_number = models.IntegerField()
    
    def get_row_data(self):
        """Return row data as a Python object"""
        return json.loads(self.row_data)
    
    def set_row_data(self, row_dict):
        """Set row data from a Python object"""
        self.row_data = json.dumps(row_dict)
    
    class Meta:
        ordering = ['row_number']
    
    def __str__(self):
        return f"Row {self.row_number} of {self.csv_upload.table_name}"
