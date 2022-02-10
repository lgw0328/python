#입력 : 12

#출력 1투터 12 까지 출력할수있게

a = int(input())

for i in range(1 ,a+1 ) :
    print(i)


a = int(input("첫번쨰 숫자를 입력해주세요"))
b = int(input("두번쨰 숫자를 입력해주세요"))

for i in range(a ,b+1):
    print(i)



a = int(input("첫번쨰 숫자를 입력해주세요"))
b = int(input("두번쨰 숫자를 입력해주세요"))

for i in range(a ,b+1):
    if i % 2  == 0:
        print(i, "=" , "짝수")
    else :
        print(i, "=" , "홀수")
        
a = int(input())

b = 0 #숫자를 더해서 저장하는변수

for i in range(0,a+1):
    b = b + i


print(b)
    



