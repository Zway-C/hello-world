# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


noun = ('cat', 'house', 'table','desk')
verb = ('kick', 'jump', 'sleep')

word = input("please type a word: ")



while word in noun:
    print ("noun")

while word in verb:
    print ("verb")

def distinquish():
    if input not in noun or verb:
        return ("please type a new word")

print(distinquish())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
