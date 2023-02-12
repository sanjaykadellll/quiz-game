print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "y":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What is capita; city of Nepal? ")
if answer.lower() == "kathmandu":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("in which district is pokhara? ")
if answer.lower() == "kaski":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("states  of Nepal? ")
if answer.lower() == "6":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")