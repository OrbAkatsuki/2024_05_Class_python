import pyinputplus as pypi
import health

def main():
    name = pypi.inputStr("請輸入您的姓名: ")
    print(name)
    cm = pypi.inputInt("請輸入您的身高(cm): ",min=0,max=300)
    print(cm)
    kg = pypi.inputInt("請輸入您的體重(kg): ",min=0,max=300)
    print(kg)
    bmi = health.cal_bmi(cm=cm, kg=kg)
    result = health.get_status(bmi=bmi)
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