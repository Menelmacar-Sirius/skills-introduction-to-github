#包含了程序结构、循环、条件判断、列表操作，，，但是主要是random随机函数的学习，今天是2025年12月27号。
import random
# 程序主入口
if __name__ == '__main__':
    # 打印
    print('Hello World!')

    # 取4个随机数
    i = 0
    rand_list = []
    while i < 4:
        rand_num = random.randint(0, 499)
        if rand_num not in rand_list:
            rand_list.append(rand_num)
            i += 1
    # 输出组队随机编码
    print(rand_list)
#某社区举办抽奖活动，共有 200 位居民（编号 1 到 200）。现在要从中随机抽出 5 位幸运儿，每人只能中奖一次。
#请编写一个程序：
#随机生成 5 个 不重复 的编号（范围：1~200）
#将结果按从小到大排序后打印出来
#最后一行显示：“恭喜以上 5 位居民中奖！”
i=0
ran_list = []
while i < 5:
    ran_num = random.randint(1, 200)
    if ran_num not in ran_list:
        ran_list.append(ran_num)
        i += 1
new_ran =sorted(ran_list)
print(f"{new_ran}恭喜以上5位居民获奖")
#接下来我将会使用random.sample写法
import random
lucky_numbers = random.sample(range(1, 201), 5)
lucky_numbers.sort()
# 打印结果
print(lucky_numbers)
print("恭喜以上5位居民中奖！")



#有关random函数的练习
import random
random.random()
random.uniform(7.052, 394.71)

print(f"生成的随机数为{random.randint(1,89)}")#randint = 随机抽整数，头尾都算数！

print(f"生成的随机数是{random.uniform(7.052, 394.71):.3f}")
#使用 :.3f 可以格式化浮点数，保留三位小数，让输出更整洁。

#random.choice(列表) —— 从一堆东西里随机挑一个，可以运用为浮点型float的随机抽取。
kids = ["小明", "小红", "小刚", "小丽"]
chosen = random.choice(kids)
print(chosen)  # 比如输出：小红

#random.shuffle(列表) —— 把一列东西彻底打乱顺序
cards = ["A", "2", "3", "4", "5"]
random.shuffle(cards)
print(cards)  # 比如：['3', 'A', '5', '2', '4']

#random.sample(列表, k) —— 从一堆东西里随机挑 k 个，不重复
people = ["张三", "李四", "王五", "赵六", "钱七"]
winners = random.sample(people, 3)
print(winners)  # 比如：['李四', '钱七', '张三']