#掌握 try-except-finally 异常处理结构，能区分通用与具体异常捕获。2025.12.29
# 程序主入口
if __name__ == '__main__':
    # 异常捕获
    try:
        result = 8 / 0
        print(result)
    except Exception as e:
        print('Error')

    # 具体的异常捕获
    try:
        result = 8 / 0
        print(result)
    except ValueError as e:
        print('ValueError')
    except ZeroDivisionError as e:
        print('ZeroDivisionError')
    finally:
        print('finally')
#捕获 ValueError（输入非数字）并提示“请输入有效数字”；
#捕获 ZeroDivisionError（除数为0）并提示“除数不能为零”；
#无论成功与否，最后都打印“计算结束”。
if __name__ == '__main__':
    try:
        number_one=int(input())
        number_two=int(input())
        result = number_one / number_two
        print(result)
    except ZeroDivisionError as e:
        print('ZeroDivisionError,除数不能为零')
    except ValueError as e:
        print('ValueError,请输入有效数字')
    finally:
        print("计算结束")
#掌握函数定义（含默认参数）、递归思想、常用内置函数（abs/max/类型转换）
def fun(number=18):
    """定义函数，传参数并带默认值"""
    if number > 18:
        return '成年人'
    else:
        return '小屁孩'

def re_fun(number):
    """递归调用，计算某个数的阶乘"""
    if number == 1:
        return number
    return number * re_fun(number - 1)
#编写一个带默认参数的函数 power(base, exponent=2)，计算 base 的 exponent 次方。
# 再编写一个递归函数 sum_to_n(n)，计算从 1 加到 n 的和（如 sum_to_n(3) = 1+2+3 = 6）。
# 在主程序中测试这两个函数，并使用 max() 和 abs() 处理结果。

#先定义，后使用
def power(base, exponent=2):
    return base ** exponent

def sum_to_n(n):
    if n<=0:
        return 0  # 防止负数或0导致无限递归（更安全）
    if n == 1:
        return 1
    return n + sum_to_n(n - 1)

if __name__ == '__main__':
    base = int(input('请输入底数：'))
    exp_input = input('请输入指数（直接回车默认为2）：')
    exponent = int(exp_input) if exp_input else 2
    result = power(base, exponent)
    print(f'结果是{result}')

    n = int(input('请输入一个正整数 n：'))
    sum_result = sum_to_n(n)
    print(f'1 到 {n} 的和是：{sum_result}')

    abs_power = abs(result)      # 取幂结果的绝对值（如果底数是负数就有用）
    final_max = max(abs_power, sum_result)  # 比较两个结果，取最大值

    print(f'幂结果的绝对值：{abs_power}')
    print(f'两个结果中的最大值：{final_max}')