# 왕실의 나이트
# 나이트가 움직일 수 있는 경우의 수를 세는 문제.

# ord('a')=97

# solution1
loc = input()
M = loc[0]
N = loc[1]

dx = [2,2,-2,-2,1,1,-1,-1]
dy = [1,-1,1,-1,2,-2,2,-2]

count = 0

for i in range(8):
  if ord(M)+dx >= 97 and int(N)+dy >= 1:
    count += 1

print(count)