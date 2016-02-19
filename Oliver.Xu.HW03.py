#Oliver Xu
#ox207
#Homework 
#Question 2
def main2(num):
    decimal_num = num
    if num > 1:
       main2(num//2)
    print(num % 2,end = '')

#Question 3
def main3(hexa_lst):
    string = ""
    hexa_lst = list(hexa_lst)
    for i in range(0, len(hexa_lst)):
        dec = int(hexa_lst[i])
        char = chr(dec)
        string = string + char
    return string

#Question 4

def main4(binary):
    binary_num = binary
    decimal_num = int(binary_num,2)
    hexa_num = hex(decimal_num)
    return hexa_num

#Question 5
def main5(num):
    octa_num = str(num)
    decimal_num = 0
    total_num = -1
    for i in (octa_num):
        total_num += 1
    for i in (octa_num):
        decimal_num = (8**total_num) * int(i) + decimal_num
        total_num = total_num - 1
    return decimal_num
