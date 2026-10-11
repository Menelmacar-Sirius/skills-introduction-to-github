n,k=map(int,input().split())
sum_a = 0  # A类数的和
count_a = 0  # A类数的个数
sum_b = 0  # B类数的和
count_b = 0  # B类数的个数
for i in range (1,n+1):
    if i%k==0:
        sum_a=sum_a+i
        count_a=count_a+1
    else:
        sum_b=sum_a+i
        count_b=count_b+1
average_a=sum_a/count_a
average_b=sum_b/count_b
print(f"{average_a:.1f} {average_b:.1f}")


n=int(input())
# 2. 准备一个变量 current_num，从 1 开始计数
current_num = 1
# 我们用 i 来代表“当前是第几行”
for i in range(1, n + 1):

    # 4. 内层循环：控制每一行打印多少个数字
    # 第一行打印 n 个，第二行打印 n-1 个...
    # range(i, n+1) 这个写法刚好能控制次数递减
    for j in range(i, n + 1):

        # 5. 打印数字，并格式化
        # end="" 表示打印完不换行，连在一起
        # f"{current_num:02d}" 表示强制占2位，不够补0
        print(f"{current_num:02d}", end="")
        # 6. 数字加 1，为下一次打印做准备
        current_num += 1
    # 7. 内层循环结束，说明这一行打印完了，这里打印一个换行
    print()

n,x=map(int,input().split())
count=0
for i in range(1,n+1):
    num=i
    while num>0:
        last=num%10
        if last==x:
            count+=1
        num=num//10
print(count)

k=int(input())
s=0.0
n=0
while s<=k:
    n+=1
    s=s+(1/n)
print(n)


k=int(input())
s=0#总金币数量
n=1# n 代表当前是第几轮（也是每天发几枚，要发几天）
while k>0:
    if k>=n:
        s=s+(n*n)
        k=k-n
        n=n+1
    else:
        s=s+(k*n)
        k=0
print(s)  


