# -*- coding: UTF-8 -*-

import pymysql
import random
import time
import datetime

surnames = [u'赵', u'钱', u'孙', u'李', u'周', u'吴', u'郑', u'王']
malefirstnames = [u'子', u'之', u'川', u'山', u'士', u'冉', u'羽', u'毅', u'海', u'涛']
malesecondnames = [u'豪', u'昱', u'博', u'凯', u'睿', u'聪', u'明', u'辉', u'勇', u'强', ]
femalefirstnames = [u'洁', u'婷', u'琦', u'琪', u'佳', u'嘉', u'舒', u'诗', u'雅', u'韵']
femalesecondnames = [u'熙', u'菲', u'彤', u'珞', u'瑜', u'雨', u'欣', u'宜', u'敏', u'姗']
connectionhead = ['188', '131', '130', '139', '157']
identities = [u'本科', u'硕士', u'博士', u'教师']
maxborrows = [15, 20, 25, 30]
maxrecoms = [3, 4, 5, 10]
durations = [30, 60, 90, 120]
faculties = [u'信息学院', u'工学院', u'理学院']
departmentsInfo = [u'网工', u'计科', u'物联网', u'数媒', u'信息']
departmentsIns = [u'电气', u'自动化', u'车辆', u'机械']
departmentsSci = [u'数学', u'电子']
statues = [u'正常', u'在借', u'损坏', u'超时']
majors = [u'工业技术', u'数理科学与化学', u'天文地理学']
discIns = [u'计算机技术', u'矿业技术', u'机械工业', u'建筑科学', u'电子技术']
discSci = [u'数学', u'物理学', u'化学', u'材料学', u'生物学']
discAst = [u'天文学', u'测绘学', u'海洋学', u'地质学', u'气象学']
keywordsIns = [u'Java', u'Python', u'C++', u'人工智能', u'深度学习', u'机器学习', u'勘探', u'矿石', u'石油', u'地下',
               u'地上', u'天然气', u'机床', u'CAD', u'零件', u'传动', u'机械', u'机电', u'园林', u'规划',
               u'土木', u'建筑', u'测量', u'结构', u'电路', u'电工', u'电子', u'线路', u'半导体', u'机器人']
keywordsSci = [u'几何', u'代数', u'拓扑', u'微积分', u'常微分', u'函数', u'力学', u'热学', u'光学', u'电学',
               u'相对论', u'物理', u'有机化学', u'无机化学', u'高分子', u'新能源', u'能源', u'生物化学', u'金属', u'木材',
               u'岩石', u'流体', u'有机', u'塑料', u'微生物学', u'细胞学', u'动物学', u'植物学', u'人类学', u'古生物学']
keywordsAst = [u'天体力学', u'宇宙学', u'天体测量学', u'空间天文学', u'射电天文学', u'恒星天文学', u'地籍学', u'制图学', u'测量学', u'测绘',
               u'遥感', u'地理信息', u'潜水', u'海洋环境', u'洋流', u'潮汐', u'堤坝', u'航线', u'矿物学', u'岩石学',
               u'地球化学', u'地层学', u'地球化学', u'构造地质学', u'大气探测', u'预报学', u'气象学', u'天气学', u'应用气象学', u'气候学']
midkeywords = [u'高级', u'中级', u'初级', u'通用', u'进阶', u'基础', u'综合', u'新版', u'分析', u'总结']
tailkeywords = [u'理论', u'技术', u'概论', u'科学', u'研究', u'指南', u'教程', u'手册', u'期刊', u'应用']
publishes = [u"清华大学出版社", u"国家科学出版社", u"机械工业出版社", u"人民邮电出版社",
             u"中国科研出版社", u"北京林业大学出版社", u"北京大学出版社", u"自然科学出版社"]
authorsurname = [u"蒋", u"沈", u"韩", u"杨", u"朱", u"秦", u"尤", u"许"]
authornames = [u"军", u"平", u"斌", u"强", u"建", u"伟", u"磊", u"刚", u"鹏", u"国"]
stacks = [u'一层', u'二层', u'三层', u'四层', u'五层']
datestart = time.mktime((1995, 1, 1, 0, 0, 0, 0, 0, 0))
dateend = time.mktime((2018, 12, 31, 23, 59, 59, 0, 0, 0))
recomreasons = [u"这本书对我的学习有益", u"教学过程中需要这本书", u"深入简出引人入胜", u"专业领域内的经典", u"非常希望获取书中的知识",
                    u"内容考究严谨", u"充满冶学精神与人文关怀", u"书中例子和图表丰富", u"语言朴实进人引人入胜", u"内容生动有趣寓教于乐",
                    u"对于初学者很友好", u"适合行业内专家阅读", u"它是极好的工具书", u"可以给予读者教材之外的启发", u"师生皆宜编著精巧"]

