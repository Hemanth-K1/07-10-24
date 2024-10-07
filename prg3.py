def is_palin(str):
    str = str.replace(" ", "").lower()
    return str == str[::-1]
str = input("Enter a string: ")
if is_palin(str):
    print(f"'{str}' is a palindrome.")
else:
    print(f"'{str}' is not a palindrome.")
