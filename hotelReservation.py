from locust import HttpUser, constant, task
import random
import re

# REQ_CNT = 0
# SUC_CNT = 0

def get_user():
    id = random.randint(1,1)
    user_name = "Cornell_"+str(id)
    pass_word = ""
    for i in range(0,10):
        pass_word += str(1)
    return user_name, pass_word

class HotelReservationUser(HttpUser):
    wait_time = constant(1)
    
    @task(600)
    def search_hotel(self):
        in_date = random.randint(9,23)
        out_date = random.randint(in_date+1, 24)
        in_date_str = str(in_date)
        if in_date <= 9:
            in_date_str = "2015-04-0" + in_date_str
        else:
            in_date_str = "2015-04-" + in_date_str
        
        out_date_str = str(out_date)
        if out_date <= 9:
            out_date_str = "2015-04-0" + out_date_str
        else:
            out_date_str = "2015-04-" + out_date_str
        
        lat = 38.0235 + (random.randint(0, 481) - 240.5)/1000.0
        lon = -122.095 + (random.randint(0, 325) - 157.0)/1000.0
        r = self.client.get("/hotels?inDate="+in_date_str+"&outDate="+out_date_str+"&lat="+str(lat)+"&lon="+str(lon))
        
    @task(390)
    def recommend(self):
        coin = random.uniform(0,1)
        req_param = ""
        if coin < 0.33:
            req_param = "dis"
        elif coin < 0.66:
            req_param = "rate"
        else:
            req_param = "price"
        lat = 38.0235 + (random.randint(0, 481) - 240.5)/1000.0
        lon = -122.095 + (random.randint(0, 325) - 157.0)/1000.0
        r = self.client.get("/recommendations?require="+req_param+"&lat="+str(lat)+"&lon="+str(lon))

    @task(5)
    def reserve(self):
        in_date = random.randint(9,23)
        out_date = in_date+random.randint(1,5)
        in_date_str = str(in_date)
        if in_date <= 9:
            in_date_str = "2015-04-0" + in_date_str
        else:
            in_date_str = "2015-04-" + in_date_str
        
        out_date_str = str(out_date)
        if out_date <= 9:
            out_date_str = "2015-04-0" + out_date_str
        else:
            out_date_str = "2015-04-" + out_date_str
            
        hotel_id = str(random.randint(1,80))
        user_id, password = get_user()
        cust_name = user_id
        num_room = "1"
        r = self.client.post("/reservation?inDate="+in_date_str+"&outDate="+out_date_str+"&hotelId="+hotel_id
                             +"&username="+user_id+"&password="+password+"&number="+num_room+"&customerName=Cornell_")
    
    @task(5)
    def user_login(self):
        user_name, password = get_user()
        r = self.client.get("/user?username="+user_name+"&password="+password)