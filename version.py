# Version file for csv-to-sql project
__version__ = "0.6.0"
__build__ = "2025.09.01.002"
__release_date__ = "2025-09-01"

# Version history and changes
VERSION_HISTORY = {
    "0.6.0": {
        "release_date": "2025-09-01",
        "branch": "master",
        "changes": [
            "Migrated database backend from SQLite to PostgreSQL",
            "Added PostgreSQL adapter (psycopg2-binary) as dependency",
            "Updated Django database settings for PostgreSQL connection",
            "Created PostgreSQL database and user with proper permissions",
            "Successfully migrated all Django models to PostgreSQL",
            "Maintained all existing functionality with improved scalability",
            "Enhanced performance and concurrent access capabilities",
            "Added production-ready database configuration"
        ],
        "features_added": [
            "PostgreSQL database backend support",
            "Production-ready database configuration",
            "Enhanced concurrent access capabilities",
            "Improved data integrity and ACID compliance",
            "Better performance for large datasets",
            "Advanced indexing and query optimization",
            "Backup and recovery capabilities",
            "Multi-user concurrent editing support"
        ],
        "technical_improvements": [
            "Replaced SQLite with PostgreSQL 16",
            "Added psycopg2-binary dependency to pyproject.toml",
            "Updated DATABASES configuration in settings.py",
            "Created dedicated PostgreSQL database 'csv2sql'",
            "Created dedicated database user 'csv2sql_user'",
            "Applied all Django migrations to PostgreSQL",
            "Verified database connection and table creation",
            "Maintained backward compatibility with existing models"
        ],
        "infrastructure": [
            "PostgreSQL 16.9 server installation and configuration",
            "Database user with restricted permissions for security",
            "UTF-8 encoding and UTC timezone configuration",
            "Proper schema permissions and access controls",
            "Development and production database separation capability",
            "Enhanced backup and disaster recovery options"
        ]
    },
    "0.5.0": {
        "release_date": "2025-09-01",
        "branch": "master",
        "changes": [
            "Added comprehensive column properties configuration system",
            "Implemented database schema properties (nullable, primary key, foreign key, etc.)",
            "Created advanced column configuration interface with validation",
            "Added support for foreign key relationships with cascade options",
            "Enhanced column information display with property badges",
            "Implemented auto-increment support for INTEGER primary keys",
            "Added unique constraints and default value settings",
            "Created comprehensive column configuration form with field dependencies",
            "Enhanced model structure to support rich column metadata",
            "Added breadcrumb navigation for better user experience"
        ],
        "features_added": [
            "Column Properties Configuration: Complete database schema setup",
            "Primary Key Configuration: Set primary keys with auto-increment",
            "Foreign Key Relationships: Configure foreign keys with cascade options",
            "Constraint Management: Nullable, unique, and default value settings",
            "Data Type Selection: Choose from TEXT, INTEGER, REAL, BOOLEAN, DATE, DATETIME, BLOB",
            "Advanced Form Validation: Smart field dependencies and constraint validation",
            "Property Badges: Visual indicators for column properties (PK, FK, UNIQUE, NOT NULL)",
            "Column Configuration UI: Dedicated interface for each column",
            "Cascade Options: SET NULL, CASCADE, RESTRICT, SET DEFAULT, NO ACTION",
            "Max Length Settings: Configurable length for TEXT fields"
        ],
        "technical_improvements": [
            "Extended CSVUpload model with column property methods",
            "Created ColumnPropertiesForm with comprehensive validation",
            "Added configure_column view with property management",
            "Built configure_column.html template with interactive UI",
            "Enhanced edit_table.html to show column properties",
            "Updated CSV processing to use new column format",
            "Added JavaScript for dynamic form field management",
            "Implemented breadcrumb navigation system",
            "Added property badge display system",
            "Enhanced URL patterns for column configuration"
        ],
        "user_experience": [
            "Interactive column configuration with real-time field updates",
            "Visual property indicators in column lists",
            "Smart form validation with helpful error messages",
            "Breadcrumb navigation for easy navigation",
            "Contextual help and tips in configuration forms",
            "Property preview in configuration sidebar",
            "Responsive design for mobile and desktop",
            "Intuitive checkbox and select controls"
        ]
    },
    "0.4.0": {
        "release_date": "2025-08-29",
        "branch": "master",
        "changes": [
            "Fixed case sensitivity for table names - now preserves exact case as entered by user",
            "Added table rename functionality in Edit view",
            "Created comprehensive Edit Table view with table information display",
            "Added Edit buttons throughout the application for better navigation",
            "Enhanced form validation to prevent duplicate table names during rename",
            "Improved user interface with dedicated edit/rename forms",
            "Added table information display including record count and column details",
            "Enhanced navigation with Edit table buttons in view and upload pages"
        ],
        "features_added": [
            "Case-sensitive table name preservation",
            "Table rename functionality with validation",
            "Edit Table view with comprehensive table information",
            "Rename form with duplicate name checking",
            "Enhanced navigation with Edit buttons",
            "Table statistics display (record count, column count)",
            "Column information display with data types",
            "Improved form validation for rename operations"
        ],
        "technical_improvements": [
            "Removed .lower() transformation from table name validation",
            "Added RenameTableForm with current table exclusion logic",
            "Created edit_table view with POST handling for renames",
            "Added edit_table URL pattern",
            "Created edit_table.html template with modern UI",
            "Updated navigation buttons across all templates",
            "Enhanced form validation with duplicate checking",
            "Improved user feedback for rename operations"
        ],
        "fixes": [
            "Table names now preserve exact case (MyTable stays as MyTable, not mytable)",
            "Form validation prevents duplicate table names during rename",
            "Enhanced error handling for rename operations",
            "Improved user feedback and success messages"
        ]
    },
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
