# -*- coding: UTF-8 -*-
from UserDAO import *
from BookDAO import *
from AdminDAO import *
from BorrowDAO import *
from IllegalDAO import *
from RecommandDAO import *
from ObjectsClasses import *


class UserClient(object):
    def __init__(self):
        self.userdao = UserDAO()
        self.userlist = []
        self.userlist2 = []

    def MatchIsUser(self):
        userlist = []
        for item in userlist:
            userid = item[0]
            passwd = item[1]
            result = self.userdao.matchIsUser(userid, passwd)
            # if result == True:
            # 建立user对象
            # self.userlist.append()

    def GetUserShow(self):
        for item in self.userlist:
            self.userdao.GetUserShow(item.id)

    def GetUserType(self):
        for item in self.userlist:
            self.userdao.GetUserType(item.id)

    def InsertUserRecord(self):
        for item in self.userlist2:
            self.userdao.InsertUserRecord(item)

    def GetUserRecord(self):
        Dict1 = {'faculty': '信息学院', 'status': '在借'}
        Dict2 = {'gender': 'female', 'useridentity': '教师'}
        Dict3 = {'department': '理学院', 'age': '21', 'status': '正常'}
        self.userdao.GetUserRecord(Dict1)
        self.userdao.GetUserRecord(Dict2)
        self.userdao.GetUserRecord(Dict3)

    def GetUserTypeRecord(self):
        self.userdao.GetUserTypeRecord()

    def TestUserClient(self):
        self.MatchIsUser()
        self.GetUserShow()
        self.GetUserType()
        self.GetUserTypeRecord()


class BookClient(object):
    def __init__(self):
        self.bookdao = BookDAO()

    def GetAllBookRecord(self):
        self.bookdao.GetAllBookRecord(0)

    def GetBookByDis(self):
        listdesci = [u'数学', u'矿业技术', u'地质学', u'生物学', u'机械工业']
        for item in listdesci:
            self.bookdao.GetBookByDis(item)

    def GetBookByMaj(self):
        majorlist = [u'工业技术', u'数理科学与化学', u'天文地理学']
        for item in majorlist:
            self.bookdao.GetBookByMaj(item)

    def GetBookByName(self):
        namelist = [u'Java', u'Python', u'C++', u'人工智能', u'深度学习', u'机器学习',
                    u'土木', u'建筑', u'测量', u'结构', u'电路', u'电工']
        for item in namelist:
            self.bookdao.GetBookByName(item)

    def GetBookByField(self):
        Dict1 = {'author': u'韩国'}
        Dict2 = {'version': u'第一版', 'booklanguage': u'英文'}
        Dict3 = {'publisher': u'清华大学出版社', 'stack': u'一层', 'floor': '3'}
        self.bookdao.GetBookByField(Dict1)
        self.bookdao.GetBookByField(Dict2)
        self.bookdao.GetBookByField(Dict3)

    def TestBookClient(self):
        self.GetAllBookRecord()
        self.GetBookByDis()
        self.GetBookByMaj()
        self.GetBookByName()
        self.GetBookByField()


class AdminClient(object):
    def __init__(self):
        self.admindao = AdminDAO()

    def matchIsAdmin(self):
        adminlist = []
        for item in adminlist:
            self.admindao.matchIsAdmin(item[0], item[1])

    def GetAdminPermission(self):
        self.admindao.GetAdminPermission()

    def GetAdminRecord(self):
        Dict = {'adminid': '218493'}
        self.admindao.GetAdminRecord(Dict)

    def TestAdminClient(self):
        self.matchIsAdmin()
        self.GetAdminPermission()
        self.GetAdminRecord()


class BorrowClient(object):
    def __init__(self):
        self.borrowdao = BorrowDAO()

    def GetBorrowRecord(self):
        self.borrowdao.GetBorrowRecord(0)

    def GetBorrowRecordByField(self, Dict):
        Dict1 = {'borrowdate': '2011-06-14'}
        Dict2 = {'preretdate': '2011-09-07'}
        Dict3 = {'bookid': '100048'}
        self.borrowdao.GetBorrowRecordByField(Dict1)
        self.borrowdao.GetBorrowRecordByField(Dict2)
        self.borrowdao.GetBorrowRecordByField(Dict3)

    def InsertBorrowRecord(self, List):
        InsertBorrowList = ['20000', '30000', '2016-12-13', '2017-01-13', '2017-01-13']
        self.borrowdao.InsertBorrowRecord(InsertBorrowList)

    def BorrowBook(self):
        userindex = 10000
        bookindex = 10000
        for uid, bid in zip(list(range(userindex, userindex + 100)), list(range(bookindex, bookindex + 100))):
            self.borrowdao.BorrowBook(uid, bid)

    def ReturnOvertimeRecord(self):
        self.borrowdao.RetureOvertimeRecord()

    def UpdateBorrowRecord(self):
        table = "borrow"
        key1 = "borrowid"
        val1 = "10001"
        key2 = "status"
        val2 = "测试"
        self.borrowdao.UpdateBorrowRecord(table, key1, val1, key2, val2)

    def TestBorrowClient(self):
        self.GetBorrowRecord()
        self.GetBorrowRecordByField()
        self.InsertBorrowRecord()
        self.BorrowBook()
        self.ReturnOvertimeRecord()
        self.UpdateBorrowRecord()


class IllegalClient(object):
    def __init__(self):
        self.Illegaldao = IllegalDAO()

    def InsertIllegal(self):
        List = ['13000', '20000', '30000', '123.45', u'否', u'2016-12-31', u'超时']
        self.Illegaldao.InsertIllegal(List)

    def GetUserIllegal(self):
        Ile = {'illegalid': '10001'}
        self.Illegaldao.GetAllIlegal(Ile)

    def BorrowToIllega(self):
        self.Illegaldao.BorrowToIllega()

    def UpdateRecord(self):
        table = 'Illegal'
        key1 = 'illegalid'
        val1 = '13000'
        key2 = 'userid'
        val2 = '21000'
        self.Illegaldao.UpdateRecord(table, key1, val1, key2, val2)

    def TestIllegalClient(self):
        self.InsertIllegal()
        self.GetUserIllegal()
        self.BorrowToIllega()
        self.UpdateRecord()


class RecommandClient(object):
    def __init__(self):
        self.recommanddao = RecommandDAO()

    def InsertRecommandRecord(self):
        List = [('11000', '线性代数', '无名', '北京林业大学出版社', '第一版', '好看')]
        self.recommanddao.InsertRecommandRecord(List)

    def GetRecommandRecord(self):
        Dict = {'userid': '11000'}
        self.recommanddao.GetRecommandRecord(Dict)

    def TestRecommandClient(self):
        self.InsertRecommandRecord()
        self.GetRecommandRecord()

class Client(object):
    def __init__(self):
        TestUserClient = UserClient()
        TestUserClient.TestUserClient()
        TestBookClient = BookClient()
        TestBookClient.TestBookClient()
        TestAdminClient = AdminClient()
        TestAdminClient.TestAdminClient()
        TestBorrowClient = BorrowClient()
        TestBorrowClient.TestBorrowClient()
        TestIllegalClient = IllegalClient()
        TestIllegalClient.TestIllegalClient()
        TestRecommandClient = RecommandClient()
        TestRecommandClient.TestRecommandClient()

if __name__ == '__main__':
    Client()
