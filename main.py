# 구현 알고리즘
# practice1 -> 상하좌우
# practice2 -> 시각
# practice3 -> 왕실의 나이트
# practice4 -> 게임 개발

N,M = map(int,input().split())
x,y,to = map(int,input().split())

move_type = [0,1,2,3] #북,동,남,서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

board = []
for i in range(N):
  li = list(map(int,input().split()))
  board.append(li)

count = 0
turn = 0

while True:

  if to == 0:
    nx = x + dx[to]
    if board[nx][y] == 1:
      turn += 1
      to = 3
      if turn == 4:
        break
    else:
      x = nx
      count += 1
      board[x - dx[to]][y] = 1
      turn = 0

  elif to == 2:
    nx = x + dx[to]
    if board[nx][y] == 1:
      turn += 1
      to = 1
      if turn == 4:
        break
    else:
      x = nx
      count += 1
      board[x - dx[to]][y] = 1
      turn = 0

  elif to == 1:
    ny = y + dy[to]
    if board[x][ny] == 1:
      turn += 1
      to = 0
      if turn == 4:
        break
    else:
      y = ny
      count += 1
      board[x][y - dy[to]] = 1
      turn = 0

  elif to == 3:
    ny = y + dy[to]
    if board[x][ny] == 1:
      turn += 1
      to = 0
      if turn == 2:
        break
    else:
      y = ny
      count += 1
      board[x][y - dy[to]] = 1
      turn = 0
  
print(count)