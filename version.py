# Version file for csv-to-sql project
__version__ = "0.3.0"
__build__ = "2025.08.29.001"
__release_date__ = "2025-08-29"

# Version history and changes
VERSION_HISTORY = {
    "0.3.0": {
        "release_date": "2025-08-29",
        "branch": "master", 
        "changes": [
            "Added comprehensive in-place table cell editing functionality",
            "Implemented advanced table filtering with real-time search",
            "Added column sorting with ascending/descending order toggle",
            "Created sophisticated pagination system with MudPager-like features",
            "Added Save/Undo functionality for table modifications",
            "Implemented reload table data capability",
            "Enhanced user interface with modern toolbar and controls",
            "Added visual feedback for modified cells and pending changes",
            "Implemented AJAX-based cell updates without page refresh", 
            "Added loading overlays and toast notifications for better UX",
            "Enhanced pagination with first/last/prev/next navigation",
            "Added dynamic page size selection (5, 10, 25, 50, 100 rows)",
            "Implemented page number input for direct navigation",
            "Added comprehensive error handling and user feedback",
            "Enhanced responsive design for mobile and desktop"
        ],
        "features_added": [
            "In-place cell editing with click-to-edit interface",
            "Real-time table filtering across all columns",
            "Multi-column sorting with visual indicators",
            "Advanced pagination with customizable page sizes",
            "Save/Undo system for table modifications",
            "AJAX table reload without losing user context",
            "Modern toolbar with intuitive controls",
            "Visual change tracking with highlighting",
            "Toast notifications for user feedback",
            "Loading states and progress indicators"
        ],
        "files_modified": [
            "csv_upload/views.py (enhanced with pagination, filtering, sorting)",
            "csv_upload/urls.py (added API endpoints)",
            "csv_upload/templates/csv_upload/view_table.html (complete redesign)",
            "version.py"
        ],
        "api_endpoints": [
            "POST /api/table/<id>/update-cell/ - Update individual table cells",
            "GET /api/table/<id>/reload/ - Reload table data with filters"
        ],
        "compatibility": {
            "browsers": ["Chrome", "Firefox", "Safari", "Edge"],
            "django": "5.2.x",
            "python": "3.8+",
            "responsive": "Mobile and Desktop optimized"
        },
        "performance": {
            "pagination": "Server-side pagination for large datasets",
            "filtering": "Efficient JSON field filtering",
            "sorting": "Optimized column sorting with caching",
            "ajax": "Asynchronous updates without page reloads"
        }
    },
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
