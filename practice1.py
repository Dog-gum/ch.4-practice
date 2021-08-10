# 상하좌우
# 1. 공간의 크기 N이 주어진다.(N*N크기)
# 2. R,L,U,D 공간을 이동한다.
# 3. 입력된 이동 방향을 토대로 최종 목적지 출력.
# 4. 단, 공간에서 벗어나는 이동은 무시.

# solution-1
N = map(int,input().split())
todo = list(map(str, input().split()))

x = 1
y = 1 

for i in todo:
  if i == 'R':
    y += 1
    if x <= 0:
      x += 1
    elif y <= 0 :
      y+= 1
  elif i == 'L':
    y -= 1
    if x <= 0:
      x += 1
    elif y <= 0 :
      y+= 1
  elif i == 'U':
    x -= 1
    if x <= 0:
      x += 1
    elif y <= 0 :
      y+= 1
  elif i == 'D':
    x += 1
    if x <= 0:
      x += 1
    elif y <= 0 :
      y+= 1
  
print(x,y)
# ->solution1 의 문제점 : 1. 불필요하게 반복되는 코드가 많다. 2. x or y > N 인 경우를 고려X.

###################################################################33

# solution-2

N = map(int,input().split())
todo = list(map(str, input().split()))

x = 1
y = 1

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_type = ['L','R','U','D']

for do in todo:
  # 이동
  for i in range(move_type):
    if do == move_type[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  # 벗어나면 무시
  if nx <= 0 or ny <= 0 or ny > N or nx > N:
    continue
  # 무시 안 당하면 위치 이동
  x = nx
  y = ny

print(x,y)
