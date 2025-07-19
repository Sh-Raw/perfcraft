from locust import HttpUser, task, between
from utils.helpers import load_test_config

class LoginUser(HttpUser):
    config = load_test_config("configs/test.yaml")

    host = config.get("host")  # dynamically set base host
    wait_time = between(1, 3)

    @task
    def login(self):
        endpoint = self.config.get("endpoint", "/post")
        method = self.config.get("method", "POST").upper()
        payload = self.config.get("payload", {})

        if method == "POST":
            with self.client.post(endpoint, json=payload, catch_response=True) as response:
                if response.status_code == 200:
                    response.success()
                else:
                    response.failure(f"Unexpected status code: {response.status_code}")
