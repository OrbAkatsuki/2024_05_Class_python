#內建的變數__name__

import pyinputplus as pypi


def cal_bmi(cm:int, kg:int):
    bmi = kg / (cm/100) ** 2
    return bmi
def get_status(bmi:float):
    if bmi >= 35:
        result = "重度肥胖"
    elif bmi >= 30:
        result = "中度肥胖"
    elif bmi >= 27:
        result = "輕度肥胖"
    elif bmi >= 24:
        result = "過重"
    elif bmi >= 18.5:
        result = "正常"
    else:
        result = "過輕"
    return result
def main():
    name = pypi.inputStr("請輸入您的姓名: ")
    print(name)
    cm = pypi.inputInt("請輸入您的身高(cm): ",min=0,max=300)
    print(cm)
    kg = pypi.inputInt("請輸入您的體重(kg): ",min=0,max=300)
    print(kg)
    bmi = cal_bmi(cm=cm, kg=kg)
    result = get_status(bmi=bmi)
    print(f"您的姓名是: {name}")
    print(f"您的BMI值: {round(bmi,ndigits=0)}")
    print(f"您的體重: {result}")

if __name__ == '__main__':
    '''
    print("我是被python執行的主程式")
    print(__name__)
    print(type(__name__))
    '''
    main()