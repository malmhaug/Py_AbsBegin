import sys

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

def high_scores(score):
    name = input("\nEnter your name --> ")

    score_file = open_file("high_scores.txt", "r")
    lines = score_file.readlines()
    score_file.close()

    score_file = open_file("high_scores.txt", "a")

    if len(lines) < 1:
        score_file.write(name + ':' + str(score) + '\n')

    for entry in lines:
        if name.lower() in entry:
            score_file.write(name + ':' + str(score) + '\n')
            break
        if name.lower() not in entry:
            score_file.write(name + ':' + str(score) + '\n')
            break

    score_file.close()


if __name__ == '__main__':
    high_scores(14)
