# Tuple元组


# 创建空元组
print (());
print (tuple());
# 创建只有一个元素的元组
print((1,)); #只有一个元素的元组，在这个元素后必须加“,”

# 访问元组的元素
a=(1,2,3,4,5);
print (a[0]);
print (a[1]);

# 元组中的元素不可修改
# 当元组中的某个元素为列表或字典时，可以修改这个元素中的内容
b=(1,2,3,['google','microsoft',4,256]);
b[3][2]=128;
print(b);

# 元组常见函数
c=(1,2,3,4,5,6);
x=[10,20,30];
print (len(c));
print (max(c));
print (min(c));
print (tuple(x));