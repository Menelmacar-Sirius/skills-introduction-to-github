#掌握基本算术运算符（含取模）、浮点数转换、除零防护及简单几何公式应用，注意运算安全与变量命名清晰性。2025.12.28
# 程序主入口
if __name__ == '__main__':
    # 运算符的用法
    number_one = input('请输入第一个数：')
    number_two = input('请输入第二个数：')
    # + 加法的使用
    sum_value = float(number_one) + float(number_two)
    print('加法运算：' + number_one + ' + ' + number_two + ' = ' + str(sum_value))
    # - 减法的使用
    diff_value = float(number_one) - float(number_two)
    print('减法运算：' + number_one + ' - ' + number_two + ' = ' + str(diff_value))
    # * 乘法的使用
    mul_val = float(number_one) * float(number_two)
    print('乘法运算：' + number_one + ' * ' + number_two + ' = ' + str(mul_val))
    # / 除法的使用
    if number_two == '0':
        print('除法运算，除数不能为0')
    else:
        div_value = float(number_one) / float(number_two)
        print('除法运算：' + number_one + ' / ' + number_two + ' = ' + str(div_value))
    # % 取模的使用
    after_val = float(number_one) % float(number_two)
    print('取模运算：' + number_one + ' % ' + number_two + ' = ' + str(after_val))

    # π的值
    pai = 3.14
    # 圆长
    circle_len = int(input('请输入圆长计算周长和面积：'))
    # 计算圆周长
    circumference = 2 * pai * (circle_len / 2)
    print('圆周长为：' + str(circumference))
    # 计算圆面积
    area = pai * (circle_len / 2) ** 2
    print('圆面积为：' + str(area))
#用户输入矩形的长和宽（支持小数），程序自动计算并输出：
#周长,面积,对角线长度（公式：√(长² + 宽²)）
#要求：使用 float 转换输入，结果保留两位小数。

import math
if __name__ == '__main__':
    length = float(input('请输入长：'))
    width = float(input('请输入宽：'))
#周长
perimeter= (length + width) * 2
print('矩形周长为' + str(perimeter))
#面积
area= length * width
print('矩形的面积为' + str(area))
#对角线
diagonal= math.sqrt(length ** 2 + width ** 2)
print('矩形的对角线为' + str(diagonal))
print(f'矩形对角线为：{diagonal:.2f}')
#f-string 和 {:.2f} 自动保留两位小数，输出更整洁！
if length == width:
    print(f'它的周长是{perimeter}，面积是{area}，对角线是{diagonal}，所以它是个正方形哦')














