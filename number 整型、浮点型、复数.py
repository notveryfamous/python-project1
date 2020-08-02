# 整型
# bin   二进制
# oct   八进制
# int   十进制
# hex   十六进制
print (bin(10));
print (oct(10));
print (hex(10));

# 浮点型
#type()函数可以查看数的类型
print (type(3+1));
print (type(3+1.0));
print (type(3-1));
print (type(3-1.0));
print (type(3*1));
print (type(3*1.0));
print (type(3/1));
print (type(3/1.0));# 在python中，无论整型相除还是浮点型相除，结果都是浮点型，如果是整除（//）则结果为整型

# 复数
print (complex (3,4));
print (complex (3,4).real);
print (complex (3,4).imag);
# 复数只在科学计数法中使用
print (complex('3'));# 如果填入了字符串，后面不可填写，且字符串中不可有空格
print (complex('3+4j'));# 可以在字符串中添加
print (complex('3+4j').real);
print (complex('3+4j').imag);