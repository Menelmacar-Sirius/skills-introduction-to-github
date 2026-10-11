score_list=[78.9,99.5,34.6,53.8,23.9,66.2]
for score in score_list:
    if score <60:
        print(score)
        print("完蛋了")
    else:
        print(score)
        print("算你好运")

score_dic={"张三":78.9,"李四":99.5,"王五":34.6,"赵七":53.8,"孙六":23.9,"宋八":66.2}
for key,value in score_dic.items():
    if value<60:
        print(key)

total=0
for i in range (1,101):
    total=total+i
    print(total)

print("我是一个求和程序")#直到输入0为止，计算所输数字总和
total=0
user_input=input("请用户输入一系列数字,(直到输入0为止，计算所输数字总和):")
while user_input!="0":
    num =float(user_input)
    total=total+num
    user_input = input("请用户输入一系列数字,(直到输入0为止，计算所输数字总和):")
result=total
print("您输入的数字和为"+str(result))




print("密码程序")
user_input=input("请您输入密码")
while user_input!="maria":
    user_input = input("密码错误，请重新输入")
print("密码正确，欢迎进入")

user_input=input("请随机输入1-100内的一个数字")
while user_input!="67":
    user_input = input("请重新输入")
print("正确，欢迎")

name="Jose"
year="lion"
message="""给{0}{1}的祝福，
给{0}{1}的甜蜜，{1}的运气，
给{0}{1}的健康，{1}的快乐，
给{0}{1}的心情，{1}的欣慰，
给{0}{1}的顺利，{1}的幸福，{1}的人生!""".format(name,year)
print(message)

name="Jose"
year="lion"
message=f"""给{name}{year}的祝福，
给{name}{year}的甜蜜，{year}的运气，
给{name}{year}的健康，{year}的快乐，
给{name}{year}的心情，{year}的欣慰，
给{name}{year}的顺利，{year}的幸福，{year}的人生!"""
print(message)

student = "小明"
subject = "数学"
score = 95
rank = 1

result = """学生{0}在{1}考试中获得了{2}分，
排名第{3}名，{0}的{1}成绩非常优秀，
{0}在{1}学科上表现{3}！""".format(student, subject, score, rank)
print(result)


