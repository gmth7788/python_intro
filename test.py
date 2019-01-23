#!/usr/bin/python3
#coding=utf-8

import openpyxl
import random
import time

def read_login_sheet(file):
    wb = openpyxl.load_workbook(file)
    sheet = wb["数据列表"]

    title = []
    for i in sheet["1"]:
        print(i.value, end=" ")
        title.append(i.value)
    print("\n")
    print(title)

    name = []
    for i in sheet["2"]:
        print(i.value, end=" ")
        name.append(i.value)
    print("\n")
    print(name)

    z = zip(title, name)
    for i,j in z:
        print(i,j)

def get_random_str(len):
    return random.sample(
        'abcdefghijklmnopqrstuvwxyz0123456789', len)

def get_random_pwd(len):
    return random.sample(
        'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()', len)

def get_random_int(len):
    return random.sample('0123456789', len)

def get_random_mail():
    box = get_random_str(random.randint(4, 10))
    domain1 = get_random_str(random.randint(4, 10))
    domain2 = get_random_str(random.randint(4, 10))
    return box+'@'+domain1+'.'+domain2

def get_random_address():
    '''
    :return:返回随机产生的地址码字符串，GB/T2260
    '''
    # 地区
    region = (
        # 华北地区
        11,  # 北京市
        12,  # 天津市
        13,  # 河北省
        14,  # 山西省
        15,  # 内蒙古自治区
        # 东北地区：
        21,  # 辽宁省
        22,  # 吉林省
        23,  # 黑龙江省
        # 华东地区：
        31,  # 上海市
        32,  # 江苏省
        33,  # 浙江省
        34,  # 安徽省
        35,  # 福建省
        36,  # 江西省
        37,  # 山东省
        71,  # 台湾省(886)
        # 华中地区：
        41,  # 河南省
        42,  # 湖北省
        43,  # 湖南省
        # 华南地区：
        44,  # 广东省
        45,  # 广西壮族自治区
        46,  # 海南省
        81,  # 香港特别行政区（852)
        82,  # 澳门特别行政区（853)
        # 西南地区：
        51,  # 四川省
        52,  # 贵州省
        53,  # 云南省
        54,  # 西藏自治区
        50,  # 重庆市
        # 西北地区：
        61,  # 陕西省
        62,  # 甘肃省
        63,  # 青海省
        64,  # 宁夏回族自治区
        65,  # 新疆维吾尔自治区
    )
    reg = random.randint(1,len(region))

    # 市（地级市、自治州、地区、盟及直辖市所属区和县的汇总码）
    # 其中，01-20，51-70表示地级市；21-50表示地区（自治州、盟）。
    province = random.randint(1,70)

    # 县（区、县级市、旗）。
    # 01-18表示地级市、自治州、地区、盟辖县级市；
    # 21-80表示县（旗）；81-99表示省直辖县级行政单位。
    county = random.randint(1,80)

    return "{:02d}{:02d}{:02d}".format(
        reg, province, county)

def get_random_birthday():
    '''
    :return:返回随机生成的生日字符串，GB/T7408
    '''
    y = random.randint(1900, 2019)
    m = random.randint(1, 12)
    d = random.randint(1, 28)
    return "{:04d}{:02d}{:02d}".format(y,m,d)

def get_iso_7064_checksum(idcard):
    # 校验码
    checksum = (1,0,-1,9,8,7,6,5,4,3,2)

    # 加权因子
    weight_coef = (7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2)

    if len(idcard) < 17:
        return None
    w = 0
    for i in range(17):
        w += int(idcard[i]) * weight_coef[i]
    r = (12 - w % 11) % 11
    if r == 10:
        return idcard[:17]+'x'
    else:
        return idcard[:17] + str(r)

def get_random_idcardnumber():
    '''
    :return:返回随机产生的身份证号码，18位
    GB11643-1999《公民身份号码》
    六位数字地址码，八位数字出生日期码，三位数字顺序码和一位数字校验码
    其中：
    1）地址码，GB/T2260
    2）出生日期码，GB/T7408
    3）顺序码，第十五位到十七位，最后一位男偶女奇
    4）校验码，ISO 7064:1983.MOD 11-2计算校验码
    '''
    s = "{:s}{:s}{:02d}{:01d}".format(
        get_random_address(),
        get_random_birthday(),
        random.randint(1,99),
        random.randint(0,9))
    s = get_iso_7064_checksum(s)
    return s


