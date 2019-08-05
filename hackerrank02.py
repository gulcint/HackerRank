if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    # i convert map to list  for used list's functions.
    arr= list(arr)

    # i found max item and it's count
    max_i = max(arr)
    count_i = arr.count(max_i)

    # i removed max_item
    for i in  range(count_i):
        arr.remove(max_i)

    # now second item is max_item in the list.
    max_item = max(arr)
    print(max_item)