import json

cities = {
    "Lahore": 13000000,
    "Karachi": 18000000,
    "Islamabad": 1200000 
}

with open("cities.json", "w") as file:
    json.dump(cities, file, indent=4 , sort_keys=True)

with open("cities.json", "r") as file:
    data = json.load(file)  
     
for city, population in data.items():
    print(f"{city}: {population}")    

new_city = input("Enter a new city name: ")
new_population = int(input("Enter the population of the new city: "))

data[new_city] = new_population

with open("cities.json", "w") as file:
    json.dump(data, file, indent=4 , sort_keys=True)
    print("\nNew city added successfully!")