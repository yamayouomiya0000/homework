import random as rd

'''
重複のない(178のように各桁の数字が被らない)任意の桁数の数字について,数字を推測するHit and Blowゲーム
数字と場所が当たっている数を「Hit」。数字は当たっているが場所が当たってない数を「Blow」で示す。
例）答えが178のとき,871と推測すると,1 Hit 2 Blow
    7は数字と場所があっているため1 Hit,1と8は数字はあっているが場所があっていないため2 Blow
'''

def createNumber_nodup(digit): #重複のない任意の桁数の整数を生成する関数
    number_list = [rd.randint(1,9)]   
    number_nodup = 0

    while True:
        randval = rd.randint(0,9)

        if randval not in number_list:             
            number_list.append(randval)   

        if len(number_list) == digit:   
            break                  

    for i in range(1,digit + 1):
        number_nodup += number_list[i-1] * (10 ** (digit - i))
                
    return number_nodup

def hitAndBlow(answer,number,digit):   #HitとBlowの数を表示する関数
    hit = 0
    blow = 0
    number_list = []
    answer_list = []

    for i in range(1,digit+1):  #整数の各桁をlistに代入する
        number_list.append(number % 10)
        number = number // 10

        answer_list.append(answer % 10)
        answer = answer // 10
    
    for i in range(1,digit + 1):
        for j in range(1,digit + 1):
            if number_list[i-1] == answer_list[i-1]:
                hit += 1
                break
            elif number_list[i-1] == answer_list[j-1]:
                blow += 1
                break
    
    print(hit,' Hit ',blow,' Blow ')

#メインの処理

while True:     #桁数を指定する，2~10以外の桁数が入力された場合は次の処理に行かないようにした
        print('何桁の数字当てゲームに挑戦しますか？(2~10桁まで)')
        digit = int(input())
        if not (digit >= 2 and digit <= 10):
            print('無効な入力です,2~10までの数字を入力してください')
        else:
            break
        
ans = createNumber_nodup(digit)     #正解の数字を生成
max_count = 10                      #回答回数の指定

print(digit,'桁の数字を当ててください')
print('回答は',max_count,'回までです')

for i in range(1,max_count + 1):

    while True:     #数字の入力,桁数の違う数字が入力された場合は次の処理に行かない
        print(i,'回目の回答です')
        num = int(input())

        if not (num >= 10 ** (digit - 1) and num <= 10 ** digit - 1):
            print('無効な入力です,',digit,'桁の数字を入力してください')
        else:
            break

    if num == ans:    #正解した場合と回答回数を使い切った場合，for文の処理終了，不正解の場合Hit and Blowの表示
        print('正解です')
        break
    elif i == max_count:
        print('不正解です')
    else:
        hitAndBlow(ans,num,digit)       

else:
    print('正解は',ans,"でした")

