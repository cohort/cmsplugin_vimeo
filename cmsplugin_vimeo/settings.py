"""
Convenience module for access of custom youtube application settings,
which enforces default settings when the main settings module does not
contain the appropriate settings.
"""
from django.conf import settings

# Autoplay
CMS_VIMEO_DEFAULT_AUTOPLAY = getattr(settings, 'CMS_VIMEO_DEFAULT_AUTOPLAY', False)

# Border
CMS_VIMEO_DEFAULT_BORDER = getattr(settings, 'CMS_VIMEO_DEFAULT_BORDER', False)

# Loop
CMS_VIMEO_DEFAULT_LOOP = getattr(settings, 'CMS_VIMEO_DEFAULT_LOOP', False)
