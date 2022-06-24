import random

ans = random.randint(100,999)
max_count = 5

print('3桁の数字を当ててください')
print('回答は',max_count,'回までです')

for i in range(1,max_count+1):
    while True:
        print(i,'回目の回答です')
        num = int(input())
        if not num>=100 and num<=999:
            print('無効な入力です,3桁の数字を入力してください')
        else:
            break


    if num==ans:
        print('正解です')
        break
    elif i==max_count:
        print('不正解です')
    elif num>ans:
        print('不正解です．もっと小さい数字です')
    elif num<ans:
        print('不正解です．もっと大きい数字です')        

else:
    print('正解は',ans,"でした")

