""" hackerrank  30 Days of code. Day 6 : Let's  Review"""

N = int(input())

for i in range(0, N):

    string = input()

    for j in range(0, len(string)):
        if j % 2 == 0:
            print(string[j], end='')

    print(" ", end='')

    for j in range(0, len(string)):
            if j % 2 != 0:
                print(string[j], end='')
    print("")

