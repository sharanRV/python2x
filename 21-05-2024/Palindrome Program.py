#palindrome Program
txt = input("Enter the text")
reverse = txt[::-1]
if txt == reverse:
    print(f"{txt}  is Palindrome ")
else:
    print(f"{txt}  is not palindrome ")