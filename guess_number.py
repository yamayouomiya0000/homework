import random

ans = random.randint(100,999)
max_count = 5

print('3桁の数字を当ててください')
print('回答は',max_count,'回までです')

for i in range(1,max_count+1):
    print(i,"回目の回答です")
    num = int(input())
    if num==ans:
        print("正解です")
        break
    else:
        print("不正解です")
else:
    print('正解は',ans,"でした")

