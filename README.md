For HotelReservation,

run the following command:

locust -f hotelReservation.py --host http://155.98.36.145:30915 --web-port 8090
replace host with new url

locust -f hotelReservation.py --host http://155.98.36.145:30915 --headless --run-time 5h -u 5000 -r 1 --csv=hotelReservationResults


For Overleaf,

run the following command:

locust -f overleaf_adv.py --host http://155.98.36.145:30910 --web-port 8091
replace host with new url
locust -f overleaf_adv.py --host http://155.98.36.145:30915 --headless --run-time 5h -u 500 -r 1 --csv=overleafResults


forward port to local if running on remote machine.