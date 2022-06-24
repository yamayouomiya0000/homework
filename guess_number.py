import random as rd

def createNumber_nodup(digit):
    number_list = [rd.randint(1,9)]   
    number_nodup = 0

    while True:
        randval = rd.randint(0,9)

        if randval not in number_list :             
            number_list.append(randval)   

        if len(number_list) == digit :   
            break                  

    for i in range(1,digit+1):
        number_nodup += number_list[i-1]*(10**(digit-i))
                
    print('数字',number_nodup)
    return number_nodup

def hitAndBlow(ans,number,digit):
    hit = 0
    blow = 0
    number_list = []
    answer_list = []

    for i in range(1,digit+1):
        number_list.append(number % 10)
        number = number // 10

        answer_list.append(ans % 10)
        ans = ans //10
    
    for i in range(1,digit+1):
        for j in range(1,digit+1):
            if number_list[i-1] == answer_list[i-1]:
                hit += 1
                break
            elif number_list[i-1] == answer_list[j-1]:
                blow += 1
                break
    
    print(hit,' Hit ',blow,' Blow ')

           
                

while True:
        print('何桁の数字当てゲームに挑戦しますか？(2~10桁まで)')
        digit = int(input())
        if not (digit>=1 and digit<=10):
            print('無効な入力です,0~10までの数字を入力してください')
        else:
            break
        
ans = createNumber_nodup(digit)
max_count = 10

print(digit,'桁の数字を当ててください')
print('回答は',max_count,'回までです')

for i in range(1,max_count+1):
    while True:
        print(i,'回目の回答です')
        num = int(input())

        if not (num>=10**(digit-1) and num<=10**digit-1):
            print('無効な入力です,',digit,'桁の数字を入力してください')
        else:
            break

    if num==ans:
        print('正解です')
        break
    elif i==max_count:
        print('不正解です')
    else:
        hitAndBlow(ans, num, digit)       

else:
    print('正解は',ans,"でした")

