def greet():
    """最简单的函数示例"""
    print("Hello, World!")
greet()

def singer_name():
    print("jackson")
singer_name()

def 勾股定理():
    a=3
    b=4
    c=(a**2+b**2)**0.5
    result=c**2
    print(f"此结果为：{result}")
勾股定理()

#三菱锥体积公式。体积=底面*高*三分之一
def tetrahedron(base_area,height):
    tetrahedron_volume=1/3*base_area*height
    print(f"tetrahedron_Volume:{tetrahedron_volume}")
    return tetrahedron_volume
tetrahedron_Volume1=tetrahedron(20,10 )
tetrahedron_Volume2=tetrahedron(30,30 )


def fun():
    a=3
    print(a)

#bmi计算公式：体重除以身高的平方
def BMI_input(weight,height):
    BMI=weight/(height*height)
    if BMI<=18.5:
        category="偏瘦"
    elif 18.5<BMI<=25:
        category="正常"
    elif 25<BMI<=30:
        category="偏胖"
    else:
        category="肥胖"
    print(f"您的BM分类是BMI：{category}")
    return BMI
result=BMI_input(75,1.64)
print(result)

import statistics#中位数
print(statistics.median([-7.89,56,782,-93,6730,88]))

from statistics import mean,geometric_mean
print(mean,geometric_mean([89,56,782,93,6730,88]))





