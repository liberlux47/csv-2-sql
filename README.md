# CSV to SQL Table Converter

A Django web application that allows users to upload CSV files and converts them into SQL tables with a web interface for viewing the data.

## Features

- 📁 **CSV File Upload**: Simple drag-and-drop or file selection interface
- 🗂️ **Dynamic Table Creation**: Automatically creates SQL tables from CSV structure
- 📊 **Data Display**: View uploaded data in a responsive HTML table format
- 🏷️ **Custom Table Names**: Name your tables for easy organization
- 🗑️ **Table Management**: Delete tables when no longer needed
- 📱 **Responsive Design**: Works on desktop and mobile devices

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd csv-to-sql
   ```

2. **Create and activate virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install django pandas
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

## Usage

1. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

2. **Access the application**:
   Open your browser and navigate to `http://127.0.0.1:8000`

3. **Upload CSV files**:
   - Select a CSV file using the file input
   - Enter a unique name for your table
   - Click "Upload & Process"
   - View the generated table below

## Project Structure

```
csv-to-sql/
├── .venv/                  # Virtual environment
├── csv_upload/             # Main Django app
│   ├── migrations/         # Database migrations
│   ├── templates/          # HTML templates
│   ├── templatetags/       # Custom template filters
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── forms.py           # Django forms
│   └── urls.py            # URL routing
├── csvtosql/              # Django project settings
│   ├── settings.py        # Project configuration
│   ├── urls.py           # Main URL routing
│   └── wsgi.py           # WSGI configuration
├── manage.py              # Django management script
└── README.md             # This file
```

## How It Works

1. **CSV Upload**: Users upload CSV files through a web form
2. **Data Processing**: Pandas library processes the CSV and determines data types
3. **Database Storage**: Data is stored in Django models (CSVUpload for metadata, CSVData for rows)
4. **Table Display**: Data is retrieved and displayed in responsive HTML tables
5. **Table Management**: Users can view, manage, and delete created tables

## Technical Details

- **Backend**: Django 5.2.5
- **Data Processing**: Pandas for CSV parsing and data type inference
- **Database**: SQLite (default Django database)
- **Frontend**: Bootstrap 5.1.3 for responsive design
- **File Handling**: Django forms with file upload validation

## Data Types Supported

- **TEXT**: String data and mixed types
- **INTEGER**: Whole numbers
- **REAL**: Decimal numbers

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the MIT License.
