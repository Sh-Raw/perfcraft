from locust import HttpUser, task, between
from utils.helpers import load_test_config

class UserFlow(HttpUser):
    config = load_test_config("configs/test.yaml")
    host = config["host"]
    headers = config.get("headers", {})
    wait_time = between(1, 2)

    def on_start(self):
        self.token = None

    @task(1)
    def full_user_journey(self):
        # Register
        reg = self.config["scenarios"]["register"]
        self.client.post(reg["endpoint"], json=reg["payload"], headers=self.headers)

        # Login
        login = self.config["scenarios"]["login"]
        with self.client.post(login["endpoint"], json=login["payload"], headers=self.headers, catch_response=True) as resp:
            if resp.status_code == 200:
                self.token = resp.json().get("token")
                resp.success()
            else:
                resp.failure("Login failed")

        # Get Profile
        get = self.config["scenarios"]["get_profile"]
        profile_headers = self.headers.copy()
        if self.token:
            profile_headers["Authorization"] = f"Bearer {self.token}"
        self.client.get(get["endpoint"], headers=profile_headers)

    @task(3)
    def login_only(self):
        login = self.config["scenarios"]["login"]
        self.client.post(login["endpoint"], json=login["payload"], headers=self.headers)

    @task(2)
    def get_profile_only(self):
        get = self.config["scenarios"]["get_profile"]
        self.client.get(get["endpoint"], headers=self.headers)
