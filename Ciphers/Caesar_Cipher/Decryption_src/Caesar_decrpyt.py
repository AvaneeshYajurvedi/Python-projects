def decrpyt(text,shift):
	result=""
	for char in message:
		if 'A'<=char<='Z':
			result+=chr((ord(char)-ord('A')-shift)%26+ord('A'))
		elif 'a'<=char<='z':
			result+=chr((ord(char)-ord('a')-shift)%26+ord('a'))
		else:
			result+=char
	return result
message=input("ENTER THE ENCRYPTED TEXT \n")
shift=int(input("ENTER THE SHIFT VALUE \n"))
print(f"THE DECRPYTED TEXT IS \n{decrpyt(message,shift)}")
