a,b,total = 0,0,0

a = 7 #int(input('a입력>>>'))
b = 9 #int(input('b입력>>>'))
total  = a+b
print(a,'+',b,'=',total)
print('%d + %d = %d'%(a,b,total) )
print('{} + {} = {}'.format(a,b,total))
print(f'{a} + {b} = {total}')
print()

msg = 1234 
print('|{}|'.format(msg))
print('|{:^10}|'.format(msg)) #|   1234   |  ^중앙맞춤
print('|{:>10}|'.format(msg)) #|      1234|  >오른쪽맞춤
print('|{:<10}|'.format(msg)) #|1234      |  <왼쪽맞춤
print('|{:10}|'.format(9876)) #|      9876|
print()

print('|{:0>10}|'.format(msg)) #  >오른쪽맞춤
print('|{:*>10}|'.format(msg)) #  >오른쪽맞춤
print('|{:,}|'.format(1234567))  #|1,234,567|

# 02print.py
