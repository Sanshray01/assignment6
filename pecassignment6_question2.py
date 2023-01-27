


def Palindrome(phr):	
	l1 = list(''.join(phr.split()))
	if l1 == list(reversed(l1)):	
		return True 
	else:
		return False
inp = input('Enter a Phrase: ')
if Palindrome(inp):
	print("It is a palindrome ")
	
else: 
	print('It is not a palindrome')
	

		
		
		