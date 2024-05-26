def reverse_string(name):
    rev_string = ""
    for s in name:
        rev_string = s + rev_string
    return rev_string


# reverse = reverse_string("sharan")
# print(reverse)

original_string = input("Enter the string")
rev_string = reverse_string(original_string)
print(rev_string)

if original_string == rev_string:
    print("Palindrome")
else:
    print("Not a Palindrome")
