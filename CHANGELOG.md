# Changelog

All notable changes to the CSV-to-SQL Django application will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
