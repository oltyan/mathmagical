import random

def get_continue(hp,enemy_count):
    if hp > 0 and enemy_count > 0:
        return True
    else:
        return False

def choose_difficulty():
    print("Please Select a difficulty: \n"
          "1. Easy (5 mosters, 0-10 numbers\n"
          "2. Challenge (8 monsters, 0-20\n"
          "3. Brutal (10 monsters, 0-100\n")
    selection_made = False
    while selection_made == False:
        try:
            difficulty = input("Selection: ")
            if int(difficulty) not in [1, 2, 3]:
                raise Exception
            selection_made = True
        except Exception as e:
            print("Invalid Input")
    return difficulty

def additions(difficulty):
    # Change parameters based on difficulty settings
    if int(difficulty) == 1:
        print("Difficulty set to Easy")
        max_int = 10
    if int(difficulty) == 2:
        print("Difficulty set to Challenging")
        max_int = 20
    if int(difficulty) == 3:
        print("Difficulty set to Brutal")
        max_int = 100
    hp = 3
    enemy_count = 5
    repeat = True
    while repeat == True:

        a = random.randint(0, max_int)
        b = random.randint(0, max_int)

        problem_string = str(a) + " + " + str(b) + " = ???"
        print(problem_string)
        problem = a + b
        answer = input("Answer: ")
        if int(answer) == int(problem):
            print("Correct")
            enemy_count -= 1
        else:
            print("Incorrect")
            hp -= 1
        hp_remaining = "HP Remaining: " + str(hp)
        enemy_remaining = "Enemies Left: " +str(enemy_count)
        print(hp_remaining)
        print(enemy_remaining)
        repeat = get_continue(hp, enemy_count)


def main():
    additions(choose_difficulty())
