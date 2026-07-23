def get_list_element(items, index):
    try:
        return items[index]
    except IndexError:
        return "index is out of range"

numbers = [1,3,46,5,6]
print(get_list_element(numbers, 4))
print()


user = {
"name": "Anna",
"age": 30
}

def get_user_data(user, key):
    try:
        return user[key]
    except KeyError:
        return "No such key"

print(get_user_data(user, "age"))
print()


def calculate_average(first_value, second_value):
    try:
        res = (float(first_value) + float(second_value))/2
        return res
    except ValueError:
        return "Invalid value"
    except TypeError:
        return "Invalid data type"

print(calculate_average(10, 20))
print(calculate_average("hello", 20))
print(calculate_average(None, 20))
print()


def read_number():
    try:
        res = int(input("Insert number: "))
        print("Number was entered successfully")
    except ValueError:
        print("Invalid number")
    finally:
        print("Program finished")

# read_number()
print()

def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age > 120:
        raise ValueError("Age is not realistic")

validate_age(10)