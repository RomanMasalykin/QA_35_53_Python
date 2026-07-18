import csv
import json
items = [
"Milk",
"Bread",
"Apples",
"Coffee"
]

def save_shopping_list(items):
    with open("shopping_list1.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        for i in items:
            writer.writerow([i])

save_shopping_list(items)
print()


with open("students.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age"])
    writer.writerow(["Anna", "21"])
    writer.writerow(["Tom", "19"])
    writer.writerow(["Kate", "22"])

def students_info(filename):
    with open("students.csv", "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Student: {row["name"]} ({row["age"]})")

students_info("students.csv")


def save_profile(name, age, city):
    profile_dict = {
        "name":name,
        "age":age,
        "city":city
    }
    with open("profile.json", "w", encoding="utf-8") as file:
        json.dump(profile_dict, file, indent=4)

save_profile("Chandler", 28, "NY")



