def enc(text):
    result=""
    for char in text:
        if 'A'<=char<='Z':
            result+=chr((ord(char)-ord('A')+13)%26+ord('A'))
        elif 'a'<=char<='z':
            result+=chr((ord(char)-ord('a')+13)%26+ord('a'))
        else:
            result+=char
    return result
message=input("Enter The Orignal Text : ")
print("Encrpyted Text :")
print(enc(message))