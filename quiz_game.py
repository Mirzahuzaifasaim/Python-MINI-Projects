print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("okay Let's play: )")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "Central processing unit":
    print('correct!')
    score += 1
else:
    print('incorrect!')

answer = input("What does GPU  stand for? ")
if answer.lower() == "graphics processing unit":
    print('correct!')
    score += 1
else:
    print('incorrect!')

answer = input("What does PAF stand for? ")
if answer.lower() == "pak air force":
    print('correct!')
    score += 1
else:
    print('incorrect!')

answer = input("What does ROM stand for? ")
if answer.lower() == "random only memory":
    print('correct!')
    score += 1
else:
    print('incorrect!')

print("You got " + str(score)+ "questions correct!")
print("You got " + str((score / 4 )* 100) + "%.")