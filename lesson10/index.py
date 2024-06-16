import tools
from tools import Student

def main():
    print(tools.PI)
    s1:Student = tools.get_student(name="廖唯善",chinese=89,english=99,math=87,franch=68)
    print(f'name={s1.name}')
    print(f'chinese={s1.chinese}')
    print(f'english={s1.english}')
    print(f'math={s1.math}')
    print(f'franch={s1.franch}')
    print(f'平均={s1.average()}')
    print(f"總分={s1.sum()}")

if __name__ == "__main__":
    main()