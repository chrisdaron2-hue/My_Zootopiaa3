import json

with open("animals_data.json", "r") as file:
    data = json.load(file)

#Iterate through the animals
for animal in data.get("animals", []):  # assumes your JSON has a top-level "animals" list
    if "Name" in animal:
        print(f"Name: {animal['Name']}")
    if "Diet" in animal:
        print(f"Diet: {animal['Diet']}")
    if "locations" in animal and isinstance(animal["locations"], list) and animal["locations"]:
        print(f"Location: {animal['locations'][0]}")
    if "Type" in animal:
        print(f"Type: {animal['Type']}")
    print("-" * 30)  # separator between animals

