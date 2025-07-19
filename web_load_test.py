from locust import HttpUser, task, between
from utils.helpers import load_test_config

class ConfigurableUser(HttpUser):
    config = load_test_config()

    wait_time = between(1, 3)
    host = config.get("host")

    @task
    def run_custom_test(self):
        method = self.config.get("method", "GET").upper()
        endpoint = self.config.get("endpoint", "/")
        payload = self.config.get("payload", {})

        if method == "GET":
            self.client.get(endpoint)
        elif method == "POST":
            self.client.post(endpoint, json=payload)
