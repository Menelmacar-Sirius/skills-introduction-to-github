#掌握 Python 基本数据类型（整型、浮点、字符串、布尔、None）及常量命名规范，理解转义字符在字符串中的作用。
# 程序主入口
if __name__ == '__main__':
    # 整型
    int_value = 666
    print(int_value)

    # 浮点数
    float_value = 6.6666
    print(float_value)

    # 字符串
    str_value = 'hello world!'
    print(str_value)
    # 转移字符串
    str_escape_value = '这是转义的\'hello world!\''
    print(str_escape_value)

    # 布尔值
    # 布尔值只有True、False两种值
    bool_true_value = True
    print(bool_true_value)
    bool_false_value = False
    print(bool_false_value)

    # 空值
    none_value = None
    print(none_value)

    # 常量-变量名全部大写
    CONS_VALUE = '大表锅'
    print(CONS_VALUE)

# 程序主入口
if __name__ == '__main__':
    # 列表的定义
    team_list = ['da_biao_guo', 'xiao_biao_mei', 'team']
    print(team_list)

    # 用len()输出列表长度
    list_len = len(team_list)
    print(list_len)

    # 访问列表的元素值
    # 访问第1个元素
    print(team_list[0])
    # 访问第3个元素
    print(team_list[2])
    # 访问倒数第2个数
    print(team_list[-2])

    # 追加元素至末尾
    team_list.append('python')
    print(team_list)

    # 插入元素到指定的位置
    team_list.insert(3, 'learning')
    print(team_list)

    # 删除末尾的一个元素
    team_list.pop()
    print(team_list)

    # 删除指定位置的一个元素
    team_list.pop(2)
    print(team_list)

    # 更新某个元素值
    team_list[1] = '小表妹'
    print(team_list)

    # 列表元素值类型，可以不同
    team_list[0] = ['da', 'biao', 'guo']
    team_list[2] = 666
    print(team_list)

# 程序主入口
if __name__ == '__main__':
    # 定义一个字符串
    str_value = '这是字符串string'
    print(str_value)

    # 字符串utf-8编码
    str_encode = str_value.encode('utf-8')
    print(str_encode)

    # 字符串utf-8解码
    str_decode = str_encode.decode('utf-8')
    print(str_decode)

    # 统计字符串的长度
    str_len = len(str_value)
    print(str_len)

    # 格式化字符串
    str_format = '这是字符串格式化： %s' % str_value
    print(str_format)
    # 格式化整数
    int_value = 666
    int_format = '这是整数格式化： %d' % int_value
    print(int_format)
    # 格式化浮点数
    float_value = 666.66
    float_format = '这是浮点数格式化： %f' % float_value
    print(float_format)
    # 综合使用
    format_value = '%s %d + %f 的值' % ('计算', 6, 6.66)
    print(format_value)

    # 格式化字符串format()的用法
    format_fun_value = '{0}的{1}成绩是{2}分'.format('小明', '数学', 99)
    print(format_fun_value)

# 程序主入口
if __name__ == '__main__':
    # 定义一个元组
    team_tuple = ('da_biao_guo', 'xiao_biao_mei', 'team')
    print(team_tuple)

    # 访问元素值
    # 访问第1个元素
    print(team_tuple[0])
    # 访问第3个元素
    print(team_tuple[2])
    # 访问倒数第2个元素
    print(team_tuple[-2])

    # 定义一个元素值的元组，必须加一个逗号,
    best_language = ('python',)
    print(best_language)

    # 元组长度同样用len()
    tuple_len = len(team_tuple)
    print(tuple_len)