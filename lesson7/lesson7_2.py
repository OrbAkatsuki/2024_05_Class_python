import random
import pyinputplus as pypi

while(True)
    min:int = 1
    max:int = 100
    count:int = 0
    # :int 是提示type是整數
    target:int = random.randint(min,max)
    print("=============猜數字遊戲=============\n")
    while(True):
        keyin = pypi.inputInt(f"猜數字範圍{min}~{max} : ",min = min,max = max)
        print(keyin)
        count += 1
        if keyin == target:
            print(f"BINGO！你猜對了，答案是:{keyin}")
            print(f"您總共猜了 {count} 次")
            break
        elif (keyin > target):
            print(f"比 {keyin} 再小一點")
            max = keyin - 1
        elif (keyin < target):
            print(f"比 {keyin} 再大一點")
            min = keyin + 1
        print(f"您已經猜了 {count} 次")
    paly_again = pypi.inputYesNo("請問還要繼續嗎?(y,n)")
    if paly_again == "no":
        break

print("遊戲結束")