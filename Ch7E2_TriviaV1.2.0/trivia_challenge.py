# Ch7E2_TriviaV1.2.0

# Ver. 1.2.0:
#               + Add save high score

# Modified by: Jim-Kristian Malmhaug | 5 Feb 2016

# About: Play a Trivia game

import sys
from high_score import high_scores

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)
    
    question = next_line(the_file)

    answers = []
    score_list = []
    for i in range(4):
        answers.append(next_line(the_file))
        try:
            score_list.append(int(next_line(the_file)))
        except:
            break

    explanation = next_line(the_file)

    return category, question, answers, score_list, explanation

def welcome(title):
    """Welcome the player"""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")
 
def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # get first block
    category, question, answers, score_list, explanation = next_block(trivia_file)
    while category:
        # ask a question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # get answer
        answer = input("What's your answer?: ")

        # store score
        score = score + score_list[int(answer)-1]

        print(explanation)

        # get next block
        category, question, answers, score_list, explanation = next_block(trivia_file)

    trivia_file.close()

    print("That was the last question!")
    print("You're final score is", score)

    high_scores(score)
 
main()
input("\n\nPress the enter key to exit.")
