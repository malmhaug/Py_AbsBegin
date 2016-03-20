# File: purse.py
# Version: 1.2.0 | Betting added
# About: Purse for betting
# Modified: 20 March 2016 | Jim-Kristian Malmhaug


class Purse(object):
    def __init__(self):
        self.money = 0

    def bet_money(self, money_output):
        self.money -= money_output

    def win_money(self, money_input):
        self.money += money_input
        return self.money


class TableMoney(object):
    def __init__(self):
        self.table_money = 0

    def reset_table(self):
        self.table_money = 0
        print("Table money: ", self.table_money)

    def add_money(self, amount):
        self.table_money += amount
        print("Table money: ", self.table_money)
