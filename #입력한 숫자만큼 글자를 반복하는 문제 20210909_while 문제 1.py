#입력한 숫자만큼 글자를 반복해서 출력
a = 0
b = 0

while a<b:
    print("반복문")
    a +=1 

a = int(input())
b =0
while b<a:
    print("반복문")
    b+=1;
    
a = int(input())
b = 1
while b<=a:
   print(b)
   b+=1;
    
a = int(input())
b = 0
while b<a:
    print(a)
    a-=1
    
a=1
while a<=100:
    if a % 3 == 0 and a % 8 == 0 :
        print(a)
    a+=1
