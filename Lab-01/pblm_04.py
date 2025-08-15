#Uppercase or Lowercase

char = input("Enter a character: ")

if char >= "A" and char <= "Z":
    print("Uppercase letter")
elif char >= "a" and char <= "z":
    print("Lowercase letter")
else:
    print("Not a letter")
