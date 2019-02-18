#!/usr/bin/python3
#coding=utf-8


class FuzzBool():

    def __init__(self, value=0.0):
        '''
        初始化私有属性__value
        :param value:
        '''
        try:
            if type(value) == float:
                f = value
            elif type(value) == str:
                f = float(value)
            else:
                f = 0.0
        except ValueError as e:
            f = 0.0
        self.__value = f if 0.0 <= f <= 1.0 else 0.0

    # ----------------------------
    # 逻辑操作符

    # 逻辑非
    def __invert__(self):
        '''
        位逻辑非，~
        :return:
        '''
        return FuzzBool(1.0 - self.__value)

    # 逻辑与
    def __and__(self, other):
        '''
        位逻辑与，&
        :return:
        '''
        return FuzzBool(min(self.__value, other.__value))

    def __iand__(self, other):
        '''
        增强版（in-place，原地修改）位逻辑与，&=
        :return:
        '''
        self.__value = min(self.__value, other.__value)
        return self

    def __rand__(self, other):
        '''
        互换操作符，self与other是不同数据类型的与操作
        位逻辑与，&
        :param other:
        :return:
        '''
        return self.__and__(self, other)

    # 逻辑或
    def __or__(self, other):
        '''
        位逻辑或，|
        :return:
        '''
        return FuzzBool(max(self.__value, other.__value))

    def __ior__(self, other):
        '''
        增强版（in-place，原地修改）位逻辑或，|
        :return:
        '''
        self.__value = max(self.__value, other.__value)
        return self

    def __ror__(self, other):
        '''
        互换操作符，self与other是不同数据类型的与操作
        位逻辑或，|
        :param other:
        :return:
        '''
        return self.__or__(self, other)

    # ----------------------------
    # eval()
    def __repr__(self):
        return ("{0}({1})".format(self.__class__.__name__,
                                  self.__value))

    # ----------------------------
    # str()
    def __str__(self):
        return str(self.__value)

    # ----------------------------
    # 数据类型转换
    def __bool__(self):
        return self.__value > 0.5

    def __int__(self):
        return round(self.__value)

    def __float__(self):
        return self.__value

    # ----------------------------
    # 比较操作符
    def __lt__(self, other):
        return self.__value < other.__value

    def __le__(self, other):
        return self.__value <= other.__value

    def __eq__(self, other):
        '''
        默认情况下，自定义类示例操作符==总是返回False，是可哈希的。
        重载__eq__()后，必须重载__hash__()才是可哈希的。
        :return:
        '''
        return self.__value == other.__value

    def __hash__(self):
        '''
        id()返回对象的内存地址，独一无二。
        :return:
        '''
        return hash(id(self))


    # ----------------------------
    # str.format()格式规约
    def __format__(self, format_spec):
        '''
        使用float.__format__()方法。
        :param format_spec:
        :return:
        '''
        return self.__value.__format__(format_spec)

    # ----------------------------
    # conjunction()和disjunction()
    @staticmethod
    def conjunction(*fuzzies):
        return FuzzBool(min([float(x) for x in fuzzies]))






if __name__=="__main__":
    pass

