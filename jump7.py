#encoding:utf-8

#print('从1到100，打印不是7的倍数、且不含7的数字：')

for num in range(1,101):
    if num % 7 == 0 or num % 10 == 7 or num //10 == 7:
        continue
    print(num)
