from locust import HttpUser, constant, task

import re

# REQ_CNT = 0
# SUC_CNT = 0

def find_in_page(doc):
    # window.csrfToken = "DwSsXuVc-uECsSv6dW5ifI4025HacsODuhb8"
    decoded_data = doc.decode('utf-8')
    token_search = re.search('window.csrfToken = "([^"]+)"', decoded_data, re.IGNORECASE)
    assert token_search, "No csrf token found in response"
    return token_search.group(1)


class OverleafUser(HttpUser):
    wait_time = constant(1)
    
    @task
    def get_users(self):
        # REQ_CNT += 1
        res = self.client.get("/login")
        self.csrf_token = find_in_page(res.content)
        # print(self.csrf_token)
        data = {
        "_csrf": self.csrf_token,
        "email": "admin@example.com",
        "password": "kapil123"
        }
        r = self.client.post("/login", data)
        # SUC_CNT += 1
        # print(SUC_CNT, REQ_CNT)
        # r = r.decode('utf-8')
        # assert r.json().get("redir", None) == "/project"
        