# Changelog

All notable changes to the CSV-to-SQL Django application will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.5.0] - 2025-09-01

### Added
- **Column Properties Configuration System**: Complete database schema management interface
- **Database Schema Properties**: Configure nullable, primary key, foreign key, unique constraints, default values
- **Foreign Key Relationships**: Set up foreign key relationships with cascade options:
  - CASCADE - Delete related records
  - SET NULL - Set foreign key to null
  - RESTRICT - Prevent deletion
  - SET DEFAULT - Set to default value
  - NO ACTION - No action
- **Primary Key Management**: Configure primary keys with optional auto-increment for INTEGER fields
- **Data Type Selection**: Choose from TEXT, INTEGER, REAL, BOOLEAN, DATE, DATETIME, BLOB
- **Constraint Management**: 
  - Nullable/NOT NULL constraints
  - Unique constraints
  - Default value settings
  - Max length for TEXT fields
- **Column Configuration Interface**: Dedicated page for configuring each column's properties
- **Property Visualization**: Visual badges showing column properties (PK, FK, UNIQUE, NOT NULL, AUTO_INC, DEFAULT)
- **Smart Form Validation**: Intelligent field dependencies and constraint validation
- **Breadcrumb Navigation**: Enhanced navigation with breadcrumbs

### Changed
- **Column Data Structure**: Extended column metadata to include comprehensive database properties
- **Edit Table View**: Enhanced with detailed property display and Configure buttons
- **CSV Processing**: Updated to initialize columns with default property values
- **Model Methods**: Added new methods for column property management

### Technical Improvements
- **Enhanced Model**: Added `get_column_properties`, `set_column_properties`, `get_column_names` methods
- **New Form Class**: `ColumnPropertiesForm` with comprehensive validation and field dependencies
- **Interactive UI**: JavaScript-powered form with dynamic field showing/hiding
- **Property Management**: Complete CRUD operations for column properties
- **URL Structure**: New endpoint `/edit/<table_id>/column/<column_name>/`
- **Template System**: New `configure_column.html` template with modern responsive design

### User Experience
- **Interactive Forms**: Real-time field updates based on selections
- **Visual Feedback**: Property badges and status indicators
- **Contextual Help**: Tips and guidance in configuration interface
- **Mobile Responsive**: Optimized for all device sizes
- **Smart Validation**: Helpful error messages and constraint enforcement

## [0.4.0] - 2025-08-29

### Added
- **Case-Sensitive Table Names**: Table names now preserve exact case as entered by the user (e.g., "MyTable" stays "MyTable", not "mytable")
- **Table Rename Functionality**: Complete rename feature accessible through the new Edit Table view
- **Edit Table View**: Comprehensive table management interface with:
  - Table information display (name, file, upload date, record count, columns)
  - Rename form with validation
  - Column information table with data types
  - Quick access to view/edit table data
  - Delete table functionality
- **Enhanced Navigation**: Added Edit buttons throughout the application:
  - Edit buttons in existing tables list on upload page
  - Edit button in table view toolbar
  - Easy navigation between view, edit, and upload pages

### Changed
- **Form Validation**: Enhanced table name validation to preserve case while still sanitizing special characters
- **User Interface**: Improved layout and navigation with consistent Edit/View/Delete button patterns
- **Form Handling**: Better duplicate name checking during rename operations (excludes current table)

### Fixed
- **Case Preservation**: Removed automatic lowercasing of table names in form validation
- **Duplicate Name Prevention**: Enhanced validation prevents creating duplicate table names during rename
- **User Feedback**: Improved success and error messages for all table operations

### Technical Improvements
- Added `RenameTableForm` with current table exclusion logic
- Created `edit_table` view with proper POST handling
- Added `edit_table` URL pattern
- Created comprehensive `edit_table.html` template
- Enhanced form validation across all table operations
- Improved error handling and user feedback

## [0.3.0] - 2025-08-29

### Added
- **In-Place Table Editing**: Click-to-edit functionality for all table cells
- **Advanced Table Controls**: Modern toolbar with Save/Undo/Reload buttons  
- **Real-Time Filtering**: Live search across all table columns with instant results
- **Column Sorting**: Click column headers to sort ascending/descending with visual indicators
- **Advanced Pagination**: MudPager-inspired pagination component with:
  - Customizable page sizes (5, 10, 25, 50, 100 rows)
  - Direct page number input
  - First/Previous/Next/Last navigation buttons
  - Dynamic page count calculation
- **Visual Change Tracking**: Modified cells highlighted with change indicators
- **AJAX Updates**: Asynchronous cell updates without page refresh
- **User Feedback System**: Toast notifications and loading overlays
- **Enhanced UX**: Modern responsive design optimized for desktop and mobile

### Changed
- **Table View**: Complete redesign with professional interface
- **Navigation**: Enhanced pagination with intuitive controls
- **Performance**: Server-side pagination for large datasets
- **Responsiveness**: Improved mobile and tablet experience

### Technical Improvements
- **New API Endpoints**: 
  - `POST /api/table/<id>/update-cell/` - Update individual cells
  - `GET /api/table/<id>/reload/` - Reload table data with filters
- **Enhanced Views**: Advanced filtering, sorting, and pagination logic
- **JavaScript Framework**: Comprehensive client-side table management
- **Error Handling**: Robust error handling with user-friendly messages
- **Performance Optimization**: Efficient JSON field operations

