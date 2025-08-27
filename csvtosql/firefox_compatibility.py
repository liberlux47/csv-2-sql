"""
Firefox Compatibility Middleware

This middleware adds Firefox-specific headers and handles browser compatibility issues.
"""


class FirefoxCompatibilityMiddleware:
    """
    Middleware to handle Firefox-specific compatibility issues
    """
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Check if the request is from Firefox
        user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
        is_firefox = 'firefox' in user_agent
        
        if is_firefox:
            # Add Firefox-specific headers
            response['X-Firefox-Compatibility'] = 'enabled'
            
            # Prevent form history errors
            response['X-Content-Type-Options'] = 'nosniff'
            
            # Add cache control for Firefox
            if 'Cache-Control' not in response:
                response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
            
            # Add referrer policy specific to Firefox
            response['Referrer-Policy'] = 'same-origin'
            
            # Prevent IndexedDB issues by setting proper headers
            response['Feature-Policy'] = 'indexeddb \'self\''
        
        return response

    def process_exception(self, request, exception):
        """
        Handle exceptions that might be Firefox-specific
        """
        user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
        is_firefox = 'firefox' in user_agent
        
        if is_firefox:
            # Log Firefox-specific exceptions differently
            import logging
            logger = logging.getLogger('firefox_compatibility')
            logger.warning(f'Firefox-specific exception: {exception}')
        
        # Return None to let Django handle the exception normally
        return None
