print("""
Welcome to UniBuddy! 
Your all-in-one app that makes your freshman jounrey a bit easier to navigate!

Please enter your credentitals to get started :    
""")

user_name = input("Please enter your student name: ").capitalize()
user_age = int(input("Please enter your age: "))
fav_colour = input("Please enter your favourite colour: ").capitalize()

print(f"""
Welcome {user_name}! I see that your favourite colour is {fav_colour}.
""")

if fav_colour == "Red":
    print("If you like the colour RED, I have the following for you!")
    print("""
1. Our red colour themed football club.
2. Our red themed art club.
3. Our red wine and cheese society.
""")
    
elif fav_colour == "Blue":
    print("If you like the colour BLUE, I have the following for you!")
    print("""
1. Our blue colour themed football club.
2. Our swimming club with a bright blue pool.
3. Our fighting game club, where you can throw digital hands.       
""")

elif fav_colour == "Yellow":
    print("If you like the colour YELLOW, I have the following for you!")
    print("""
1. Our basketball club.
2. Our sunbathing society.
3. Our dance club.  
""")
        
elif fav_colour == "Orange":
    print("If you like the colour ORANGE, I have the following for you!")
    print("""
1. Our orange juice drinking club.
2. Our travelling society.
3. Our orange dress club.
""")
    
elif fav_colour == "Pink":
    print("If you like the colour PINK, I have the following for you!")
    print("""
1. Our pink ligloss club. 
2. Our flower conservation society.
3. Our pink sweet eating society.
""")

elif fav_colour == "Purple":
    print("If you like the colour PURPLE, I have the following for you!")
    print("""
1. Our purple trouser club.
2. Our purple bow club.
3. Our film club.""")
          
elif fav_colour == "Green":
    print("If you like the colour GREEN, I have the following for you!")
    print("""
1. Our eco-friendly choices society.
2. Our healthy eating club.
3. Our gourmet cheese club.""")

else:
    print("I am not sure if that was a colour you entered. Please try again.")

if user_age <= 21:
    print("Here are some freshman related events!")
    print("""
1. Friend speed dating.
2. Our freshman society.
3. Our dance club.""")

else:
    print("Here are a few event suggestions that might be to your liking:")
    print("""
1. Our wine tasting with cheese club.
2. Our sunbathing society.
3. Our beer drinking club.""")

print("""
Here is some FAQs:
      
1. When does the term start?
2. Do you have a contact number?
3. Where is the main campus?
4. Where do I find more information?""")

question = input("Is there anything you would like to ask me from the FAQ's above? ").capitalize()

if question == "Q":
    print("Thank you! Bye.")

elif question == "When does the term start?":
    print("It starts in January 2024.")

elif question == "Where is the main campus?":
    print("It is at 74 Zoo lane.")

elif question == "Do you have a contact number?":
    print("Yes, it is 0116 759 283")

elif question == "Where do I find more information?":
    print("You can visit our website where we have all our information.")
        
elif question != "Q":
    print("I am sorry, I do not understand. Please ask me a question from the list.")
