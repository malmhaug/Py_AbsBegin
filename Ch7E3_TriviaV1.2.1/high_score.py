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
    new_lines = []
    no_name = 0

    name = input("\nEnter your name --> ")

    score_file = open_file("high_scores.txt", "r")
    lines = score_file.readlines()
    score_file.close()

    # If file is empty, write name and score
    if len(lines) < 1:
        print("Empty file")
        new_lines.append(str(score) + ':' + name + '\n')

    # Transfer from lines to new_lines
    for entry in lines:
        new_lines.append(entry)

    # Check for new names
    for entry in range(len(new_lines)):
        if new_lines[entry].find(name) == -1:
            no_name += 1
    if no_name >= len(new_lines):
        print("New name")
        new_lines.append(str(score) + ':' + name + '\n')

    # Check score for names already in list
    for entry in range(len(new_lines)):
        position = new_lines[entry].find(':')
        old_score = int(new_lines[entry][:position])
        if name.lower() in new_lines[entry] and old_score < score:
            print("New score for person in list")
            new_lines[entry] = str(score) + ':' + name + '\n'

    # Sort list
    new_lines.sort(reverse=True)

    print("HIGH SCORE\n")
    for entry in new_lines:
        print(entry)

    score_file = open_file("high_scores.txt", "w")
    score_file.writelines(new_lines)
    score_file.close()

if __name__ == '__main__':
    high_scores(16)
