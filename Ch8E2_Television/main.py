# File: main.py
# About: Television, a program which simulates a television
# Version 1.0.0
# By: Jim-Kristian Malmhaug | 02.03.2016

from television import Television

def main():
    tv = Television()
    option = -1

    while option != 0:
        print("""

                1. Raise volume
                2. Lower volume
                3. Switch channel - up
                4. Switch channel - down
                5. Specify channel

                0. Exit
        """)
        option = int(input("---> "))

        if option == 1:
            tv.raise_volume()
        if option == 2:
            tv.lower_volume()
        if option == 3:
            tv.switch_channel_up()
        if option == 4:
            tv.switch_channel_down()
        if option == 5:
            tv.specify_channel()


main()
input("\nPress enter...")
