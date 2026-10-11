shopping_list=["苹果","香蕉","梨子","橘子","草莓"]#列表与布尔值，字符串等不同，是可变的，案例如下
shopping_list.append("蓝莓")#为列表添加新的东西#“方法“，实现特定功能
shopping_list.remove("橘子")
print(shopping_list)#可变-类型
print(shopping_list[3])
shopping_list[0]="菠萝"
print(shopping_list)


a="appointment"
print(a.upper())#大写转换
a=a.upper()
print(a)#不可变-类型


list_1=["string"]
list_1.append("69.77")
list_1.append("True")
list_1.append("None")
print(list_1)

num_list=[67,-9,33,-84,0,1532,-783]#非字符串无需引号，否则无法进行数学运算
print(max(num_list))
print(min(num_list))
print(sorted(num_list))#排序


shopping_menu=[]
shopping_menu.append("食品")
shopping_menu.append("日用品")
shopping_menu.remove("日用品")
shopping_menu.append("药品")
shopping_menu.append("服装")
shopping_menu.append("五金")
print(shopping_menu)
print(len(shopping_menu))
print(shopping_menu[2])
shopping_menu[3]="烟酒"
print(shopping_menu)

#字典
contacts={"wayne":"bruce","kent":"clark","prince":"diana"}#姓氏在前，名字在后
print(contacts["wayne"])
print("wayne" in contacts)
print(len(contacts["wayne"]))


pure_dic={"白羊":"3月21日～4月20日","双子":"5月22日～6月21日","金牛":"4月21日～5月21日","巨蟹":"6月22日～7月22日"}
pure_dic["狮子"]="7月23日～8月23日"
pure_dic["处女"]="8月24日～9月23日"
pure_dic["天秤"]="9月24日～10月23日"
pure_dic["天蝎"]="10月24日～11月22日"

star=input("请输入您的星座：")
if star in pure_dic:
    print(pure_dic[star])
else:
    print("您查询的星座暂未收录")
    print("当前仅收录 " + str(len(pure_dic)))
