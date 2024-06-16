#常數必須要用大寫的
PI = 3.1415926

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


#父類別
class __Person():
    def __init__(self,n):
        self.name = n
    def __repr__(self) -> str:
        return f'學生姓名: {self.name}'

#繼承 (子類別)
class Student(__Person):
    def __init__(self, n:str,ch:int,en:int,ma:int,fn:int):
        super().__init__(n)
        self.__chinese = ch
        self.__english = en
        self.__math =ma
        self.__franch =fn

    #繼承-只能傳出值，不可以更改的property(屬性)  只能讀不能寫
    @property
    def chinese(self) -> int:
        return self.__chinese
    @property
    def english(self) -> int:
        return self.__english
    @property
    def math(self) -> int:
        return self.__math
    @property
    def franch(self) -> int:
        return self.__franch
    def __repr__(self) -> str:
        message:str = super().__repr__()
        message += "\n※學期考試成績如下"
        return message
    def sum(self) -> int:
        return self.chinese + self.english + self.math + self.franch
    
    def average(self) -> float:
        return round(self.sum() / 4.0, ndigits=2)
    

def get_student(name:str, chinese:int, english:int, math:int ,franch:int):
    return Student(n=name,ch=chinese,en=english,ma=math,fn=franch)    