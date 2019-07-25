#coding:UTF-8
#__autor__='wyxces'

# +号
str1 = "pythoe"+"+号"
print(str1)

# 逗号 + jion
str2 = "pythoe",",号"
str2_ = "".join(str2)
print(str2,str2_)
# 逗号  但是字符串之间会多出一个空格
print("pythoe",",号")


#直接连接
str3 = "pythoe""直接连接"
print(str3)
print("pythoe""直接连接")
str3_2 = "pythoe"    "直接连接2"
print(str3_2)

#格式化
str4 = '%s%s'%('Python', '格式化')
print(str4)


str4_2 = '{}{}'.format('Python', '格式化2')
print(str4_2)

#jion
str_list = ["python","jion"]
str5 = "".join(str_list)
print(str5)

#多行字符串拼接
str6 = ('select *'
     'from atable'
     'where id=888')
print(str6)

