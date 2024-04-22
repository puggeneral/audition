# This is a sample Python script.
import random


def random_power():
    return [random.randint(1, high_num), random.randint(1, high_num), random.randint(1, high_num),
            random.randint(1, high_num), random.randint(1, high_num), random.randint(1, high_num),
            random.randint(1, high_num)]


print("this is a guess the number game but with a bit of a twist")
playing = input("would you like to play ")
play_again = "yes"
if playing != "yes" and playing != "of course":
    print("Oh in that case drop by later if you change your mind")

else:
    while play_again == "yes":
        high_num = 50
        number = random.randint(1, 50)
        not_number = random.randint(1, 50)
        power_ups = [random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50),
                     random.randint(1, 50)]
        power_downs = [random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50),
                       random.randint(1, 50)]
        game_playing = "yes"
        guesses = -1
        while game_playing == "yes":
            guesses += 1
            print(f"guess a number from 1-{high_num}")
            print(f"total guesses: {guesses}")
            answer = input("your number: ")
            answer_int = int(answer)
            if answer_int == number:
                print(f"congrats your got the number in {guesses} guesses")
                play_again = input("do you want to play again ")
                if play_again == "no":
                    game_playing = "no"
                else:
                    number = random.randint(1, 50)
                    guesses = -1
                    high_num = 0
                    power_ups = random_power()
                    power_downs = random_power()
            elif answer_int in power_ups:
                power = random.randint(1, 100)
                hints = 0
                if power < 50:
                    if hints < 1:
                        print("you got a powerup you get a hint")
                        if number < 10:
                            print("the number is from 1-10")
                        elif number < 20:
                            print("the number is from 10-20")
                        elif number < 30:
                            print("the number is from 20-30")
                        elif number < 40:
                            print("the number is from 30-40")
                        elif number < 50:
                            print("the number is from 40-50")
                        else:
                            print("the number is over 50")
                    else:
                        if number <= 10:
                            if number < 6:
                                print("the number is from 1-5")
                            else:
                                print("the number is from 6-10")
                        elif number <= 20:
                            if number < 16:
                                print("the number is from 10-15")
                            else:
                                print("the number is from 16-20")
                        elif number <= 30:
                            if number < 26:
                                print("the number is from 20-25")
                            else:
                                print("the number is from 25-30")
                        elif number <= 40:
                            if number < 36:
                                print("the number is from 30-35")
                            else:
                                print("the number is from 36-40")
                        elif number <= 50:
                            if number < 46:
                                print("the number is from 40-45")
                            else:
                                print("the number is from 45-50")
                        elif number <= 60:
                            if number < 56:
                                print("the number is from 50-55")
                            else:
                                print("the number is from 56-60")
                        elif number <= 70:
                            if number < 66:
                                print("the number is from 60-65")
                            else:
                                print("the number is from 66-70")
                        else:
                            print("the number is over 70")
                    power_ups = random_power()
                    power_downs = random_power()
                    hints += 1
                elif power < 51:
                    print(f"the number is {number}")
                elif power < 89:
                    print("you got a powerup")
                    if hints > 0:
                        if number <= 10:
                            if number < 6:
                                print("the number is from 1-5")
                            else:
                                print("the number is from 6-10")
                        elif number <= 20:
                            if number < 16:
                                print("the number is from 10-15")
                            else:
                                print("the number is from 16-20")
                        elif number <= 30:
                            if number < 26:
                                print("the number is from 20-25")
                            else:
                                print("the number is from 25-30")
                        elif number <= 40:
                            if number < 36:
                                print("the number is from 30-35")
                            else:
                                print("the number is from 36-40")
                        elif number <= 50:
                            if number < 46:
                                print("the number is from 40-45")
                            else:
                                print("the number is from 45-50")
                        elif number <= 60:
                            if number < 56:
                                print("the number is from 50-55")
                            else:
                                print("the number is from 56-60")
                        elif number <= 70:
                            if number < 66:
                                print("the number is from 60-65")
                            else:
                                print("the number is from 66-70")
                        else:
                            print("the number is over 70")
                    else:
                        high_num -= 10
                        print("the number is now in a smaller range")
                        number = random.randint(1, high_num)
                    power_ups = random_power()
                    power_downs = random_power()
                else:
                    print("you got a powerup you get a hint")
                    while not_number == number:
                        not_number = random.randint(1, 50)
                    print(f"the number is not {not_number}")
                    not_number = random.randint(1, 50)
                    while not_number == number:
                        not_number = random.randint(1, 50)
                    print(f"the number is not {not_number}")
                    power_ups = random_power()
                    power_downs = random_power()
            elif answer_int in power_downs:
                print("you got a bad number a new number will now be picked and the range will be bigger")
                high_num += 10
                number = random.randint(1, high_num)
                power_ups = random_power()
                power_downs = random_power()
            else:
                print("that's not it guess again")
