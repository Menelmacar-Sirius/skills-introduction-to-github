import sys

# 读取所有输入并拼接成一个完整的字符串
lines = sys.stdin.read().splitlines()
full_str = ""
for line in lines:
    full_str += line.strip()

# 截取到 'E' 之前的内容，忽略 E 及之后的所有字符
if 'E' in full_str:
    full_str = full_str[:full_str.find('E')]

# 初始化两种赛制的比分
score_11_w = 0
score_11_l = 0
score_21_w = 0
score_21_l = 0

# 用于存储每局结束时的比分结果
results_11 = []
results_21 = []

# 遍历每一个球的胜负记录
for char in full_str:
    if char == 'W':
        score_11_w += 1
        score_21_w += 1
    elif char == 'L':
        score_11_l += 1
        score_21_l += 1
    else:
        # 忽略非 W、L 的字符（虽然题目说 E 之后忽略，但防患于未然）
        continue

    # 判断 11 分制是否结束一局
    # 条件：一方达到 11 分，且分差 >= 2
    if (score_11_w >= 11 or score_11_l >= 11) and abs(score_11_w - score_11_l) >= 2:
        results_11.append(f"{score_11_w}:{score_11_l}")
        score_11_w = 0
        score_11_l = 0

    # 判断 21 分制是否结束一局
    # 条件：一方达到 21 分，且分差 >= 2
    if (score_21_w >= 21 or score_21_l >= 21) and abs(score_21_w - score_21_l) >= 2:
        results_21.append(f"{score_21_w}:{score_21_l}")
        score_21_w = 0
        score_21_l = 0

# 输出 11 分制的结果
for res in results_11:
    print(res)
# 输出 11 分制当前正在进行的局（如果比分不为 0:0，或者刚好打完一局后下一局刚开始的 0:0 也要输出）
# 注意：如果刚好打完一局，上面的逻辑已经把比分清零了，此时输出 0:0 代表下一局刚开始
print(f"{score_11_w}:{score_11_l}")

# 输出空行分隔
print()

# 输出 21 分制的结果
for res in results_21:
    print(res)
print(f"{score_21_w}:{score_21_l}")