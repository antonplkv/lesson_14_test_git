# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Factory:

    def __init__(self):
        print('Hello')
        print('Goodbye')


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.


def say_goodbye(name):
    print(f'Bye, {name}')
# Press the green button in the gutter to run the script.


def super_useful_function(*input_data):
    for i in input_data:
        yield i


if __name__ == '__main__':
    print_hi('PyCharm')
    say_goodbye('Max')
    print('Hi')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
