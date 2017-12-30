import random

def get_continue():
    response = input("Would you like to continue? 1 = Yes, 2 = No : ")
    if response == '1':
        return True
    if response == '2':
        return False

def additions():
    repeat = True
    while repeat == True:

        a = random.randint(0, 20)
        b = random.randint(0, 20)

        problem_string = str(a) + " + " + str(b) + " = ???"
        print(problem_string)
        problem = a + b
        answer = input("Answer: ")
        if int(answer) == int(problem):
            print("Correct")
        else:
            print("Incorrect")
        repeat = get_continue()

def main():
    additions()
