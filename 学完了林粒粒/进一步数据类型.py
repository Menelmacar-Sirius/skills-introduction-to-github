from 初识数据类型 import use_height

is_happy=True
if is_happy:
    print("happy")
else:
    print("bad")

3!=4
5==5
5==6

#这是第一种，用str转换int.ds说不对，输入的是字符串，但直接与数字字符串比较会导致字典序比较而非数值比较
today_learning_process=input("今日进步指数")
if today_learning_process<"60":
    print("今天学习成果不及格")
elif"60"<today_learning_process<"80":
    print("还不错")
elif "80"<today_learning_process<"95":
    print("很不错了")
elif "95"<today_learning_process<"100":
    print("你是最棒的")
    print("加油，再接再厉")

#这是第二种，用int函数将str转换
today_learning_process=int(input("今日进步指数"))
if today_learning_process<=60:
    print("不过关")
else:
    print("可以算过关了")
    print("再接再厉")

#else后面什么都不用加，只有冒号
if "明天会下雨":
    if "温度低":
        print("穿棉袄")#问题在于：字符串 "明天会下雨" 和 "温度低" 作为条件永远为 True，所以代码会一直执行第一个分支。
    else:
        print("穿大衣")
else:
        print("穿长袖")

# 假设我们通过某些方式获取天气信息，deepseek给出的答案
will_rain = True  # 明天下雨
is_cold = False   # 温度不低

if will_rain:
    if is_cold:
        print("穿棉袄")
    else:
        print("穿大衣")
else:
    print("穿长袖")

#用布尔值构建
a=int(input("下雨指数"))
b=int(input("空气湿度"))
if a<=40:
    if b<=20:
        print('可以晾衣服')
    else:
        print('不可以晾衣服')
#bmi=weight/(height**2)
user_weight=float(input("请输入您的体重"))
user_height=float(input("请输入您的身高"))
user_bmi=user_weight/(user_height**2)
print("您的bmi指数为  "+str(user_bmi))
# 偏瘦:18.5 <user_BMI <= 25
# 偏胖:25 <user_BMI <= 30
# 肥胖:user_BMI > 30
if user_bmi<= 18.5:
    print("此BMI值属于偏瘦范围")
elif 18.5 < user_bmi<= 25:
    print("此BMI值属于正常范围")
elif 25 < user_bmi<= 30:
    print("此BMI值属于偏胖范围")
else:
    print("此BMI值属于肥胖范围")


# bmi=weight/(height**2)
try:
    user_weight = float(input("请输入您的体重"))
    user_height = float(input("请输入您的身高"))
    user_bmi = user_weight /(user_height ** 2)
except ValueError:
    print("输入不为合理数字,请重新运行程序,并输入正确的数字。")
except ZeroDivisionError:
    print("身高不能为零,请重新运行程序,并输入正确的数字。")
except:
    print("发生了未知错误,请重新运行程序。")
else:
    print("您的BMI值为:" + str(user_bmi))
finally:
    print("程序结束运行。")
# 偏瘦:user_BMI <= 18.5
# 正常:18.5 < user_BMI <= 25
# 偏胖:25 < user_BMI <= 30
# 肥胖:user_BMI > 30
if user_bmi <= 18.5:
    print("此BMI值属于偏瘦范围")
elif 18.5 < user_bmi <= 25:
    print("此BMI值属于正常范围")
elif 25 < user_bmi <= 30:
    print("此BMI值属于偏胖范围")
else:
    print("此BMI值属于肥胖范围")

math=float(input("数学成绩"))
chinese=float((input("语文成绩"))
english=float(input("英语成绩"))
if (math>=90 and chinese>=120 and english>=120):
    print("have a good day")
else:
    print("not a good day")

math=float(input("数学成绩"))
chinese=float(input("语文成绩"))
english=float(input("英语成绩"))
if math>=90 and chinese>=120 and english>=120:
    print("have a good day")
else:
    print("not a good day")