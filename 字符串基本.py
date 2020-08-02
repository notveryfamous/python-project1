#字符串连接
print ("A"+"B");

#字符串多次连接
print ("Jupyter"*3);

#字符串切片操作
print ("jupyter"[0]);
print ("jupyter"[1]);
print ("jupyter"[6]);
print ("jupyter"[-1]);#可以反过来截取，效果等同于print ("jupyter"[6]);
print ("jupyter"[1:4]);#可以截取一段字符，语法格式为：print ("字符串"[开头:结尾])；
print ("jupyter"[4:7]);
print ("jupyter"[4:]);#效果等同于print ("jupyter"[4:7]);
#String.strip()

#去除空白字符
print (' jupyter '.strip());
print (' \njupyter \r'.strip());

#去除指定字符
print ('123abc123'.strip('12'));
print ('123abc123'.strip('21'));
print ('4123abc123'.strip('21'));
print ('123abc123'.strip('213'));
print ('123ab123c321'.strip('213'));
#lstrip(),rstrip:一个处理左边，一个处理右边
print (' 123 '.lstrip());
print (' 123 '.rstrip());

#判断字符的开头和结尾
print ('apple'.startswith('a'));
print ('apple'.startswith('b'));
print ('apple'.endswith('e'));
print ('apple'.endswith('l'));

#返回字符位置
print ('apple'.find('p'));
print ('apple'.find('m'));
print ('apple'.index('p'));
print ('apple'.index('m'));

#字符串替换
print ('lemon'.replace('m','mmmm'));
print ('lemon'.replace('lomon','apple'));

#字符串的其他操作
print (len('apple'));
print ('lemonmmm'.count('m'));
print ('lemon'.upper());
print ('APPLE'.lower());
print ('apple'.center(10,'-'));
print ('apple'.center(5,'-'));
print ('apple'.center(4,'-'));
print ('apple'.center(6,'-'));