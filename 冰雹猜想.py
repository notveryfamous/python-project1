import time

#函数Collatz
def Collatz(number):
    if number % 2 == 0:
        print (number // 2)
        return (number // 2)

    elif number == 1:
        print (number)
        return number

    else:
        print(3*number + 1)
        return(3*number + 1)


if __name__ == '__main__':
#输入内容校验：1.只能输入数字；2.首次输入错误后，变更输入提示
    while 1:
        number = input('please input a digital: ').strip()
        if number.isdigit(): break
        while 1:
            number = input('Input is illegal, Input again: ').strip()
            if number.isdigit(): break
        break
        
    T = 0
    
    #用while不断循环函数直到结果为1
    while 1:
        time.sleep(0.001)           #每0.1S计算一次，不至于卡死                    
        T += 1
        print('seq:'+str(T),'--->', end=' ')     #结合collatz函数内部print语句进行格式化输出
        number = Collatz(int(number))
        if number == 1: break