a,b = map(int,input().split())
grade = list(map(int, input().split()))
for i in range(b):
    start, end = map(int, input().split())
    print(f'{sum(grade[start-1:end])/(end - start + 1) :.2f}')
print(grade)
