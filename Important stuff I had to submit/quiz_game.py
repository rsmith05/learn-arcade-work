def main(answers_correct):
    print("Quiz game")
    print()

    # FIRST QUESTION
    question_1 = input("What pokemon is a fire type?\nA. Bulbasaur"
                       "\nB. Charmander\nC. Altaria\nD. Greninja\n? ")
    if question_1.upper() == "B":
        print("Correct!")
        answers_correct += 1
    else:
        print("Incorrect!")
    print()

    # SECOND QUESTION
    question_2 = input("What is the airspeed velocity of a European unladen swallow?"
                       "\nA. 26 mi/h\nB. 20 mi/h\nC. 10 mi/h\nD. 24 mi/h\n? ")
    if question_2.upper() == "D":
        print("Correct!")
        answers_correct += 1
    else:
        print("Incorrect!")
    print()

    # THIRD QUESTION
    question_3 = int(input("What is the vertical asymptote of the equation "
                           "(x-2)/(x+4)? "))
    if question_3 == -4:
        print("Correct!")
        answers_correct += 1
    else:
        print("Incorrect!")
    print()

    # FOURTH QUESTION
    question_4 = int(input("what is the zero for the same equation above? "))
    if question_4 == 2:
        print("Correct!")
        answers_correct += 1
    else:
        print("Incorrect!")
    print()

    # FIFTH QUESTION
    question_5 = input("Am I asking this question because I'm too lazy to think of "
                       "another question (YES/NO)? ")
    if question_5.upper() == "YES":
        print("Correct!")
        answers_correct += 1
    else:
        print("Incorrect!")

    # ENDING CARD THAT TELLS YOUR SCORE
    print()
    print("Wow! You got a " + str((answers_correct / 5) * 100) +
          "% on this quiz!\nThat's better than my spanish grade!")


main(0)
