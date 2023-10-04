from locust import HttpUser, task, between

class OverleafUser(HttpUser):
    wait_time = between(1, 5)  # Random wait time between requests

    @task
    def access_overleaf(self):
        self.client.get("http://localhost:8080")

