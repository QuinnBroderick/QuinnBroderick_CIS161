#problem 1 below
pet_type = "Labradoodle"#creats a varible and sets it to a string Labradoodle
pet_name = "Rumble"#creats a varible and sets it to a string rumble
sentence = f"I have a dog named {pet_name} and he is a {pet_type}"#creats a varible that will contain a sentence
print (sentence) # prints the sentence

#problem 2 below

name = input("Your name is:") # gets an input and sets it equal to varible name
age = None
while age is None: # creates a loop that askes for an input that is an int and checks to make sure it is an int if not the program ends
    try:
        age = int(input("Your age is:")) # gets an input coverts it to an int then sets it to varible age
    except ValueError:
        print("input is not an integer")
savings = None
while savings is None: # creates a loop that askes for an input that is an int and checks to make sure it is an int if not the program ends
    try:
        savings = int(input("Your yearly savings are:"))# get an input coverts it to an int then sets it to varible savings
    except ValueError:
        print("input is not an integer")
sentence1 = f"\nHello {name}! You are currently {age} years old. In 10 years, you will be {age + 10} years old."#creats a varible that contains a sentence
sentence2 = f"\nIf you save ${savings} each year, in 5 years you will have saved ${savings*5}."#creats a varible that contains a sentence
sentence3 = f"\nYour average monthly savings is ${savings/12}."#creats a varible that contains a sentence
print(sentence1) # prints the sentence
print(sentence2) # prints the sentence
print(sentence3) # prints the sentence

#problem 3 below

from datetime import datetime #imports datetime from the datetime libary
current_date = datetime.now().month # uses the datetime func along with the month fuct to set  the varible current_date equal to the current month
months_dic = {1:"january",2:"february",3:"march",4:"april",5:"may",6:"june",7:"july",8:"august",9:"september",10:"october",11:"november",12:"december"}# creates a dicionary that contains all the months and sets them to their associated number desication
days_dic = {1:31 ,2:28 ,3:31 ,4:30 ,5:31 ,6:30 ,7:31 ,8:31 ,9:30 ,10:31 ,11:30 ,12:31 } # creats a dic that contains all the month desictions and assocates them to the number of days in each month
print(f"\nthe current month is {months_dic[current_date]} and there are {days_dic[current_date]} days in it") # prints a sentence

# problem 4 below
eggs = None
while eggs is None:
    try:
        eggs= int(input("\nHow many eggs do you have:")) # asks for an input converts it to an int then sets it to varible eggs
    except ValueError:
        print("input is not an integer")
sentence4 = f"\nThis makes {int(eggs/12)} with {eggs%12} left over" # creats a sentence with the nuber of dozens you have with how many left over
print(sentence4) # prints the sentence