def create_login_sheet(file, num):
    '''
    创建指定行数的"数据列表"
    :param file: 文件名
    :param num: 行数
    :return:
    '''
    t0 = time.time()
    wb = openpyxl.Workbook()
    ws_login = wb.create_sheet("数据列表", 0)

    title = ['userNO', 'name', 'id',
             'idCardNumber', 'description',
             'weight#int', 'gender', 'secLevel#int',
             'userOrg', 'userOrgname', 'telephone',
             'mobilePhone', 'fax', 'homeTelephoneNumber',
             'pagerTelephoneNumber', 'address',
             'postalCode', 'countryName', 'friendlyCountryName',
             'stateOrProvinceName', 'localityName',
             'streetAddress', 'email']

    name = [ '编号', '姓名', '登录名', '身份证号', '描述',
             '排序', '性别', '密级', '组织标识', '组织名称',
             '工作电话', '移动电话', '传真', '家庭电话',
             '寻呼机号码', '邮寄地址', '邮编', '国家英文缩写',
             '国家全称', '省', '市', '街道地址', '电子邮件'
             ]

    # 表头
    idx = range(1, len(title)+1)
    z = zip(title, idx)
    for t,i in z:
        ws_login.cell(row=1, column=i, value=t)

    idx = range(1, len(name)+1)
    z = zip(name, idx)
    for t,i in z:
        ws_login.cell(row=2, column=i, value=t)


    # 数据
    for i in range(2, num+2):
        # userNO 编号
        ws_login.cell(row=i, column=1,
                      value='lruser%04d' % (i-1))

        # name 姓名
        ws_login.cell(row=i, column=2,
                      value='lruser%04d' % (i-1))

        # id 登录名
        ws_login.cell(row=i, column=3, value="".join(
            random.sample('abcdefghijklmnopqrstuvwxyz!@#$%^&*()',
                          6)))

        # idCardNumber 身份证号
        ws_login.cell(row=i, column=4,
                      value=get_random_idcardnumber())

        # description 描述
        ws_login.cell(row=i, column=5,
                      value="".join(random.sample(
                          '0123456789x',10)))

        # weight#int 排序
        ws_login.cell(row=i, column=6,
                      value=random.randint(1,10))

        # gender 性别
        ws_login.cell(row=i, column=7,
                      value="".join(random.sample(
                          'MF',1)))

        # secLevel#int 密级
        ws_login.cell(row=i, column=8,
                      value=random.randint(1,10))

        # userOrg 组织标识
        ws_login.cell(row=i, column=9,
                      value="".join(random.sample(
                          '0123456789',10)))

        # userOrgname 组织名称
        ws_login.cell(row=i, column=10,
                      value="".join(random.sample(
            'abcdefghijklmnopqrstuvwxyz',10)))

        # telephone 工作电话
        ws_login.cell(row=i, column=11,
                      value="".join(random.sample(
                          '0123456789',8)))

        # mobilePhone 移动电话
        ws_login.cell(row=i, column=12,
                      value="".join(random.sample(
                          '0123456789',10)))

        # fax 传真
        ws_login.cell(row=i, column=13,
                      value="".join(random.sample(
                          '0123456789',8)))

        # homeTelephoneNumber 家庭电话
        ws_login.cell(row=i, column=14,
                      value="".join(random.sample(
                          '0123456789',8)))

        # pagerTelephoneNumber 寻呼机号码
        ws_login.cell(row=i, column=15,
                      value="".join(random.sample(
                          '0123456789',10)))

        # address 邮寄地址
        ws_login.cell(row=i, column=16,
                      value="".join(random.sample(
            'abcdefghijklmnopqrstuvwxyz',20)))

        # postalCode 邮编
        ws_login.cell(row=i, column=17,
                      value="".join(random.sample(
                          '0123456789',6)))

        # countryName 国家英文缩写
        ws_login.cell(row=i, column=18,
                      value="".join(random.sample(
                          'abcdefghijklmnopqrstuvwxyz',
                          3)))

        # friendlyCountryName 国家全称
        ws_login.cell(row=i, column=19,
                      value="".join(random.sample(
                          'abcdefghijklmnopqrstuvwxyz',
                          20)))

        # stateOrProvinceName 省
        ws_login.cell(row=i, column=20,
                      value="".join(random.sample(
                          'abcdefghijklmnopqrstuvwxyz',
                          10)))

        # localityName 市
        ws_login.cell(row=i, column=21,
                      value="".join(random.sample(
                          'abcdefghijklmnopqrstuvwxyz',
                          10)))

        # streetAddress 街道地址
        ws_login.cell(row=i, column=22,
                      value="".join(random.sample(
                          'abcdefghijklmnopqrstuvwxyz',
                          20)))

        # email 电子邮件
        ws_login.cell(row=i, column=23,
                      value="".join(random.sample(
                          'abcdefghijklmnopqrstuvwxyz',
                          5))+ r"@163.com")

    try:
        wb.save(file)
    except PermissionError as e:
        print(e)
    finally:
        t1 = time.time()
        print("耗时%0.2f秒." % (t1 - t0))




def str_format():
    title = ("剧名", "剩余票数", "票价", "日期")
    rec = (("凤还巢", 10, 30.16, "2019-2-5 19:30:00"),
           ("七星灯", 104, 40.52, "2019-2-7 19:30:00"),
           ("莱茵的黄金", 255, 30.16, "2019-2-6 18:00:00"),
           ("乌盆记", 3, 66.16, "2019-2-10 19:30:00"))
    sche = []
    for i in range(4):
        sche.append(zip(title, rec[i]))

    print("{:20s} {:10s} {:15s} {:20s}".format(title[0],
                                               title[1],
                                               title[2],
                                               title[3]))

    print("-"*60)
    for i in range(len(rec)):
        print("{:<20s} {:>10d} {:>10.2f} {:<20s}".format(rec[i][0],
                                                 rec[i][1],
                                                 rec[i][2],
                                                 rec[i][3]))
    

if __name__=="__main__":
    # str_format()
    # a = 10
    # b = 20
    # print(a and b)
    # print(a or b)
    # print(not a)

    create_login_sheet(r"D:\wangbin\my_workspace\python_intro\login.xlsx", 20000)
    # read_login_sheet(r"./user.xlsx")
