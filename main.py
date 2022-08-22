import sys
def valid(i, j, arr):
    if len(arr[i]) != len(set(arr[i])):
        return 0
    vertical_arr = []
    for k in range(9):
        vertical_arr.append(arr[k][j])
    if len(vertical_arr) != len(set(vertical_arr)):
        return 0
    return 1


def main () :
    arr = [list(map(int, input().split())) for _ in range(9)]
    i = 0
    while i < 9:
        for j in range(9):
            if arr[i][j] == 0:
                arr[i][j] = 1
                while valid(i, j, arr) == 0:
                    arr[i][j] = arr[i][j] + 1
        i = i + 1;
    for i in arr:
        for j in i:
            print(j, end=' ')
        print("\n", end='')

main()