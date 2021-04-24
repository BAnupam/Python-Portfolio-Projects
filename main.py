from morse_code_data import morse_dict

text = input("Enter text to convert : ").upper()
print("Input : ", text)

morse_code = ""
words = text.split()
print(words)

for word in words:
    for char in word:
        if morse_dict[char]:
            morse_code += morse_dict[char] + " "
        else:
            print("Invalid character : ", char)
    morse_code += "   "
morse_code += "       "

print("Morse Code : ", morse_code)