def ConnectMySQL():
    user = "lsm"
    passwd = "12345678"
    host = "188.131.178.78"
    post = "3306"
    database = "libmanasys"
    try:
        dbhandle = pymysql.connect(host, user, passwd, database)
        print("Connect to database:{} user:{} host:{}".format(database, user, host))
        return dbhandle
    except Exception as e:
        print(e)


def ExecuteSQL(dbhandle, sql):
    print(sql)
    try:
        cursor = dbhandle.cursor()
        cursor.execute(sql)
        dbhandle.commit()
    except Exception as e:
        dbhandle.rollback()
        print(e)


def SearchSQL(dbhandle, sql):
    try:
        cursor = dbhandle.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        dbhandle.rollback()
        print(e)


def CreateUser(userid):
    userid = str(userid)
    name = ""
    name += random.choice(surnames)
    password = ''.join(random.sample('0123456789', 6))
    if random.randint(0, 1) == 0:
        gender = "male"
        name += malefirstnames[random.randint(0, 9)]
        name += malesecondnames[random.randint(0, 9)]
    else:
        gender = "female"
        name += femalefirstnames[random.randint(0, 9)]
        name += femalesecondnames[random.randint(0, 9)]
    connection = ""
    connection += connectionhead[random.randint(0, 3)]
    connection += ''.join(random.sample('0123456789', 10))
    identityindex = random.randint(0, 20)
    if identityindex < 10:
        identityindex = 0
        age = random.randint(18, 22)
    elif identityindex >= 10 and identityindex <= 13:
        identityindex = 1
        age = random.randint(23, 25)
    elif identityindex > 13 and identityindex <= 16:
        identityindex = 2
        age = random.randint(26, 28)
    else:
        identityindex = 3
        age = random.randint(29, 55)
    facultyindex = random.randint(0, 2)
    faculty = faculties[facultyindex]
    if facultyindex == 0:
        department = departmentsInfo[random.randint(0, 4)]
    elif facultyindex == 1:
        department = departmentsIns[random.randint(0, 3)]
    else:
        department = departmentsSci[random.randint(0, 1)]
    identity = identities[identityindex]
    statusindex = random.randint(0, 9)
    if statusindex == 9:
        status = statues[3]
    elif statusindex == 8:
        status = statues[2]
    elif statusindex <= 7 and statusindex >= 5:
        status = statues[1]
    else:
        status = statues[0]
    return [userid, name, password, faculty, department, age, gender, identity, connection, status]


def CreateUserTable(dbhandle):
    sql = "CREATE TABLE user(" \
          "userid VARCHAR(20) NOT NULL PRIMARY KEY," \
          "username VARCHAR(20) NOT NULL," \
          "password VARCHAR(20) NOT NULL," \
          "faculty VARCHAR(20) NOT NULL," \
          "department VARCHAR(20) NOT NULL," \
          "age TINYINT UNSIGNED DEFAULT 20," \
          "gender VARCHAR(10) DEFAULT 'male'," \
          "useridentity VARCHAR(20) NOT NULL," \
          "userconnection VARCHAR(20) NOT NULL," \
          "status VARCHAR(20) NOT NULL" \
          ")" \
          "engine=innodb DEFAULT charset=utf8;"
    ExecuteSQL(dbhandle, sql)


def InsertUserTable(dbhandle):
    for i in range(0, 1000):
        user = CreateUser(10000 + i)
        sql = "INSERT INTO user(" \
              "userid,username,password,faculty,department,age,gender,useridentity,userconnection,status)" \
              " VALUES(" \
              "'{}','{}','{}','{}','{}',{},'{}','{}','{}','{}'" \
              ");".format(user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7], user[8], user[9])
        ExecuteSQL(dbhandle, sql)


