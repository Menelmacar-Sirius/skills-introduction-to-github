class FavouriteFruit:
    def __init__(self):
        self.name="blueberry"
        self.category="berry"
        self.colour="blue"
        self.taste="a bit sour and a bit sweet"
        self.price="100元/kg"
fruit1=FavouriteFruit()
print(fruit1.colour)

class FavouriteFootballPlayer:
    def __init__(self,player_name,player_age,player_weight,player_height,player_nationality):
        self.name=player_name
        self.age=player_age
        self.weight=player_weight
        self.height=player_height
        self.nationality=player_nationality
    def say_info(self):
        print(f"球员{self.name}的年龄是{self.age},他的身高是{self.height}m，体重是{self.weight}kg，他出身的国家是{self.nationality}")
    def introduce_and_speak(self):
        self.say_info()
        print("i hate you")
    def think(self,content):
        print(f"球员{self.name}在思考{content}")
player1=FavouriteFootballPlayer("kevin",34,78,1.81,"比利时")
player1.introduce_and_speak()
player1.think("我到底该怎么办")

# 定义一个学生类
# 要求：
# 1. 属性包括学生姓名、学号，以及语数英三科的成绩
# 2. 能够设置学生某科目的成绩
# 3. 能够打印出该学生的所有科目成绩
class Student:
    def __init__(self,name,student_id):
        self.name=name
        self.student_id=student_id
        self.grades={"语文":0,"数学":0,"英语":0,"物理":0,"化学":0,"生物":0}

    def set_grade(self,category,grade):
        if category in self.grades:
            self.grades[category]=grade
    def print_grade(self):
        print(f"学生{self.name}(学号{self.student_id})的成绩为：")
        for category in self.grades:
            print(f"{category}:{self.grades[category]}分")
chen=Student("陈陈","114514")
chen.set_grade("化学",56)
chen.set_grade("生物",91)
chen.set_grade("英语",77)
chen.print_grade()


#类继承练习: 人力系统
# - 员工分为两类:全职员工 FullTimeEmployee、兼职员工 PartTimeEmployee。
# - 全职和兼职都有"姓名 name"、”工号 id"属性,
# 都具备"打印信息 print_info"(打印姓名、工号)方法。
#- 全职有"月薪 monthly_salary"属性,
#兼职有"日薪 daily_salary"属性、"每月工作天数 work_days"的属性。
#- 全职和兼职都有”计算月薪 calculate_monthly_pay"的方法,但具体计算过程不一样。
class Employee:
    def __init__(self,name,employee_id):
        self.name=name
        self.employee_id=employee_id
    def print_employee(self):
        print(f"员工姓名：{self.name}，{self.employee_id}")
class FullTimeEmployee(Employee):
    def __init__(self,name,employee_id,monthly_salary):
        super().__init__(name,employee_id)
        self.monthly_salary=monthly_salary

    def calculate_monthly_pay(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self,name,employee_id,daily_salary,work_days):
        super().__init__(name,employee_id)
        self.work_days=work_days
        self.daily_salary=daily_salary

    def calculate_monthly_pay(self):
        return self.daily_salary*self.work_days

zhang=FullTimeEmployee("zhang",325,9000)
li=PartTimeEmployee("li",7890,135,27)
zhang.print_employee()
li.print_employee()
print(zhang.calculate_monthly_pay())
print(li.calculate_monthly_pay())


class Fruit:
    def __init__(self,taste):
        self.taste=taste
    def show(self):
        print(f"这是{self.taste}的水果")
class Apple(Fruit):
    def __init__(self,taste,colour):
        super().__init__(taste)
        self.colour=colour
    def show_colour(self):
        print(f"这是{self.colour}的！")
my_apple=Apple(taste="sweet",colour="red")
my_apple.show()
my_apple.show_colour()

# 第一根线：父类
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def start(self):
        return f"{self.brand}启动了！"

# 第二根线：子类（继承）
class Car(Vehicle):
    def honk(self):
        return "嘀嘀！"

# 第三根线：造车 + 使用
my_car = Car("比亚迪")
log_content = my_car.start() + "\n" + my_car.honk()

# 第四根线：写入文件
with open("car_log.txt", "w", encoding="utf-8") as f:
    f.write(log_content)

print("✅ 日志已保存到 car_log.txt")

class Animal:
    def __init__(self,name,species,color):
        self.name=name
        self.species=species
        self.color=color
    def say_info(self):
        return f"{self.name}是{self.species}的{self.color}"
class Dog(Animal):
    def bark(self):
        return f"汪汪，我是{self.name}"
my_dog=Dog("小白","柯基","黄色")

# 4. 准备日志内容（三行）
log = (
    my_dog.say_info() + "\n" +
    my_dog.bark() + "\n" +
    "✅ 今日就诊完成"
)

# 5. 写入文件 pet_visit.txt
# 您来写 with open(...) 部分！
with open("pet_visit.txt", "w", encoding="utf-8") as f:
    f.write(log)

print("✅ 就诊日志已保存！")




















