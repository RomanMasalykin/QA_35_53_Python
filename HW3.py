def create_profile(name, age = 18, city = "Unknown"):
    res = {f"name: {name}, age: {age}, city: {city}"}
    return res

print(create_profile("Anna"))
print(create_profile(city = "NY", name = "Monica"))
print("***********")

def sum_even_numbers(*numbers):
    if not numbers:
        return 0
    sum_all = 0
    for n in numbers:
        if n%2==0:
            sum_all += n
    return sum_all

# return sum(n for n in numbers if n%2==0)

print(sum_even_numbers(1,2,3,4,5,6))
print("**********")


def print_pet_info(name, **info):
    print(name)
    for key, value in info.items():
        print(f"{key}: \"{value}\"")

print_pet_info("Lucky", age = 4,color = "White",breed = "Spitz")
print("**********")


def merge_lists(*lists):
    if not lists:
        return []
    res_ = []
    for l in lists:
        res_ += l
    return res_

print(merge_lists([1, 2],[3],[4, 5],[]))
print("*********")
# return sum(lists, [])


def build_message(*words, separator = " "):
    if not words:
        return None
    return separator.join(words)

print(build_message("Hello","World"))
