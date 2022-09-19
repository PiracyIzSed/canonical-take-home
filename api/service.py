from app import get_application
from app.core.config import get_app_settings

settings = get_app_settings()
application = get_application(settings)