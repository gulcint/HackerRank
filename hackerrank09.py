'''
Task 
Output the symmetric difference integers in ascending order, one per line.
Sample Input
4
2 4 5 9
4
2 4 11 12
Sample Output
5
9
11
12
'''




M = int(input())
numbersM = input()
list_m = numbersM.split()
new_listM = list(map(int,list_m))

N = int(input())
numbersN = input()
list_n = numbersN.split()
new_listN = list(map(int,list_n))

result = []
for i in range(M):
    if(new_listN.count(new_listM[i]) == 0):
        result.append(new_listM[i])

for i in range(N):
    if(new_listM.count(new_listN[i]) == 0):
        result.append(new_listN[i])

result.sort()

for i in result:
    print(i)