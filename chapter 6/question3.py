a = input("Enter the comment : ")
spam_1 = "Make a lot of money"
spam_2 = "buy now"
spam_3 = "subscribe this"
spam_4 = "click this"

if(spam_1 in a or spam_2 in a or spam_3 in a or spam_4 in a): print("Its a spam")
else: print("Not spam")
