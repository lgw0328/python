0#반복문
for i in range(1 ,15, -1):
    print(i) 
#첫번째 문제
#1부터 100까지 2의 배수만 출력
#for문을 이용해서

for i in range(0 ,101, 2):
    print(i)

for i in range(101 ,0 ,-2):
    print(i)

for i in range(2050 ,2002 ,-4):
    print(i)

a = int(input())

for i in range(1, 10):
    print(a,"*",i, "=", a*i)


for i in range(1 , 10):
    if 3 == i or 6 == i or 9 == i :
        print("짝")
    else :
        print(i)
