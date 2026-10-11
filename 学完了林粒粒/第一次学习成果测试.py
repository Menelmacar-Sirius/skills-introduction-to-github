shopping_list=["苹果","牛奶","面包"]
shopping_list.append("鸡蛋")
print(f"今天要买{shopping_list}")
###AI给的答案
shopping_list = ["苹果", "牛奶", "面包"]
if "鸡蛋" not in shopping_list:  # ← 更聪明：先检查有没有
    shopping_list.append("鸡蛋")
# 用 “、” 把所有东西连起来
items = "、".join(shopping_list)
print(f"今天要买：{items}")

students = {
    "小明": {"语文": 85, "数学": 90, "英语": 78},
    "小红": {"语文": 92, "数学": 88, "英语": 85},
    "小刚": {"语文": 70, "数学": 95, "英语": 80}
}#字典的嵌套{}

highest_score = 0
top_student = ""#找最高分 —— “记账法”

for name, grades in students.items():#.items() —— 把字典“一页页翻开
    total = sum(grades.values())#求和，只要分数，不要名字
    print(f"{name}的总分是：{total}")
    if total > highest_score:
        highest_score = total
        top_student = name

print(f"最高分是{top_student}，得了{highest_score}分！")

bills={"January":{"水费":30,"电费":80,"燃气费":45},
       "February":{"水费":28,"电费":85,"燃气费":50},
       "March":{"水费":35,"电费":90,"燃气费":40},}
highest_total = 0
highest_month = ""
for month,costs in bills.items():
    total=sum(costs.values())
    if total > highest_total:
        highest_total = total
        highest_month = month
print(f"{highest_month}是花销最大的月份，花了{highest_total}")

def send_blessing(name,relation):
    if relation=="grandma":
        print(f"{name},新年快乐！福如东海！")
    elif relation=="friends":
        print(f"{name},新年快乐！万事如意！")
    else:
        print(f"{name}，新年快乐!")
send_blessing("李奶奶", "奶奶")
send_blessing("小美", "小孙女")
send_blessing("张阿姨", "邻居")

def suggest_clothes(temp, person):
    if temp<10:
        print(f"{person},今天冷,记得多加件羽绒服")
    elif temp>20:
        print(f"{person},今天天气暖和。穿件衬衫就好了")
    else:
        print(f"{person},今天天气一般，多加件外套吧")
suggest_clothes(5, "小孙女")
suggest_clothes(15, "老伴")
suggest_clothes(25, "邻居王叔")

class Pet:
    def __init__(self,name,species,age,colour):
        self.name = name
        self.age = age
        self.colour = colour
        self.species = species
    def action(self):
        if self.species=="狗狗":
            print("shout!")
        elif self.species=="猫猫":
            print("run")
        else:
            print("哼!")
    def introduce(self):
            print(f"我是{self.age}岁的{self.colour}色{self.name}")

wangcai=Pet("旺财","狗狗",7,"黑")
mimi=Pet("咪咪","猫猫",3,"白")
wangcai.action()
mimi.action()
wangcai.introduce()

class Fruit:
    def __init__(self,name,taste,colour):
        self.name = name
        self.taste = taste
        self.colour = colour
    def describe(self):
        print(f"我是{self.colour}的{self.name},味道很{self.taste}")
    def is_delicious(self):
        if self.taste=="sweet"or self.taste=="delicious":
            print("真好吃")
        else:
            print("not good")
apple=Fruit("苹果","sour","红色")
banana=Fruit("香蕉","sweet","黄色")
apple.describe()
banana.is_delicious()