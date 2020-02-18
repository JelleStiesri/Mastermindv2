import random
import itertools

def create_code():
    code = ''
    for i in range(0, 4):
        number = random.randint(1, 6)
        code_num = str(number)
        code += code_num

    return code




def game_menu():
    print("""
Welcome to mastermind
Guess the four number code
Each number in the code is between 1 and 6
B = right number in the right spot
W = right number but in the wrong spot
X = number not in the code
Gamemodes:
1. cpu gives a code player guesses
2. player gives code cpu guesses (algorithm 1)
3. player gives code cpu guesses (algorithm 2)
4. player gives code cpu guesses (self made algorithm 3)
5. Exit game
    """)
    while True: #Zodat je het spel nog een keer kan spelen
        game = input('Enter your choice: ')
        if game.isdigit(): #waarom geen int vragen?
            if game == '1':
                game_1()
            elif game == '2':
                game_2()
            elif game == '3':
                game_3()
            elif game == '4':
                print(game_4())
            elif game == '5':
                break


def create_all_answers():
    all_answers = []
    all_answers = sorted(list(itertools.product('123456', repeat=4)))

    return all_answers


def create_feedback(code, guess):
    feedback = {'B': 0, 'W': 0}
    lst = []

    for i in range(0, 4):
        if code[i] == guess[i]:
            feedback['B'] += 1
            lst.append(guess[i])

    for i in range(0, 4):
        if guess[i] in code:
            num = guess[i]
            num_count = guess.count(num)
            num2_count = code.count(num)
            if lst.count(guess[i]) < num_count and lst.count(guess[i]) < num2_count:
                lst.append(num)
                feedback['W'] += 1

    return feedback


def calc_worst_case(lst):
    # nog niet af
    for i in lst:
        cac = 0
        item_feedback = create_feedback()


def simple_strategy(lst):
    # af
    code = input('Enter a code: ')
    if not code.isdigit():
        print('Enter a code with numbers between one and six')
    else:
        print(code)
        attempts = 0
        lives = 10
        while lives > 0:
            guess = lst[0]
            feedback = create_feedback(code, guess)
            print(guess)
            print(feedback)
            for i in reversed(lst):
                item_feedback = create_feedback(guess, i)
                if feedback != item_feedback:
                    lst.remove(i)
            print(lst)
            lives -= 1
            attempts += 1
            if guess == code:
                print('De computer heeft de code geraden in ', attempts, ' pogingen')
                break
            elif lives == 0:
                print('GAME OVER')
            else:
                print('De computer heeft de code niet geraden')


def worst_case(lst):
    # nog niet af
    code = input('Enter a code: ')
    if not code.isdigit():
        print('Enter a code with numbers between one and six')
    else:
        attempts = 0
        lives = 10
        while lives > 0:
            if attempts == 0:
                guess = '1122'
            else:
                guess = calc_worst_case(lst)

            print(guess)
            feedback = create_feedback(code, guess)
            print(feedback)
            for i in reversed(lst):
                item_feedback = create_feedback(guess, i)
                if item_feedback != feedback:
                    lst.remove(i)

            print(len(lst))
            attempts += 1
            lives -= 1

            if lives == 0:
                print('De computer heeft de code niet geraden')
                break

            elif code == guess:
                print('De computer heeft de code geraden in ', attempts, ' pogingen')
                break


def game_1():
    # af

    lives = 10
    code = create_code()

    while lives > 0:
        guess = input("Guess the code: ")
        if not guess.isdigit():
            print('Enter a code with numbers between one and six')
        else:
            if len(guess) != 4:
                print('Enter a four digit code')
            else:
                if code == guess:
                    print('You guessed the code')
                    exit()

                else:
                    feedback = []
                    for i in range(0, len(guess)):
                        if guess[i] == code[i]:
                            feedback.append('B')

                        elif guess[i] in code:
                            feedback.append('W')

                        else:
                            feedback.append('X')
                    lives -= 1

                    random.shuffle(feedback)
                    feedback = "-".join(feedback)
                    print(feedback)

    if lives == 0:
        print('GAME OVER')
        exit()


def game_2():
    all_answers = create_all_answers()
    simple_strategy(all_answers)


def game_3():
    all_answers = create_all_answers()
    worst_case(all_answers)


def game_4():
    all_answers = create_all_answers()
    code = input('Enter a code: ')
    attempts = 0
    for i in all_answers:
        if i == code:
            return 'De code is gevonden in ' + str(attempts) + ' pogingen'
        else:
            attempts += 1


game_menu()
"""
bronvermeldingen:
"""