#coding:UTF-8
#__autor__='wyxces'

# 随机整数：
import random
import string

print(random.randint(1,100))

# 随机选取0到100间的偶数：
print(random.randrange(0,100,2))

# 随机浮点数：
print(random.random())
print(random.uniform(1,10))

# 随机字符：
str = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()'
print(random.choice(str))

# 多个字符中生成指定数量的随机字符：
print(random.sample(str,5))

# # 从a-zA-Z0-9生成指定数量的随机字符串：
print(''.join(random.sample(string.ascii_letters+string.digits,8)))


# # 多个字符中选取指定数量的字符组成新字符串：
list01 = ['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a']
print(''.join(random.sample(list01,5)))


#  打乱排序
list02 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(list02)
print(list02)

# 多个字符串中选取指定数量的字符串
list03 = ['zs','ys','x','ws','vs','us']
print(random.choice(list03))