def count(string, char):
    return string.count(char)
string = input("Enter a string: ")
char = input("Enter the character: ")
occurrence = count(string, char)
print(f"The character '{char}' occurs {occurrence} times in the string.")