def CreateBook(bookid):
    bookid = str(bookid)
    pages = random.randint(100, 600)
    isbn = "{}-{}-{}-{}-{}".format(''.join(random.sample('0123456789', 3)), ''.join(random.sample('0123456789', 3)),
                                   ''.join(random.sample('0123456789', 4)), ''.join(random.sample('0123456789', 2)),
                                   ''.join(random.sample('0123456789', 1)))
    majorindex = random.randint(0, 2)
    discindex = random.randint(0, 4)
    major = majors[majorindex]
    bookname = ""
    if majorindex == 0:
        discipline = discIns[discindex]
        bookname = ''.join(random.sample(keywordsIns[discindex * 6:(discindex + 1) * 6 - 1], 2))
    elif majorindex == 1:
        discipline = discSci[discindex]
        bookname = ''.join(random.sample(keywordsSci[discindex * 6:(discindex + 1) * 6 - 1], 2))
    else:
        discipline = discAst[discindex]
        bookname = ''.join(random.sample(keywordsAst[discindex * 6:(discindex + 1) * 6 - 1], 2))
    if random.randint(0, 4) == 0:
        booklanguage = u"英文"
    else:
        booklanguage = u"中文"
    bookname += midkeywords[random.randint(0, 9)]
    bookname += tailkeywords[random.randint(0, 9)]
    publisher = publishes[random.randint(0, 7)]
    abstract = ""
    author = authorsurname[random.randint(0, 7)]
    author += authornames[random.randint(0, 9)]
    if random.randint(0, 1) == 0:
        author += authornames[random.randint(0, 9)]
    timestamp = random.randint(datestart, dateend)
    datetuple = time.localtime(timestamp)
    collecttime = time.strftime("%Y-%m-%d", datetuple)
    versionindex = random.randint(0, 2)
    if versionindex == 0:
        version = u"第一版"
    elif versionindex == 1:
        version = u"第二版"
    else:
        version = u"第三版"
    statusindex = random.randint(0, 9)
    if statusindex == 9:
        status = statues[3]
    elif statusindex == 8:
        status = statues[2]
    elif statusindex <= 7 and statusindex >= 5:
        status = statues[1]
    else:
        status = statues[0]
    stack = stacks[random.randint(0, 4)]
    shelf = random.randint(1, 30)
    floor = random.randint(1, 5)
    bookvalue = round(random.uniform(10, 300), 2)
    return [bookid, bookname, author, pages, collecttime, version, major,
            discipline, isbn, booklanguage, publisher, status, abstract,
            stack, shelf, floor, bookvalue]


def CreateBookTable(dbhandle):
    sql = "CREATE TABLE book(" \
          "bookid VARCHAR(20) NOT NULL PRIMARY KEY," \
          "bookname VARCHAR(20) NOT NULL," \
          "author VARCHAR(20) NOT NULL," \
          "pages SMALLINT UNSIGNED," \
          "collecttime DATE NOT NULL," \
          "version VARCHAR(20) NOT NULL," \
          "major VARCHAR(20) NOT NULL," \
          "discipline VARCHAR(20) NOT NULL," \
          "isbn VARCHAR(30) NOT NULL," \
          "booklanguage VARCHAR(20) NOT NULL," \
          "publisher VARCHAR(20) NOT NULL," \
          "status VARCHAR(20) NOT NULL," \
          "abstract TEXT," \
          "stack VARCHAR(20) NOT NULL," \
          "shelf TINYINT NOT NULL," \
          "floor TINYINT NOT NULL," \
          "bookvalue FLOAT NOT NULL" \
          ")" \
          "engine=innodb DEFAULT charset=utf8;"
    ExecuteSQL(dbhandle, sql)


def InsertBookTable(dbhandle):
    for i in range(10000):
        book = CreateBook(100000 + i)
        sql = "INSERT INTO book(" \
              "bookid, bookname, author, pages, collecttime, version, major, discipline, isbn, " \
              "booklanguage, publisher, status, abstract, stack, shelf, floor, bookvalue)" \
              " VALUES(" \
              "'{}','{}','{}',{},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}', {}, {}, {}" \
              ");".format(book[0], book[1], book[2], book[3], book[4], book[5], book[6], book[7], book[8], book[9],
                          book[10], book[11], book[12], book[13], book[14], book[15], book[16])
        ExecuteSQL(dbhandle, sql)


