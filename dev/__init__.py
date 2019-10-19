
if __name__ == "__main__":
    #字符串类型
    cnStr = "空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，\n" \
            "Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，\n" \
            "便于日后代码的维护或重构。"
    print(cnStr)
    # =表示赋值的意思，==才是判断相等的
    num1 = 2
    num2 = 3
    print(num1 == num2)
    #python里靠缩进来维护逻辑关系，在一个条件的缩进块里的才会根据条件结果执行
    if num2 > 2:
        print(num1)
        if num1 > 2:
            print(num2)
    #这个语句不会管上面的if num2>2,始终会执行的
    print(num1+num2)
    #列表:list
    numList = [100,99,88]
    print(numList)
    # range(30): [0,30) 理论上列表可以保存很多元素
    for i in range(30):
        numList.append(i)
    #列表有很多方法，例如翻转方法(reverse)，reverse是列表内翻转
    numList.reverse()
    print("翻转后的列表numList内容是:",numList) #这个地方打印出来的结果，跟上面打印出来的是反的
    # strList = ["hi","今天晚上有空吗","我请你吃饭"]

    #长度函数:len,相当于一把尺子，能计算很多种数据类型的长度
    print("numList's length is：",len(numList))
    aStr = "dshadhlashdl"
    print(len(aStr))