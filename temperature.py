#encoding:utf-8
fahrenheit = 0
print("华氏 | 摄氏")
while fahrenheit <= 250:
    celsius = (fahrenheit - 32)/1.8 
    print('{:5d}{:7.2f}'.format(fahrenheit , celsius))
    fahrenheit = fahrenheit +25
