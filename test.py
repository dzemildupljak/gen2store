from geopy.geocoders import Nominatim
goelocator = Nominatim(user_agent="geoapiExercises")
zipcode = "36300"
location = goelocator.geocode(zipcode)
print("Zipcode: ", zipcode)
print("Location:", location)
