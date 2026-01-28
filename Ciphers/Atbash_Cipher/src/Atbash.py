def atbash(message):
	cipher=""
	for ch in message:
		if 'A'<=ch<='Z':
			cipher+=chr(ord('A')+ord('Z')-ord(ch))
		elif 'a'<=ch<='z':
			cipher+=chr(ord('a')+ord('z')-ord(ch))
		else:
			cipher+=ch
	return cipher
a=input("ENTER THE STRING: \n")
print(f"Encrpyted String Is \n{atbash(a)}")
