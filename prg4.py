def replace(string, char):
    return string.replace(" ", char)
string = input("Enter a string: ")
char = input("Enter the character to replace spaces with: ")
modified_string = replace(string, char)
print(f"Modified string: {modified_string}")
