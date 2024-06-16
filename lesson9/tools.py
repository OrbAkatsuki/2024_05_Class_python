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