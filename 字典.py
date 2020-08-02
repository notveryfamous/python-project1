# 简单字典的创建
fruits={'lemons':5,'apples':3};
print(fruits);

# 通过键访问成员
print(fruits['lemons']);
print(fruits['apples']); # 字典无序，不可通过序号访问，否则报错

# 更新字典成员
fruits['apples']=20;
print(fruits);
fruits['pears']=30;
print(fruits);

# 字典删除

# 方法一：删除指定成员
x={'chinese':10,'maths':20,'english':40};
del x['chinese'];
print(x);

# 方法二：清空字典中所有成员
y={'1':1,'2':2,'3':3};
y.clear();
print(y);

# 方法三：删除字典（删除后不可访问）
z={'lemons':5,'apples':3};
del z; # print(z);会报错

#--------------------------------------------------------------------#（我是分割线）

# 字典常用函数

# 1.复制字典
# dict.copy()
fruit1={'lemons':5,'apples':3};
fruit2=fruit1.copy();
print(fruit2);

# 2.获取字典的键
# dict.get(key.default=None)
# 获取key对应的值，若key不存在则返回default
print(fruit1.get('lemons'));
print(fruit1.get('lemon'));
print(fruit1.get('lemon','无此key'));

# 3.字典的迭代

# dict.items()
# 获取由键和值组成的迭代器

# dict.keys()
# 获取键的迭代器

# dict.values()
# 获取值的迭代器

fruit1={'lemons':5,'apples':3};
print(fruit1.items());
print(fruit1.keys());
print(fruit1.values());

# 4.字典成员的删除

# dict.pop(key[default])
# 删除key:value的指定成员组，若不存在，则返回default
fruit3={'lemons': 5, 'apples': 20, 'pears': 30};
fruit3.pop('lemons');
print(fruit3);
print(fruit3.pop('a','无此key'));

# dict.popitem()
# 从字典末尾删除key:value，并返回key:value
fruit3={'lemons': 5, 'apples': 20, 'pears': 30};
print(fruit3.popitem());
print(fruit3.popitem());
print(fruit3.popitem());

# 5.更新字典成员

# dict.update([key:value])
# 从另外一个字典更新成员（若不存在则创建，若存在则覆盖）
fruit3={'lemons': 5, 'apples': 20, 'pears': 30};
fruit3.update({'lemons':10});
print(fruit3);
fruit3.update({'a':10});
print(fruit3);

# dict.setdefault(key,default=None)
# 若字典存在key，则返回对应的值（不会覆盖原值），若字典不存在key，则建立一个key:default的字典成员
fruit3={'lemons': 5, 'apples': 20, 'pears': 30};
print(fruit3.setdefault('lemons',20));
fruit3.setdefault('a',20);
print(fruit3);