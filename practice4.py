# 게임 개발


# solution1

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
while True:
  if to == 0 or 2:
    nx = x + dx[to]
    if board[nx][y] == 1:
      continue
    else:
      x = nx
      count += 1
      board[x - dx[to]][y] = 1
  elif to == 1 or 3:
    ny = y + dy[to]
    if board[x][ny] == 1:
      continue
    else:
      y = ny
      count += 1
      board[x][y - dy[to]] = 1
  elif board[x-1][y-1]==1 and board[x+1][y-1]==1 and board[x-1][y+1]==1 and board[x+1][y+1]==1:
    break

print(count)