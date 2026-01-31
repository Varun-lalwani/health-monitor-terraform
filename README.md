- All database credentials are injected via environment variables
  to avoid secrets in code.
- The service connects to PostgreSQL using psycopg2.
- DB helper functions include:
  • get_apis_to_check()
  • insert_health_result()
  • get_health_state()
  • update_health_state()

Health checks are executed via a Python service that sends HTTP requests
with configurable timeouts. API health is determined using expected status
codes and failure thresholds to avoid false positives. Database credentials
are injected via environment variables to prevent hardcoded secrets.

Notifications are triggered only when an API’s health state changes. Alerts are logged to the console and inserted into the notifications table for audit purposes, ensuring no alert spam.

Logging is implemented to track all health checks (INFO) and failures (ERROR). Any single API failure does not crash the scheduler, ensuring continuous monitoring and operational reliability.

I first built the application locally with proper separation of concerns and environment-based configuration. Once stable, I used Terraform to provision AWS infrastructure (EC2 + RDS) and deploy the same application without changing core logic.


## Logging
Logs are managed via systemd/journald.

View logs:
journalctl -u health-monitor -f

Log rotation is handled automatically by journald.
