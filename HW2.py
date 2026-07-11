my_list = [1,2,3,4,5]

def print_list_reverse(lst):
    if not isinstance(lst, list) or not lst:
        print("Wrong list")
        return
    print(lst[::-1])

print_list_reverse(my_list)


def print_list_reverse1(lst):
    if not isinstance(lst, list) or lst== [] or lst == None:
        print("Wrong list")
        return
    print(lst[::-1])

print_list_reverse1(my_list)
print("*************")


point = (2.0,7)
def is_valid_point(point):
    if point is None or not point:
        return None
    if not (isinstance(point[0], (int, float))
            and isinstance(point[1], (int, float))):
        return False
    return True

print(is_valid_point(point))
print("*************")


sublist = [10,20,30,40,50,60,70,80]
def print_sublist_reverse(lst, start, finish):
    if not isinstance(lst, list) or type(start) is not int or type(finish) is not int:
        print("Wrong args")
        return
    if len(lst) == 0 or start < 0 or finish < 0 or start >= len(lst) or finish >= len(lst) or start > finish:
        print("Wrong args")
        return
    left_part = lst[:start]
    middle_part = lst[start:finish + 1]
    right_part = lst[finish + 1:]
    res = left_part + middle_part[::-1] + right_part
    print(res)


print_sublist_reverse(sublist, 1, 3)
print("*********")


students = {
    "Alice": 90,
    "Bob": 85,
    "Diana": 90,
    "Charlie": 85
}

def get_students_by_grade_(students):
    if (students is None or len(students) == 0
            or not isinstance(students, dict)):
        return {}
    result = {}
    for name, grade in students.items():
        if grade not in result:
            result[grade] = []
        result[grade].append(name)
    return result

print(get_students_by_grade_(students))