def CreateBorrowTable(dbhandle):
    sql = "CREATE TABLE borrow(" \
          "borrowid VARCHAR(20) NOT NULL PRIMARY KEY," \
          "userid VARCHAR(20) NOT NULL," \
          "bookid VARCHAR(20) NOT NULL," \
          "borrowdate DATE NOT NULL," \
          "presretdate DATE," \
          "actretdate DATE NOT NULL" \
          ")" \
          "engine=innodb DEFAULT charset=utf8;"
    ExecuteSQL(dbhandle, sql)


def InsertBorrowTable(dbhandle):
    sql1 = "SELECT bookid,collecttime FROM book WHERE status = '在借'"
    sql2 = "SELECT userid,useridentity FROM user WHERE status = '在借'"
    resultbook = SearchSQL(dbhandle, sql1)
    resultuser = SearchSQL(dbhandle, sql2)
    borrowid = 10001
    startindex = 0
    endindex = 0
    for user in resultuser:
        sql3 = "SELECT duration FROM usertype WHERE useridentity='{}'".format(user[1])
        duration = int(SearchSQL(dbhandle, sql3)[0][0])
        if user[0] != resultuser[-1][0]:
            if random.randint(1, 10) == 1:
                booknumber = 10
            else:
                booknumber = 11
            endindex += booknumber
            for book in resultbook[startindex:endindex]:
                borrowdate = book[1] + datetime.timedelta(random.randint(1, 1000))
                actretdate = borrowdate + datetime.timedelta(duration)
                presretdate = actretdate - datetime.timedelta(random.randint(1, 10))
                sql = "INSERT INTO borrow" \
                      "(borrowid,userid,bookid,borrowdate,presretdate,actretdate) " \
                      "VALUES" \
                      "('{}','{}','{}','{}','{}','{}'" \
                      ");".format(borrowid, user[0], book[0], borrowdate, presretdate, actretdate)
                ExecuteSQL(dbhandle, sql)
                borrowid += 1
        else:
            for book in resultbook[startindex:]:
                borrowdate = book[1] + datetime.timedelta(random.randint(1, 1000))
                actretdate = borrowdate + datetime.timedelta(duration)
                presretdate = actretdate - datetime.timedelta(random.randint(1, 10))
                sql = "INSERT INTO borrow" \
                      "(borrowid,userid,bookid,borrowdate,presretdate,actretdate) " \
                      "VALUES" \
                      "('{}','{}','{}','{}','{}','{}'" \
                      ");".format(borrowid, user[0], book[0], borrowdate, presretdate, actretdate)
                ExecuteSQL(dbhandle, sql)
                borrowid += 1
        startindex = endindex
    return borrowid


def CreateIllegalTable(dbhandle):
    sql = "CREATE TABLE Illegal(" \
          "illegalid VARCHAR(20) NOT NULL PRIMARY KEY," \
          "userid VARCHAR(20) NOT NULL," \
          "bookid VARCHAR(20) NOT NULL," \
          "amount FLOAT NOT NULL," \
          "isprocessed VARCHAR(5) NOT NULL," \
          "illegaldate DATE NOT NULL," \
          "illegaltype VARCHAR(20) NOT NULL" \
          ")" \
          "engine=innodb DEFAULT charset=utf8;"
    ExecuteSQL(dbhandle, sql)


def InsertIllegalTable(dbhandle):
    sql1 = "SELECT bookid,bookvalue,collecttime FROM book WHERE status = '损坏'"
    sql2 = "SELECT userid FROM user WHERE status = '损坏'"
    resultbook1 = SearchSQL(dbhandle, sql1)
    resultuser1 = SearchSQL(dbhandle, sql2)
    illegalid = 10001
    startindex = 0
    endindex = 0
    for user in resultuser1:
        if user[0] != resultuser1[-1][0]:
            booknumberindex = random.randint(1, 5)
            if booknumberindex == 1 or booknumberindex == 2:
                booknumber = 10
            else:
                booknumber = 9
            endindex += booknumber
            for book in resultbook1[startindex:endindex]:
                illegaldate = book[2] + datetime.timedelta(random.randint(1, 1000))
                sql = "INSERT INTO Illegal" \
                      "(illegalid,userid,bookid,amount,isprocessed,illegaldate,illegaltype) " \
                      "VALUES" \
                      "('{}','{}','{}',{},'否','{}','损坏'" \
                      ");".format(illegalid, user[0], book[0], book[1], illegaldate)
                ExecuteSQL(dbhandle, sql)
                illegalid += 1
        else:
            for book in resultbook1[startindex:]:
                illegaldate = book[2] + datetime.timedelta(random.randint(1, 1000))
                sql = "INSERT INTO Illegal" \
                      "(illegalid,userid,bookid,amount,isprocessed,illegaldate,illegaltype) " \
                      "VALUES" \
                      "('{}','{}','{}',{},'否','{}','损坏'" \
                      ");".format(illegalid, user[0], book[0], book[1], illegaldate)
                ExecuteSQL(dbhandle, sql)
                illegalid += 1
        startindex = endindex
    return illegalid


