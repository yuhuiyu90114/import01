import random
start = input ('請輸入猜測範圍起始值:')
end = input ('請輸入猜測範圍結束值:')
start = int (start)
end = int (end)
pwd = random.randint(start,end)
count = 0
while True:
    num = input ('請猜數字:')
    num = int (num)
    count += 1
    if num == pwd:
        print('猜對了!')
        print('這是第{}次'.format(count))
        break
    elif num > pwd :
        print ('比答案大')
    else:
        print ('比答案小')
    print('這是第{}次'.format(count))