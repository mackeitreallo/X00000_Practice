#Write your code below this line 👇
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
        
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
    ]
#Write your code above this line 👆

def add_new_country(country_visited, visit_times, cities_visited):
    new_country = {}
    new_country["country"] = cities_visited
    new_country["visits"] = visit_times
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

#Do NOT change any of the code below👇
add_new_country("Russia", 2, ["Moscow", "Saint Pettersberg"])
print(travel_log)