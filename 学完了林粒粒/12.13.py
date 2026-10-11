f=open("./poem.txt","r",encoding="utf-8")
result=f.read()
print(result)
f.close()

with open("./poem.txt","r",encoding="utf-8") as f:
    result=f.read()
    print(result)
f.close()

with open("./poem.txt","r",encoding="utf-8") as f:
    print(f.readline())
    print(f.readline())

with open("./poem.txt","r",encoding="utf-8") as f:
    lines=f.readlines()
    for line in lines:
        print(line)

with open("./poem.txt","r+",encoding="utf-8") as f:
    f.write("hello world")
    f.write("you are right ")

with open("./poem1.txt","w",encoding="utf-8") as f:
    f.write("我欲乘风归去，\n又恐琼楼玉宇，\n高处不胜寒。\n")

with open("./poem1.txt","a",encoding="utf-8") as f:
    f.write("起舞弄清影，\n何似在人间。\n")

#异常处理
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

def calculate_and_print(num):
    result=num * num
    print(f"""
| 数字参数 |{num} |
|计算结果 |{result} |""")

calculate_and_print(3)

#测试
assert
#匿名
lambda