import time
from db import get_apis_to_check
from checker import check_api


def main():
    print("🚀 API Health Monitor Scheduler started...")

    while True:
        apis = get_apis_to_check()

        for api in apis:
            check_api(api)

        # Sleep for the smallest interval (can be adjusted)
        time.sleep(30)  # Fast-track: checks every 30 seconds

if __name__ == "__main__":
    main()
# In production, this scheduler loop can be replaced with distributed schedulers,
# containerized tasks (ECS/Fargate), or Kubernetes CronJobs for scalability and reliability.
