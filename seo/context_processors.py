# ----------------------------------------------------------------------------
# Stdlib imports
# ----------------------------------------------------------------------------
from __future__ import absolute_import, unicode_literals


# ============================================================================

# ----------------------------------------------------------------------------
# Core Django imports
# ----------------------------------------------------------------------------

from django.conf import settings


# ============================================================================


# ----------------------------------------------------------------------------
# Third-party app imports
# ----------------------------------------------------------------------------


# ============================================================================


# ----------------------------------------------------------------------------
# Imports from our apps
# ----------------------------------------------------------------------------




# ============================================================================


def seo(request):
    """
    Adds cicanon blog name context variables to the context.

    """
    
    return {

        # 'CICANON': settings.CICANON,
        # 'DISQUS_SITE_NAME':settings.DISQUS_SITE_NAME,        
        # 'BLOG_NAME': settings.SITE_NAME,
        'SITE_DESCRIPTION':settings.SITE_DESCRIPTION,
        'SITE_NAME':settings.SITE_NAME,
        'SITE_SLOGAN':settings.SITE_SLOGAN,
    }
