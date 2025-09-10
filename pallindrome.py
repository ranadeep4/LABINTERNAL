def pallindrome(num):
    temp = num
    rev = 0
    while(temp>0):
        rem = temp % 10
        rev = (rev * 10) + rem
        temp = temp // 10
    return num == rev
print(pallindrome(121)) 
print(pallindrome(123))