import sys
a = int(input())
stone = list(map(int,input().split()))
stone_list = [1] * a
for i in range(1,a):
    max_stone = 0
    for j in range(i):
        if stone[i] > stone[j]:
            if max_stone< stone_list[j]:
                max_stone = stone_list[j]
    stone_list[i] = max_stone + 1
print(max(stone_list))