def InsertIllegalAndBorrowTable(dbhandle, illegalid, borrowid):
    illegalid += 1
    borrowid += 1
    sql1 = "SELECT bookid,collecttime,bookvalue FROM book WHERE status = '超时'"
    sql2 = "SELECT userid,useridentity FROM user WHERE status = '超时'"
    resultbook = SearchSQL(dbhandle, sql1)
    resultuser = SearchSQL(dbhandle, sql2)
    startindex = 0
    endindex = 0
    for user in resultuser:
        sql3 = "SELECT duration FROM usertype WHERE useridentity='{}'".format(user[1])
        duration = int(SearchSQL(dbhandle, sql3)[0][0])
        amount = round(random.uniform(0, 10), 2)
        if user[0] != resultuser[-1][0]:
            booknumberindex = random.randint(1, 6)
            if booknumberindex == 1:
                booknumber = 9
            else:
                booknumber = 10
            endindex += booknumber
            for book in resultbook[startindex:endindex]:
                borrowdate = book[1] + datetime.timedelta(random.randint(1, 1000))
                actretdate = borrowdate + datetime.timedelta(duration)
                # presretdate = actretdate - datetime.timedelta(random.randint(1, 10))
                sql = "INSERT INTO borrow" \
                      "(borrowid,userid,bookid,borrowdate,presretdate,actretdate) " \
                      "VALUES" \
                      "('{}','{}','{}','{}','{}','{}'" \
                      ");".format(borrowid, user[0], book[0], borrowdate, "0000-00-00", actretdate)
                # print(sql)
                ExecuteSQL(dbhandle, sql)
                borrowid += 1
                illegaldate = actretdate
                sql = "INSERT INTO Illegal" \
                      "(illegalid,userid,bookid,amount,isprocessed,illegaldate,illegaltype) " \
                      "VALUES" \
                      "('{}','{}','{}',{},'否','{}','超时'" \
                      ");".format(illegalid, user[0], book[0], amount, illegaldate)
                # print(sql)
                ExecuteSQL(dbhandle, sql)
                illegalid += 1
        else:
            for book in resultbook[startindex:]:
                borrowdate = book[1] + datetime.timedelta(random.randint(1, 1000))
                actretdate = borrowdate + datetime.timedelta(duration)
                presretdate = actretdate - datetime.timedelta(random.randint(1, 10))
                sql = "INSERT INTO borrow" \
                      "(borrowid,userid,bookid,borrowdate,presretdate,actretdate) " \
                      "VALUES" \
                      "('{}','{}','{}','{}','{}','{}'" \
                      ");".format(borrowid, user[0], book[0], borrowdate, "0000-00-00", actretdate)
                # print(sql)
                ExecuteSQL(dbhandle, sql)
                borrowid += 1
                illegaldate = actretdate
                sql = "INSERT INTO Illegal" \
                      "(illegalid,userid,bookid,amount,isprocessed,illegaldate,illegaltype) " \
                      "VALUES" \
                      "('{}','{}','{}',{},'否','{}','超时'" \
                      ");".format(illegalid, user[0], book[0], amount, illegaldate)
                # print(sql)
                ExecuteSQL(dbhandle, sql)
                illegalid += 1
        startindex = endindex


def CreateRecomTable(dbhandle):
    sql = "CREATE TABLE recommand(" \
          "userid VARCHAR(20) NOT NULL," \
          "bookname VARCHAR(20) NOT NULL," \
          "author VARCHAR(20) NOT NULL," \
          "publisher VARCHAR(20) NOT NULL," \
          "version VARCHAR(20) NOT NULL," \
          "recomreason TEXT(200)," \
          "statue VARCHAR(20) NOT NULL," \
          "CONSTRAINT recompk PRIMARY KEY" \
          "(userid, bookname, author, publisher, version)" \
          ")" \
          "engine=innodb DEFAULT charset=utf8;"
    ExecuteSQL(dbhandle, sql)


