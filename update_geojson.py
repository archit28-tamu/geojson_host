import json
import random
import datetime

# Get current timestamp for tracking updates
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Load the existing GeoJSON file
with open("dummy.geojson", "r") as f:
    geojson_data = json.load(f)

# Update the population of each city with significant changes
for feature in geojson_data["features"]:
    # Create more noticeable changes (±5-10% of population)
    current_population = feature["properties"]["Population"]
    change_percentage = random.uniform(-0.10, 0.10)  # -10% to +10%
    population_change = int(current_population * change_percentage)
    feature["properties"]["Population"] += population_change
    
    # Add last updated timestamp to each feature
    feature["properties"]["LastUpdated"] = current_time

# Randomly decide whether to add a new city (25% chance)
if random.random() < 0.25:
    # List of potential new Texas cities to add
    potential_cities = [
        {"name": "San Antonio", "coordinates": [-98.4936, 29.4241], "population": 1547253},
        {"name": "Fort Worth", "coordinates": [-97.3208, 32.7555], "population": 927720},
        {"name": "El Paso", "coordinates": [-106.4850, 31.7619], "population": 678815},
        {"name": "Arlington", "coordinates": [-97.1081, 32.7357], "population": 398112},
        {"name": "Corpus Christi", "coordinates": [-97.3964, 27.8006], "population": 317863}
    ]
    
    # Filter out cities that are already in the GeoJSON
    existing_cities = [feature["properties"]["City"] for feature in geojson_data["features"]]
    available_cities = [city for city in potential_cities if city["name"] not in existing_cities]
    
    # Add a new city if there are any available
    if available_cities:
        new_city = random.choice(available_cities)
        new_feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": new_city["coordinates"]
            },
            "properties": {
                "City": new_city["name"],
                "Population": new_city["population"],
                "LastUpdated": current_time
            }
        }
        geojson_data["features"].append(new_feature)

# Save the updated GeoJSON to a file
with open("dummy.geojson", "w") as f:
    json.dump(geojson_data, f, indent=4)

print(f"GeoJSON file updated successfully at {current_time}")