def is_prime(n):
    """判断一个数是否为质数"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

L = int(input())
current_sum = 0
count = 0
n = 2
result_primes = []

while True:
    if is_prime(n):
        if current_sum + n <= L:
            current_sum += n
            result_primes.append(n)
            count += 1
        else:
            break
    n += 1

print(len(result_primes))
    # 2. 再输出具体的质数，用空格隔开
if result_primes:
    print(*result_primes.split())


# 小明是一名魔法师，他有一根魔法杖。这根魔法杖需要通过镶嵌“魔力水晶”来充能。
# 商店里有无数颗魔力水晶，每颗水晶都有一个固定的“魔力值”。
# 水晶的魔力值依次为正整数序列：1, 2, 3, 4, 5, ...
# 小明的魔法杖有一个最大承载力 M
# 镶嵌在水晶上的魔力值总和不能超过这个 M
# 为了施展最强的法术，小明希望镶嵌尽可能多的水晶数量。请问他最多能镶嵌多少颗水晶？并依次输出这些水晶的魔力值。
# 一个正整数 M
# 表示魔法杖的最大承载力。
# 输出格式
# 第一行输出一个整数，表示最多能镶嵌的水晶数量。
# 第二行按从小到大的顺序输出这些水晶的魔力值，数字之间用空格隔开。

L=int(input())
current_sum = 0  # 当前总魔力值
count = 0        # 水晶数量
crystals = []    # 用来存选中的水晶


def is_prime(n):
    if n <2:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True

i=2#当前要拿的水晶魔力值为 i。
while True:
    if is_prime(i):
        if current_sum+i<=L:
            current_sum+=i
            count+=1
            crystals.append(i)
        else:
            break
    i+=1
print(count)
print(*crystals)

#两种算法1.硬算 (不被识别)2.斐波那契数列
import math
genaho=math.sqrt(5)
n=int(input())
x=((1+genaho)/2)**n
y=((1-genaho)/2)**n
FN=(x-y)/genaho
print(FN)

n=int(input())
f=[0,1,1]
for i in range (3,n+1):
    feibinaqie=f[i-1]+f[i-2]
    f.append(feibinaqie)
print(f"{f[n]:.2f}")


n = int(input())
nums = list(map(int, input().split()))
nums.sort()

max_len = 1
current_len = 1

for i in range(1, n):
    if nums[i] == nums[i-1] + 1:
        current_len += 1
        # i=5，,如果是连贯的（比如 4 和 5），当前长度 +1
        if current_len > max_len:
            max_len = current_len
            # 如果是重复数字（比如 5 和 5），上面两个条件都不满足，什么都不做，保留原长度
    elif nums[i] != nums[i-1]:
        current_len = 1
    # 如果不是连贯的，而且也不是重复数字（比如 6 和 8），那就是彻底断了
    # 重新从 1 开始数

print(max_len)

n=int(input())
i=2
while i*i<=n:
    if n%i==0:
        break
    i=i+1
print(n//i)

import sympy
n=int(input)
m=sympy.primefactors(n)
print(m[-1])


n=int(input())

current=0
for i in range(n):
    row=[]
    # 遍历每一行（共 n 行）
    # 初始化当前行为空列表
    for j in range(n):# 遍历每一列（每行 n 个元素）
        row.append(str(current))
        current+=1
    print(''.join(row))

print()

current=0

for i in range(1,n+1):
        # 计算缩进空格数：2*(n-i)
    spaces = ' ' * (2 * (n - i))
    row = []
    for j in range(i):  # 第i行有i个数字
        row.append(str(current))
        current += 1
    # 拼接缩进和数字行
    print(spaces + ''.join(row))

import statistics
n=int(input())
num=list(map(float, input().split()))
num.sort()
last=num.pop()
first=num.pop(0)
average=sum(num)/len(num)
print(f"{average:.2f}")

#一周金额7X+21K=7（X+3K），52周N=364（X+3K），，so（X+3K）=N/364=target
N=float(input())
target=N//364
K=1
X=target-3*K

while X>100:
    K=+1
    X=target-3*K
print(X)
print(K)

budgets = []
for i in range(12):
    x = int(input())
    budgets.append(x)
#=====
budgets = [int(input()) for _ in range(12)]

hand=0 #津津手中持有的现金，初始为 0。
saved=0 #存在妈妈那里的总存款，初始为 0。

for i in range(12):
    hand+=300#
    hand=hand-budgets[i]

    if hand <0:
        print(f"-{i+1}")
        exit()

    to_save=(hand//100)*100
    saved+=to_save
    hand=hand-to_save

total=hand+int(saved*1.2)
print(total)

#小鱼比可爱
n = int(input())
a = list(map(int, input().split()))

result = []
for i in range(n):#外层循环。变量 i 代表当前这条鱼的下标
    count = 0
    for j in range(i):  # 只遍历左边的鱼
        if a[j] < a[i]:#内层循环。变量 j 代表当前鱼左边的那些鱼的下标。
            count += 1
    result.append(str(count))
#" ".join(...) 会把其中每个元素用一个空格 ' ' 连接起来。
print(" ".join(result))


nums= list(map(int, input().split()))
result=nums[:-1][::-1]
print(" ".join(map(str, result)))
#map(str, result)：将每个数字转为字符串 
#" ".join(...) 用空格把它们连接起来

n = int(input())
path=[n]
while n!=1:
    if n%2==1:
        n=n*3+1
    else:
        n=n//2
    path.append(n)
# path[::-1] 利用切片将列表反转（从 1 开始回到 n）
# map(str, ...) 将数字列表转为字符串列表
# " ".join(...) 用空格连接
print(" ".join(map(str, path[::-1])))

l,m=map(int,input().split())#表示马路的长度 l 和区域的数目 m。
#初始化马路状态
# 创建一个长度为 l+1 的列表，初始值全为 1（表示有树）
# 为什么要 l+1？因为是从 0 到 l，总共 l+1 个点
trees = [1] * (l + 1)
for _ in range (m):
    u,v=map(int,input().split())
    # 将这个区域内的树全部移走（标记为 0）
    # 注意：range(u, v+1) 是因为题目要求包括端点 v，而 range 是左闭右开
    for i in range(u, v + 1):
        trees[i] = 0
#统计剩余的树
# sum(trees) 会计算列表中所有元素的和
# 因为只有 1 (有树) 和 0 (无树)，总和就是 1 的个数
remaining_trees = sum(trees)
print(remaining_trees)


n= int(input())
student =[]
for _ in range(n):
    line= list(map(int, input().split()))
    Chinese , mathematics , English = line[0], line[1], line[2]
    total = Chinese + mathematics + English 
    student.append([Chinese ,mathematics ,English ,total ])
count=0
for i in range(n):
    for j in range (i+1,n):
        s1=student[i]
        s2=student[j]
         # abs() 函数用于计算绝对值
        diff_c = abs(s1[0] - s2[0]) # 语文差
        diff_m = abs(s1[1] - s2[1]) # 数学差
        diff_e = abs(s1[2] - s2[2]) # 英语差
        diff_t = abs(s1[3] - s2[3]) # 总分差
        if diff_c <= 5 and diff_m <= 5 and diff_e <= 5 and diff_t <= 10:
            count += 1

print(count)




import sys

line = sys.stdin.readline().strip()

n = len(line)
# 标记数组，记录哪些下标已经被“完整单词”占用了
used = [False] * n

count_boy = 0
count_girl = 0

# 第一遍扫描：寻找完整的单词
i = 0
while i < n:
    found = False

    # 尝试匹配 "boy" (长度3)
    if i + 3 <= n and line[i:i + 3] == "boy":
        count_boy += 1
        # 标记这3个位置已使用
        for j in range(i, i + 3):
            used[j] = True
        i += 3
        found = True

    # 尝试匹配 "girl" (长度4)
    elif i + 4 <= n and line[i:i + 4] == "girl":
        count_girl += 1
        # 标记这4个位置已使用
        for j in range(i, i + 4):
            used[j] = True
        i += 4
        found = True

    # 如果当前位置不是单词开头，继续下一个字符
    if not found:
        i += 1

# 第二遍扫描：统计剩余未使用的字符
for i in range(n):
    if not used[i]:
        char = line[i]
        # 属于 boy 的残余字符：o 或 y
        # 注意：b 只存在于 boy 中，如果剩下的 b 没有被完整 boy 覆盖，
        # 它可能是另一个 boy 的唯一残留。但根据题目逻辑，
        # 通常 o 和 y 是区分度最高的。
        # 题目逻辑暗示：如果剩下一个 o 或 y，它一定来自一个 boy。
        if char in ['o', 'y']:
            count_boy += 1

        # 属于 girl 的残余字符：i, r, l
        # 同理，g 只存在于 girl，但 i, r, l 是 girl 独有的后缀特征
        elif char in ['i', 'r', 'l']:
            count_girl += 1

        # 关于字符 'b' 和 'g'：
        # 如果一个单独的 'b' 剩下，它必然属于一个 boy。
        # 如果一个单独的 'g' 剩下，它必然属于一个 girl。
        # 但根据题目“覆盖”的特性，通常 o, y, i, r, l 更容易作为残留出现。
        # 为了严谨，我们可以加上：
        elif char == 'b':
            count_boy += 1
        elif char == 'g':
            count_girl += 1

# 输出结果
print(count_boy)
print(count_girl)



import sys

line = sys.stdin.readline().strip()

m,n=map(int,input())
for _ in range (n):
     