def InsertRecomTable(dbhandle):
    sql1 = "SELECT userid FROM user limit 100;"
    resultuser = SearchSQL(dbhandle, sql1)
    for user in resultuser:
        userid = user[0]
        majorindex = random.randint(0, 2)
        discindex = random.randint(0, 4)
        if majorindex == 0:
            bookname = ''.join(random.sample(keywordsIns[discindex * 6:(discindex + 1) * 6 - 1], 2))
        elif majorindex == 1:
            bookname = ''.join(random.sample(keywordsSci[discindex * 6:(discindex + 1) * 6 - 1], 2))
        else:
            bookname = ''.join(random.sample(keywordsAst[discindex * 6:(discindex + 1) * 6 - 1], 2))
        bookname += midkeywords[random.randint(0, 9)]
        bookname += tailkeywords[random.randint(0, 9)]
        author = authorsurname[random.randint(0, 7)]
        author += authornames[random.randint(0, 9)]
        if random.randint(0, 1) == 0:
            author += authornames[random.randint(0, 9)]
        publisher = publishes[random.randint(0, 7)]
        versionindex = random.randint(0, 2)
        if versionindex == 0:
            version = u"第一版"
        elif versionindex == 1:
            version = u"第二版"
        else:
            version = u"第三版"
        recomreason = ','.join(random.sample(recomreasons, random.randint(2, 5)))
        recomreason +=  '。'
        sql = "INSERT INTO recommand (" \
              "userid, bookname, author, publisher, version, recomreason, statue)" \
              " VALUES(" \
              "'{}','{}','{}','{}','{}','{}','{}'" \
              ");".format(userid, bookname, author, publisher, version, recomreason, "待定")
        ExecuteSQL(dbhandle, sql)

def CreateUsertypeTable(dbhandle):
    sql = "CREATE TABLE usertype(" \
          "useridentity VARCHAR(20) NOT NULL PRIMARY KEY," \
          "maxborrow TINYINT NOT NULL," \
          "maxrecom TINYINT NOT NULL," \
          "duration TINYINT NOT NULL)" \
          "engine=innodb DEFAULT charset=utf8;"
    ExecuteSQL(dbhandle, sql)


def InsertUsertype(dbhandle):
    for identity, maxborrow, maxrecom, duration in zip(identities, maxborrows, maxrecoms, durations):
        sql = "INSERT INTO usertype(" \
              "useridentity,maxborrow,maxrecom,duration)" \
              "VALUES" \
              "('{}',{},{},{}" \
              ");".format(identity, maxborrow, maxrecom, duration)
        ExecuteSQL(dbhandle, sql)


def CreateAndInsertAdminTable(dbhandle):
    sql = "CREATE TABLE admin(" \
          "adminid VARCHAR(20) NOT NULL PRIMARY KEY," \
          "passwd VARCHAR(20) NOT NULL," \
          "connecttion VARCHAR (20) NOT NULL," \
          "adminpri TINYINT NOT NULL" \
          ")" \
          "engine=innodb DEFAULT charset=utf8;"
    ExecuteSQL(dbhandle, sql)

    for i in range(0, 7):
        adminid = ''.join(random.sample('123456789', 6))
        passwd = ''.join(random.sample('123456789', 6))
        connection = connectionhead[random.randint(0, 3)]
        connection += ''.join(random.sample('0123456789', 10))
        sql = "INSERT INTO admin(" \
              "adminid, passwd, connecttion, adminpri)" \
              "VALUES(" \
              "'{}','{}','{}',{}" \
              ");".format(adminid, passwd, connection, i)
        ExecuteSQL(dbhandle, sql)


if __name__ == '__main__':
    dbhandle = ConnectMySQL()
    CreateUserTable(dbhandle)
    InsertUserTable(dbhandle)
    CreateBookTable(dbhandle)
    InsertBookTable(dbhandle)
    CreateBorrowTable(dbhandle)
    borrowid = InsertBorrowTable(dbhandle)
    CreateIllegalTable(dbhandle)
    illegalid = InsertIllegalTable(dbhandle)
    InsertIllegalAndBorrowTable(dbhandle, illegalid, borrowid)
    CreateRecomTable(dbhandle)
    InsertRecomTable(dbhandle)
    CreateUsertypeTable(dbhandle)
    InsertUsertype(dbhandle)
    CreateAndInsertAdminTable(dbhandle)
    dbhandle.close()
