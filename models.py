from models import API_ENDPOINTS

# Tables
API_ENDPOINTS = "api_endpoints"
HEALTH_RESULTS = "health_results"
HEALTH_STATE = "health_state"
NOTIFICATIONS = "notifications"

# Health state options
STATE_HEALTHY = "HEALTHY"
STATE_UNHEALTHY = "UNHEALTHY"
STATE_DEGRADED = "DEGRADED"

# Columns (optional, for clarity)
API_ID = "api_id"
STATUS_CODE = "status_code"
RESPONSE_TIME_MS = "response_time_ms"
SUCCESS = "success"
CONSECUTIVE_FAILURES = "consecutive_failures"
CURRENT_STATE = "current_state"
LAST_CHANGED_AT = "last_changed_at"
