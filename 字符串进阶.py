# %格式化字符串
print ('hello %s' %('world'));
print ('hello %s,%s' %('world','python'));
print ('I am %d years old.' % (16));
print ('%.5f' %(3.14));
# format格式化字符串
print ('hello {}'.format('world'));
print ('hello {1} {0}'.format('world','lemmon'));
print ('I am {name} ,I am {age} years old.'.format(name='lemon',age=16));
print ('i am %(name)s ,i am %(age)s years old' %{'name':'lemon','age':16});