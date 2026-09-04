print ("Hello, I am an AI chatterbox, what is your name?")
name = input()
print (f"Nice to meet you {name}! How are you doing today? (Good/Bad)")
mood = input().lower()
if mood == "good":
    print ("Oh wow, I'm glad to hear that!")
elif mood == "bad":
    print ("That's okay, tomorrow will be better.")
else:
    print ("It can be hard to express some feelings into words, can it not?")
print ("It was a pleasure interacting with you, see you soon!")