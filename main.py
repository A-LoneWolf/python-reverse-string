def reverse(text):
	return text[::-1]
	
continues= True
while continues:	
	txt_input = input("Please Type some string to reverse: ")
	print(f"Reverse string of {txt_input} is \"{reverse(txt_input)}\"")
	again=input("\nDo you want to Try again? Y/n : ").lower()
	if again == "y":
		None
	else:
		continues=False
