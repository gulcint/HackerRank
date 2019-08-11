
"""Task 
Given n names and phone numbers, assemble a phone book that maps friends' 
names to their respective phone numbers. You will then be given an unknown 
number of names to query your phone book for. For each name queried, print 
the associated entry from your phone book on a new line in the form name=phoneNumber;
if an entry for name is not found, print Not found instead.
Note: Your phone book should be a Dictionary/Map/HashMap data structure.
 
"""

"""
#this code give test case 1 error.

n = int(input())
dic = {}

for i in range(n):
    x,y= input().split()
    dic[x] = y

for i in range(n):
    name = input()
    if(name in dic.keys()):
        print(name + '='+ str(dic[name]))
    else :
        print('Not found')
      
"""

# 2nd code is work for all cases.

num = int(input())

phone_book = {}

for i in range(0, num):
    entry = str(input()).split(" ")

    name = entry[0]
    phone = int(entry[1])
    phone_book[name] = phone

for j in range(0, num):
    name = str(input())

    if name in phone_book:
        phone = phone_book[name]
        print(name + "=" + str(phone))
    else:
        print("Not found")
