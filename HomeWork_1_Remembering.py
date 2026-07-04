s = "Shalom"

def print_reverse_string(s):
    if not s or s.strip():
        print("Wrong string")
    else:
        print(s[::-1])

# print_reverse_string(s)


phone = "0968663763"

def is_phone_number(phone):
    if  not phone or not phone.strip():
        return None
    elif phone.isdigit() and len(phone) == 10 and phone[0] == "0":
        return True
    else:
        return "Error"

# print(is_phone_number(phone))
'''
phone.startswith("0")
'''


word = "Gandalf"

def print_substring_reverse(word, start, finish):
   if not word or not word.strip():
       print("Wrong args")
       return
   if start < 0 or finish < 0 or start > finish or start >= len(word) or finish >= len(word):
       print("Wrong args")
       return
   else:
       left_part = word[:start]
       middle_part_reversed = word[start:finish+1][::-1]
       right_part = word[finish+1:]

       result = left_part + middle_part_reversed + right_part
       print(result)

print_substring_reverse(word, 1, 3)


sen = "Hold your horses mister"

def get_words_reverse(sen):
    step1 = sen.split()
    step2 = step1[::-1]
    result = " ".join(step2)
    print(result)

# get_words_reverse(sen)


def get_words_reverse_in_columns(sen):
    step1 = sen.split()[::-1]
    print("\n".join(step1)[::-1])

get_words_reverse_in_columns(sen)