### User Interface
- **Modern Design**: Professional toolbar and control layout
- **Visual Feedback**: Clear indicators for modified, loading, and error states
- **Accessibility**: Keyboard navigation and screen reader support
- **Mobile Responsive**: Optimized for all device sizes

### Developer Features
- **Modular JavaScript**: Well-organized client-side code
- **API Documentation**: Clear endpoint specifications
- **Version Tracking**: Comprehensive change documentation

---

## [0.2.0] - 2025-08-26

### Added
- **Firefox Browser Compatibility**: Comprehensive Firefox support with specific error handling
- **Custom Middleware**: `FirefoxCompatibilityMiddleware` for browser-specific functionality
- **JavaScript Error Suppression**: Handles Firefox form history, IndexedDB, and CORS errors
- **Enhanced Security Headers**: Firefox-optimized CSP and referrer policies
- **Browser Detection**: Automatic Firefox detection with tailored behavior
- **Improved User Experience**: Firefox-specific Bootstrap initialization and alert handling

### Changed
- **Templates**: Updated all HTML templates with Firefox-compatible meta tags
- **External Resources**: Added `crossorigin="anonymous"` to Bootstrap CDN links
- **Error Handling**: Enhanced JavaScript error management for external services
- **Table Scrolling**: Optimized table display behavior for Firefox
- **Form Interactions**: Added Firefox-specific confirmation dialogs

### Fixed
- Firefox console errors from form history system
- IndexedDB compatibility issues in Firefox
- CORS errors from external services (Sentry endpoints)
- Bootstrap functionality in Firefox environment
- Alert dismissal behavior in Firefox

### Technical Details
- **Files Modified**: 6 files updated/created
- **Browser Support**: Chrome, Firefox, Safari, Edge
- **Django Compatibility**: 5.2.x
- **Python Compatibility**: 3.8+

### Developer Notes
- Firefox-specific middleware handles User-Agent detection
- JavaScript error suppressions prevent console noise
- Security headers optimized for Firefox behavior
- Maintains backward compatibility with other browsers

---

## [0.1.0] - 2025-08-25

### Added
- **Initial Release**: Django web application for CSV to SQL conversion
- **Core Features**:
  - CSV file upload functionality
  - Automatic SQL table creation from CSV data
  - Data type detection and mapping
  - Table viewing and management
  - CRUD operations for uploaded tables
- **User Interface**: Bootstrap-styled responsive web interface
- **Data Processing**: Pandas integration for CSV parsing and analysis
- **Database**: SQLite backend with Django ORM

### Technical Implementation
- **Django Framework**: Version 5.2.x
- **Frontend**: Bootstrap 5.1.3 with responsive design
- **Backend**: Python with pandas for data processing
- **Database**: SQLite with automatic migrations
- **Architecture**: MVT (Model-View-Template) pattern

### Components Created
- **Models**: `CSVUpload`, `CSVData` for data persistence
- **Views**: Upload, view, delete functionality
- **Forms**: `CSVUploadForm` with validation
- **Templates**: Upload, view table, confirmation pages
- **Template Tags**: Custom filters for data display

### Browser Support
- **Primary**: Chrome, Safari, Edge
- **Status**: Firefox compatibility issues identified for future resolution

---

## Git Tags and Releases

### Tag Format
- **Release Tags**: `v0.3.0`, `v0.2.0`, `v0.1.0`
- **Pre-release Tags**: `v0.3.0-rc.1`, `v0.3.0-beta.1`
- **Development Tags**: `v0.3.0-dev.20250829`

### Release Process
1. **Feature Development**: Work in feature branches
2. **Version Update**: Update `version.py` with changes
3. **Changelog Update**: Document changes in `CHANGELOG.md`
4. **Testing**: Verify functionality across supported browsers
5. **Tagging**: Create git tag with semantic version
6. **Release**: Merge to main branch and deploy

### Branch Strategy
- **main**: Stable production releases
- **develop**: Integration branch for features
- **feature/***: Individual feature development
- **hotfix/***: Critical bug fixes for production

---

## Feature Comparison

| Feature | v0.1.0 | v0.2.0 | v0.3.0 |
|---------|--------|--------|--------|
| CSV Upload | ✅ | ✅ | ✅ |
| Table Viewing | ✅ | ✅ | ✅ |
| Firefox Support | ❌ | ✅ | ✅ |
| Cell Editing | ❌ | ❌ | ✅ |
| Table Filtering | ❌ | ❌ | ✅ |
| Column Sorting | ❌ | ❌ | ✅ |
| Advanced Pagination | ❌ | ❌ | ✅ |
| AJAX Updates | ❌ | ❌ | ✅ |
| Save/Undo | ❌ | ❌ | ✅ |
| Mobile Responsive | ⚠️ | ⚠️ | ✅ |

---

## Contributing

When contributing to this project:

1. **Update Version**: Modify `version.py` with new version and changes
2. **Document Changes**: Add entry to this `CHANGELOG.md`
3. **Test Compatibility**: Verify functionality in supported browsers
4. **Follow Format**: Use [Keep a Changelog](https://keepachangelog.com/) format

---

## Version Support

| Version | Status | Branch | Support Until |
|---------|--------|--------|---------------|
| 0.3.x   | Active | main   | Current       |
| 0.2.x   | Legacy | v0.2.x | 2025-12-31    |
| 0.1.x   | EOL    | v0.1.x | 2025-08-31    |

---

*This changelog is automatically maintained as part of the development process.*
