#掌握生成器（yield）实现惰性求值，高效生成斐波那契数列，节省内存且支持大数量级序列。...2025.12.31
#Python 的 range(start, stop) 表示：
#从 start 开始
#一直数到 stop - 1
#不包括 stop

def get_sequence(num):
    """获取斐波拉契数列"""
    # 初始化数据
    n = 0
    one = 0
    two = 1
    # 获取各个数列值
    while n < num:
        # 返回数列值
        yield two
        # 替换位置计算
        tmp = one
        one = two
        two += tmp
        n += 1
# 程序主入口
if __name__ == '__main__':
    number = int(input('请输入一个数获取斐波拉契数列：'))
    # 获取数列
    number_list = get_sequence(number)
    # 打印数列
    for value in number_list:
        print(value)
#编写一个生成器函数 even_squares(n)，用于生成前 n 个偶数的平方（如 4, 16, 36...）。
#在主程序中，让用户输入 n，然后打印这些平方数，并使用内置函数 sum() 计算它们的总和。
def even_squares(n):
    for i in range(1,n+1):
        yield(2*i)**2
if __name__ == '__main__':
    n=int(input('请输入一个数:'))
    gen=even_squares(n)
# 方法1：转成列表打印（方便看所有数）
    squares_list = list(gen)
    print("前", n, "个偶数的平方：", squares_list)
    total=sum(even_squares(n))
    print(f'它们的总和是：{total}')

