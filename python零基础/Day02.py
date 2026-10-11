#掌握条件判断、循环校验、基本算术运算及除零异常预防，2025.12.28
# 程序主入口
if __name__ == '__main__':
    # 运算方式
    operate_type = input('请选择运算类型：1加法，2减法，3乘法，4除法：')
    # 判断类型是否有效
    while int(operate_type) not in (1, 2, 3, 4):
        print('类型选择错误，只能为1-4')
        operate_type = input('请重新选择运算类型：1加法，2减法，3乘法，4除法：')
    # 第一个数
    number_one = int(input('请输入第一个数：'))
    # 第二个数
    number_two = int(input('请输入第二个数：'))
    if operate_type == '1':
        # 1加法
        result = number_one + number_two
        print('加法运算，结果是：' + str(result))
    elif operate_type == '2':
        # 2减法
        result = number_one - number_two
        print('减法运算，结果是：' + str(result))
    elif operate_type == '3':
        # 3乘法
        result = number_one * number_two
        print('乘法运算，结果是：' + str(result))
    elif operate_type == '4':
        # 4除法
        if number_two == 0:
            print('第二个数即除数不能为0')
        else:
            result = number_one / number_two
            print('除法运算，结果是：' + str(result))
    else:
        print('算法类型错误')

#编写一个“温度转换器”程序：
#用户输入一个数字和单位（C 表示摄氏度，F 表示华氏度），程序自动转换为另一种单位。
#要求：校验单位只能是 'C' 或 'F'（不区分大小写）；
#若输入无效单位，提示并重新输入；
#输出格式如：“32°F = 0°C”。
#经验之谈，注意数字与字符串str的问题，整数int，非整数，浮点float
#注意1.c2.f的问题，本质上是12代替规避了cf的大小写问题
if __name__ == '__main__':
    temperature_degree=float(input("请输入一个数字"))
    temperature_change=input("请输入任意单位：1.C，2.F")
    while int(temperature_change)not in (1,2):
        print('类型选择错误，只能为1-2')
        temperature_change = input("请重新输入任意单位：1.C，2.F")
    if temperature_change == "1":
        result=temperature_degree *1.8+32
        print('摄氏度转换为华氏度的结果是：' + str(result))
    elif temperature_change == "2":
        result=(temperature_degree-32)/1.8
        print('华氏度转换为摄氏度的结果是：' + str(result))
    else:
        print("转换错误")

#掌握带星号（*）的序列解包语法，能灵活提取列表/元组中的部分元素，剩余元素自动聚合成列表。
# 程序主入口
if __name__ == '__main__':
    company, date, *others = ['juejin', '20181016', 'morning', 'Tues']
    print(company, date, others)
#给定一个表示学生信息的列表：['张三', '男', '18', '高三', '数学', '物理', '化学']，
#其中前四项是基本信息，后面是选修课程。
#请用一行解包语句，将姓名、性别、年龄、年级分别赋值，并将所有课程存入一个列表 courses，最后打印出来。
if __name__ == '__main__':
    name,gender,age,grade,*sources=['张三', '男', '18', '高三', '数学', '物理', '化学']
    print(name, gender,age,grade,sources)
























