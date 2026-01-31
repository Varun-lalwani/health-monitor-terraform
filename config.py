import os

# -----------------------------
# Database credentials
# -----------------------------
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", 5432))
DB_NAME = os.getenv("DB_NAME", "api_health_monitor")
DB_USER = os.getenv("DB_USER", "api_monitor")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")

# -----------------------------
# Global settings
# -----------------------------
# How often the main loop runs (seconds)
GLOBAL_CHECK_INTERVAL = int(os.getenv("GLOBAL_CHECK_INTERVAL", 10))

# Default timeout for API requests
DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", 5))
