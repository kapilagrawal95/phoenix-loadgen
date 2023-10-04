from locust import User, task, constant

class MyFirstTest(User):
    weight=2
    wait_time = constant(1)
    
    @task
    def launch(self):
        print("launching")
        
    @task
    def search(self):
        print("Searching")
        
        
class MySecondTest(User):
    weight=2
    wait_time = constant(1)
    @task
    def launch2(self):
        print("second launching")
        
    @task
    def search2(self):
        print("second Searching")