# 一、列表的创建
# 创建空列表
print (list());
# 只有一个元素的列表
print ([1,]);
# 有四个元素的列表
print ([1,2,3,4,]);
# 有不同数据类型的列表
print ([1,2,3,'abcd',[1.55,15,'1xed5']]);

# 二、列表访问
print ([1,3.14,'abc',[1,2,'google']] [3]);
print ([1,3.14,'abc',[1,2,'google']] [3] [2]);

# 三、列表的相加相乘
print ([1,2]+[3,4]);# 列表不可相减
print (['google',]*3);# 列表不可相除




# list.count(x)
# 查找列表中x出现的次数，不存在则返回0
x=[1,2,3,4,2];
print (x.count(2));
print (x.count(5));

# list.append(x)
# 向列表末尾追加成员x
a=[1,2,3,4];
a.append(5);
print (a);
b=[1,2,3,4];
b.append([5,6,7]);
print (b);

# list.extend(1)
# 向列表末尾追加另一个列表
p=[1,2,3,4];
q=[5,6,7,8,9];
p.extend(q);
print (p);

# list.index(x)
# 返回参数x的序号，如果没有，则报错
c=[1,2,3,4];
print (c.index(2));

# list.insert(index,obect)
# 在列表的指定位置插入参数
d=[1,2,3];
d.insert(2,'d');
print (d);

# list.pop()
# 默认删除列表的尾部成员，并且返回删除的成员
e=[1,2,3,4,5,6,7,8,9];
e.pop();
print (e);
e.pop(3);
print (e);

# list.remove(x)
# 删除列表中的指定成员（有多个时删除第一个），若指定成员不存在则报错
f=[1,2,3,4,'sks','win10','win10',1,2,4,3,'sks',[1],[1]];
f.remove(1);
f.remove('win10');
f.remove('sks');
f.remove([1]);
print (f);

# list.reverse()
# 将列表中的成员顺序颠倒
g=[1,2,3,4,'sks','win10','win10',1,2,4,3,'sks',[1],[1]];
g.reverse();
print (g);

# list.sort()
# 将列表中的成员排序（若无规律可循，则报错）
h=[30,52,10];
h.sort();
print (h);
i=[30,52,10];
i.sort(reverse=True);# 倒过来排序
print (i);
