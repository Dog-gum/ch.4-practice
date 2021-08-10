# 시각
# 1. 00시 00분 00초 ~ N시 59분 59초 까지 3이 하나라도 포함되는 경우의 수 출력 프로그램.

# solution1

N = int(input())

# 초단위 3 포함된 횟수
s = 6+10-1

# 분단위 3포함된 횟수
m = (60-s)*s + s*60

# 시간단위 3포함된 횟수
if N < 3:
  h = (N+1)*m
elif 13 > N > 2:
  h = (N)*m + 1*3600
elif 23 > N > 12:
  h = (N-1)*m + 2*3600
else:
  h = (N-2)*m + 3*3600

print(h)

#############################################

# solution2
N = int(input())

count = 0
for h in range(N+1):
  for m in range(60):
    for s in range(60):
      if '3' in str(h) + str(m) + str(s):
        count+=1

print(count)

# 문자열일부에 해당 숫자가 포함되어 있는지 확인하는 방법. if '숫자' in str(a)+str(b)