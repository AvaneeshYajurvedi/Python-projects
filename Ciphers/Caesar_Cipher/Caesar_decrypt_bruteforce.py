def brute_force(ciphertext):
	for shift in range(1,26):
		result=''
		for char in message:
			if 'A'<=char<='Z':
				result+=chr((ord(char)-ord('A')-shift)%26+ord('A'))
			elif 'a'<=char<='z':
				result+=chr((ord(char)-ord('a')-shift)%26+ord('a'))
			else:
				result+=char
		print(f"Shift {shift}:{result}")
message=input("ENTER THE ENCRYPTED TEXT \n")
brute_force(message)
