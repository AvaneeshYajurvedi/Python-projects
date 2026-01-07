n=str(input("Enter The Password\n"))
m=len(n)
if m>14:
    print("PASSWORD LENGTH CAN BE ONLY 14 CHARACTERS LONG!\n")
    exit()
else:
    count=0
    number = 0
    uppercase = 0
    lowercase = 0
    for ch in n:
        if ch in "!@#$%^&*()_+-={}[]|:;'<>,.?/":
            count+=1
    for ch1 in n:
        if ch1 in "0123456789":
            number+=1
    for ch2 in n:
        if ch2 in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            uppercase+=1
    for ch3 in n:
        if ch3 in "abcdefghijklmnopqrstuvwxyz":
            lowercase+=1
types=0
if lowercase>0:
    types+=1
if uppercase>0:
    types+=1
if number>0:
    types+=1
if count>0:
    types+=1    

if m<6 or types==1:
    print("Password Strength:WEAK\n")
    print("Suggestions to improve your password:\n1. Use at least 6 characters.\n2. Include a mix of uppercase and lowercase letters, numbers, and special characters.\n")
elif types==2 or types==3:
    print("Password Strength: MEDIUM\n")
    print("Suggestions to improve your password:\n1. Use a mix of uppercase and lowercase letters, numbers, and special characters.\n2. Avoid using common words or easily guessable information.\n")
else:
    print("Password Strength: STRONG\n")
    print("Your password is strong. Remember to update it regularly and avoid using the same password across multiple sites.\n")    