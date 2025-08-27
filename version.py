# Version file for csv-to-sql project
__version__ = "0.2.0"
__build__ = "2025.08.26.001"
__release_date__ = "2025-08-26"

# Version history and changes
VERSION_HISTORY = {
    "0.2.0": {
        "release_date": "2025-08-26",
        "branch": "feature/table-configuration", 
        "changes": [
            "Added comprehensive Firefox browser compatibility fixes",
            "Implemented Firefox-specific error handling for form history issues",
            "Added IndexedDB error suppression for Firefox",
            "Created custom FirefoxCompatibilityMiddleware for browser-specific handling",
            "Enhanced templates with Firefox-compatible meta tags and CORS headers",
            "Added JavaScript error suppression for external service CORS issues",
            "Implemented Firefox-specific Bootstrap initialization and alert handling",
            "Added security headers optimized for Firefox (CSP, referrer policy)",
            "Enhanced table scrolling behavior for Firefox compatibility",
            "Added confirmation dialogs for critical actions in Firefox"
        ],
        "files_modified": [
            "csv_upload/templates/csv_upload/upload.html",
            "csv_upload/templates/csv_upload/view_table.html", 
            "csv_upload/templates/csv_upload/confirm_delete.html",
            "csvtosql/settings.py",
            "csvtosql/firefox_compatibility.py (new file)",
            "version.py"
        ],
        "compatibility": {
            "browsers": ["Chrome", "Firefox", "Safari", "Edge"],
            "django": "5.2.x",
            "python": "3.8+"
        }
    },
    "0.1.0": {
        "release_date": "2025-08-25",
        "branch": "main",
        "changes": [
            "Initial Django project setup",
            "Basic CSV upload functionality", 
            "SQL table creation and viewing",
            "Bootstrap UI implementation",
            "CRUD operations for CSV tables"
        ],
        "files_created": [
            "Django project scaffolding",
            "CSV upload models, views, forms",
            "HTML templates with Bootstrap styling",
            "Template filters for data display"
        ],
        "compatibility": {
            "browsers": ["Chrome", "Safari", "Edge"],
            "django": "5.2.x", 
            "python": "3.8+"
        }
    }
}
