# 布尔类型是数字分类下的一种
print (int (True));
print (isinstance (True,int));
print (isinstance (False,int));
print (bool(1));
print (bool(0));
print (bool(-1));# 在数字类型下，布尔类型为0时，返回False

#布尔值总结
#当布尔值为0、None、空值时，布尔返回类型为False
print (bool(0));
print (bool(None));
print (bool());
print (bool(''));
print (bool(' '));#字符串中间不能有空格
print (bool([]));#空列表
print (bool({}));#空字典
print (bool(()));#空元组