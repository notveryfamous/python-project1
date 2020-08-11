# 算数运算符

# 一、关于加号的运算
# 1.数字之间相加
print(1+2.0);

# 2.数字与布尔型之间
print(int(True));
print(int(False));
print(1+True);
print(1+False);

# 3.字符串之间相加
print('Hello'+'Python'+'.');

# 二、关于减号的运算
# 集合之间的减法
a={1,2,3,4,5,6};
b={1,2,3};
print(a-b);

# 三、关于乘号的运算
# 字符串、列表、元组
print('Python '*3);
print([1,2,3]*3);
print((1,2,3)*3);

# 四、关于求余的运算
# 求余时，如果是浮点型，则结果返回浮点型
print(10%3);
print(10.0%3);

# 五、关于取整的运算
# 求余时，如果是浮点型，则结果返回浮点型
print(10//3);
print(10//3.0);


#-----------------------------------------------------------------------------#（我是分割线）


# 赋值运算符

# 变量赋值
a=1;
print(a);
# 先运算再赋值

# +=
a=1;
b=2
a += b; # a=a+2
print(a);

# -=
a=1;
b=2;
a -= b; # a=a-2
print(a);

# *=
a=1;
b=2;
a *= b; # a=1*2
print(a);

# /=
a=1;
b=2;
a /= b; # a=1/2
print(a);

# %=
a=1;
b=2;
a %= b; # a=a%b
print(a);

# **=
a=1;
b=2;
a **= b; # a=a**b
print(a);

# //=
a=1;
b=2;
a //= b; # a=a//b
print(a);


#-----------------------------------------------------------------------------#（我是分割线）


# 比较（关系）运算符
# 返回布尔类型

# 数字之间比较

# == 返回两个对象的值是否相等
print(1 == 1);
print(1 == 0.5);

# <> 和 != 都是不等于
# <> 用于Python 2
# != 用于 Python 2 3
print(1!=1);
print(1!=0.5);

# >=
print(1>=1.0);
print(1>=2);

# <=
print(1<=1.0);
print(1<=0.5);

# 字符串之间比较
print('a'=='b');
print('a'<'b');
# 通过ASCII码比较大小
print(ord('a'));
print(ord('b'));
print(ord('c'));
'''
如何比较'abc'与'acb'的大小
逐字比较：
先比较'a'与'a'，结果为一样大；
再比较'b'与'c'，结果为'c'大；
之后就不再比较，并输出结果：'acb'大
'''
print('abc'=='acb');
print('abc'<'acb');
print('abc'>'acb');

# 列表
print([1,3,2]==[1,2,3]);
print([1,3,2]>[1,2,3]);
print(['a','b','c']==['a','c','b']);
print(['a','b','c']<['a','c','b']);
'''
列表的比较方式等同于字符串的比较
'''

# 元组
print((1,3,2)==(1,2,3));
print((1,3,2)>(1,2,3));
print(('a','b','c')==('a','c','b'));
print(('a','b','c')<('a','c','b'));
'''
元组的比较方式等同于字符串的比较
'''

# 集合
# 元组
print({1,3,2}=={1,2,3});
print({1,3,2}>{1,2,3});
print({'a','b','c'}=={'a','c','b'});
print({'a','b','c'}<{'a','c','b'});
'''
集合的比较方式不等同于字符串的比较
集合是无序的
只要成员都一样就相等
'''

# 字典
# 字典不支持大小比较
print({'lemon':5,'apple':10}=={'lemon':5});
# print({'lemon':5,'apple':10}<{'lemon':5});会报错


#--------------------------------------------------------------------------------------------#


# 逻辑运算符
'''
逻辑运算符有三种
and（且）：条件同时成立的时候，返回True，否则返回False
or（或）：条件有一个成立的时候，返回True，否则返回False
not（非）：取反
逻辑运算符，操作类型与返回类型，都是布尔类型
这里的操作类型，除了布尔类型，其他数据类型都会先转为布尔类型，然后再进行逻辑运算
'''

# 布尔类型

# and
print(True and False);
print(False and False);
print(True and True);

# or
print(True or False);
print(True or True);
print(False or False);

# not
print(not True);
print(not False);
print(not not True);
print(not True or False); # False and False
print(not True and True); # False and True

# 非布尔类型
# 布尔类型为0、None、空值（空字符串、空列表、空元组、空字典、空集合）的时候，返回False

# and
# 当and的左右两边都为True时，返回右边的True；当and的左右两边都为False时，返回左边的False；
print(0 and 1);
print(0 and 0);
print(1 and 1);
print(2 and 1);

# or
# 当or的左右两边都为True时，返回左边的True；当or的左右两边都为False时，返回右边的False；
print(0 or 1);
print(0 or 0);
print(1 or 1);
print(2 or 1);
print(0 or []);

# not
print(not 1);
print(not 0);


#----------------------------------------------------------------#


# 成员运算符
'''
成员运算符有两种：
in
和
not in
判断一个元素是否在另一个元素中，返回布尔类型
'''

# 字符串
a='lemon';
print(a in 'hello lemon');
print(a not in 'hello lemon');

# 列表、元组、集合
a=1;
print(a in [1,2,3,4,5]);
print(a in (1,2,3,4,5));
print(a in {1,2,3,4,5});

# 字典
# 字典的成员运算，针对的是key:value中的key
a=1;
b={'lemon':5};
print(a in b);
a=5;
print(a in b);
a='lemon';
print(a in b);
