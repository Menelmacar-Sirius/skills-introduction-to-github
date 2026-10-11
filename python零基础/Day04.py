# while的用法-计算100以内所有偶数的和 今天是2025.12.29
sum = 0
n = 0
while n <= 100:
    if n % 2 == 0:
        sum += n
    n += 1
print(sum)

#掌握素数判定逻辑：通过试除法检查2到n/2之间是否有因数，并注意处理小于2的非素数边界情况。
# 程序主入口
if __name__ == '__main__':
    number = int(input('请输入一个整数：'))
    # 先处理特殊情况：小于2的数都不是素数！
    if number < 2:
        print(str(number) + '不是素数')
    else:
        is_prime = True  # 先假设它是素数
        # 从2开始，试到 number//2（整除一半）
        start = 2
        while start <= number // 2:
            if number % start == 0:  # 如果能整除
                is_prime = False     # 就不是素数
                break                # 不用再试了
            start += 1

        if is_prime:
            print(str(number) + '是素数')
        else:
            print(str(number) + '不是素数')

    str_num = str(number)  # 转成字符串
    if str_num == str_num[::-1]:
#[::] 叫做“切片”（slice），就像切香肠：
#num[0:3] → 切前3段...num[1:] → 从第2段切到结尾
#而 [::-1] 的意思是：
#起始：从头到尾（默认）
#结束：从头到尾（默认）
#步长：-1 → 表示“倒着走”！
# 所以 num[::-1] = “从最后一个字符，一个一个往回走，直到第一个”。

        print(f'{number}是回文数')
    else:
        print(f'{number}不是回文数')

#编写一个程序，判断用户输入的整数是否为回文素数（既是素数，又是回文数，如131、313）。
#要求：先判断是否为素数；。。再判断其字符串形式是否正读反读相同；。。输出“是回文素数”或“不是回文素数”
