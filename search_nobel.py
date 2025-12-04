# Opal Reeves Assignment 10b (extra credit)
import json

def search_nobel(year, category):
    with open("nobels.json", "r") as f:
        data = json.load(f)

    surnames = []

    for prize in data["prizes"]:
        if prize["year"] == year and prize["category"] == category:

            for person in prize["laureates"]:
                surnames.append(person["surname"])
    
    return sorted(surnames)