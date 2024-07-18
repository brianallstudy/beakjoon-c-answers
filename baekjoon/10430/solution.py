// [문제 링크]: https://www.acmicpc.net/problem/10430

A, B, C = input().split()
x = int(A)
y = int(B)
z = int(C)
print((x+y)%z)
print(((x%z)+(y%z))%z)
print((x*y)%z)
print(((x%z)*(y%z))%z)