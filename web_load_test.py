from locust import HttpUser, task, between
from utils.helpers import load_test_config

class UserFlow(HttpUser):
    config = load_test_config("configs/test.yaml")
    host = config["host"]
    wait_time = between(1, 2)

    @task
    def user_flow(self):
        # Step 1: Register
        reg = self.config["scenarios"]["register"]
        self.client.post(reg["endpoint"], json=reg["payload"])

        # Step 2: Login
        login = self.config["scenarios"]["login"]
        with self.client.post(login["endpoint"], json=login["payload"], catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Login failed")

        # Step 3: Get profile
        get = self.config["scenarios"]["get_profile"]
        self.client.get(get["endpoint"])
