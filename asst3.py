#generates a random integer between 1 and 6, like a die.  Will assign a grade based on that number.  Can account for errors if a number outside the range of 1-6 is generated.
import random
num=random.randint(1,6)
print(num)
if(num==3):
    print("Your grade is D.")
elif(num==6):
	print("Your grade is A.")
elif(num==5):
	print("Your grade is B.")
elif(num==4):
    print("Your grade is C.")
elif(num==2):
    print("Your grade is F.")
elif(num==1):
    print("Your grade is W.")
elif(num<1):
    print("An error has occured.")
elif(num>6):
    print("An error has occured.")
else:
    print("An error has occured.")
    
