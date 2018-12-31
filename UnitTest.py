# -*- coding: UTF-8 -*-
from UserAPI import User, UserAPI
from BookAPI import Book, BookAPI
from AdminAPI import Admin, AdminAPI
from BorrowAPI import Borrow, BorrowAPI
from illegalAPI import Illegal, IllegalAPI
from RecommandAPI import Recommand, RecommandAPI
from UserType import UserTypeAPI
from MiddleLayer import MiddleLayer
import os

logfile = open("UnitTestLog", "w")


def Display(result):
    print(result, file=logfile)


class UserClient(object):
    def __init__(self):
        self.userapi = UserAPI()

    def MatchIsUser(self):
        print(self.userapi.matchIsUser('10973', '941075'))

    def GetUserShow(self):
        Display(self.userapi.GetUserShow('10001'))

    def InsertUserRecord(self):
        user = User()
        user.setid('11002')
        user.setusername('sanshui')
        user.setpassword('123456')
        user.setfaculty('信息')
        user.setdepartment('计算机')
        user.setage('20')
        user.setgendar('female')
        user.setuseridentity('硕士')
        user.setuserconnection('8088888')
        user.setstatus('正常')
        try:
            self.userapi.InsertUserRecord(user)
            print("InsertUserRecord-OK", file=logfile)
        except:
            print("InsertUserRecord-Error", file=logfile)

    def GetUserRecord(self):
        Dict1 = {'faculty': '信息学院', 'status': '在借'}
        Dict2 = {'gender': 'female', 'useridentity': '教师'}
        Dict3 = {'department': '理学院', 'age': '21', 'status': '正常'}
        Display(self.userapi.GetUserRecord(Dict1))
        Display(self.userapi.GetUserRecord(Dict2))
        Display(self.userapi.GetUserRecord(Dict3))

    def DeleteRecord(self):
        table = 'user'
        key = 'userid'
        val = '10088'
        try:
            self.userapi.DeleteRecord(table, key, val)
            print("DeleteUserRecord-OK", file=logfile)
        except:
            print("DeleteUserRecord-Error", file=logfile)

    def TestUserClient(self):
        self.MatchIsUser()
        self.GetUserShow()
        self.InsertUserRecord()
        self.GetUserRecord()


class AdminClient(object):
    def __init__(self):
        self.adminapi = AdminAPI()

    def matchIsAdmin(self):
        print(self.adminapi.matchIsAdmin('256491', '439628'), file=logfile)

    def GetAdminPermission(self):
        print(self.adminapi.GetAdminPermission('168452'), file=logfile)

    def GetAdminRecord(self):
        Display(self.adminapi.GetAllAdminRecord())

    def TestAdminClient(self):
        self.matchIsAdmin()
        self.GetAdminPermission()
        self.GetAdminRecord()


class BookClient(object):
    def __init__(self):
        self.bookapi = BookAPI()

    def GetAllBookRecord(self):
        Display(self.bookapi.GetAllBookRecord(1000))

    def GetBookByDis(self):
        listdesci = [u'数学', u'矿业技术', u'地质学', u'生物学', u'机械工业']
        for item in listdesci:
            Display(self.bookapi.GetBookByDis(item))

    def GetBookByMaj(self):
        majorlist = [u'工业技术', u'数理科学与化学', u'天文地理学']
        for item in majorlist:
            Display(self.bookapi.GetBookByMaj(item))

    def GetBookByName(self):
        namelist = [u'Java', u'Python', u'C++', u'人工智能', u'深度学习', u'机器学习',
                    u'土木', u'建筑', u'测量', u'结构', u'电路', u'电工']
        for item in namelist:
            Display(self.bookapi.GetBookByName(item))

    def GetBookByField(self):
        book1 = Book()
        book1.set_author(u'韩国')
        book2 = Book()
        book2.set_version(u'第一版')
        book2.set_booklanguage(u'英文')
        book3 = Book()
        book3.set_publisher(u'清华大学出版社')
        book3.set_stack(u'一层')
        book3.set_floor(3)
        Display(self.bookapi.GetBookByField(book1))
        Display(self.bookapi.GetBookByField(book2))
        Display(self.bookapi.GetBookByField(book3))

    def InsertBookRecord(self):
        test = Book()
        test.set_bookid('300001')
        test.set_bookname('1')
        test.set_author('1')
        test.set_pages('1')
        test.set_collecttime('2010-09-17')
        test.set_version('1')
        test.set_major('1')
        test.set_discipline('1')
        test.set_isbn('133-314-2343-16-2')
        test.set_booklanguage('1')
        test.set_publisher('1')
        test.set_status('1')
        test.set_abstract('1')
        test.set_stack('1')
        test.set_shelf('1')
        test.set_floor('2')
        test.set_bookvalue('1')
        try:
            self.bookapi.InsertBookRecord(test)
            print("InsertBookRecord-OK", file=logfile)
        except:
            print("InsertBookRecord-Error", file=logfile)

    def UpdateRecord(self):
        try:
            self.bookapi.UpdateRecord('book', 'bookid', '300000', 'bookid', '300001')
            print("DeleteBookRecord-OK", file=logfile)
        except:
            print("DeleteBookRecord-Error", file=logfile)

    def DeleteRecord(self):
        try:
            self.bookapi.DeleteRecord('book', 'bookid', '300000')
            print("DeleteBookRecord-OK", file=logfile)
        except:
            print("DeleteBookRecord-Error", file=logfile)

    def TestBookClient(self):
        self.GetAllBookRecord()
        self.GetBookByDis()
        self.GetBookByMaj()
        self.GetBookByName()
        self.GetBookByField()
        self.InsertBookRecord()
        self.UpdateRecord()
        self.DeleteRecord()


class BorrowClient(object):
    def __init__(self):
        self.borrowapi = BorrowAPI()

    def GetBorrowRecord(self):
        Display(self.borrowapi.GetBorrowRecord(100))

    def GetBorrowRecordByField(self):
        borrow1 = Borrow()
        borrow1.set_borrowdate('2011-06-14')
        borrow2 = Borrow()
        borrow2.set_presretdate('2011-09-07')
        borrow3 = Borrow()
        borrow3.set_bookid('100048')
        Display(self.borrowapi.GetBorrowRecordByField(borrow1))
        Display(self.borrowapi.GetBorrowRecordByField(borrow2))
        Display(self.borrowapi.GetBorrowRecordByField(borrow3))

    def InsertBorrowRecord(self):
        test = Borrow()
        test.set_borrowid('50000')
        test.set_userid('10000')
        test.set_bookid('100000')
        test.set_borrowdate('2017-03-06')
        test.set_presretdate('2017-03-20')
        test.set_actretdate('2017-05-09')
        try:
            self.borrowapi.InsertBorrowRecord(test)
            print("InsertBorrowRecord-OK", file=logfile)
        except:
            print("InsertBookRecord-Error", file=logfile)

    def BorrowBook(self):
        uid = 10000
        bid = 100001
        try:
            self.borrowapi.BorrowBook(str(uid), str(bid))
            print("BorrowBook-OK", file=logfile)
        except:
            print("BorrowBook-Error", file=logfile)

    def ReturnOvertimeRecord(self):
        Display(self.borrowapi.RetureIllegalRecord())

    def UpdateBorrowRecord(self):
        table = "borrow"
        key1 = "borrowid"
        val1 = "10001"
        key2 = "status"
        val2 = "测试"
        try:
            self.borrowapi.UpdateRecord(table, key1, val1, key2, val2)
            print("UpdateBorrowRecord-OK", file=logfile)
        except:
            print("UpdateBorrowRecord-Error", file=logfile)

    def TestBorrowClient(self):
        self.GetBorrowRecord()
        self.GetBorrowRecordByField()
        self.InsertBorrowRecord()
        self.BorrowBook()
        self.ReturnOvertimeRecord()
        self.UpdateBorrowRecord()


class IllegalClient(object):
    def __init__(self):
        self.Illegalapi = IllegalAPI()

    def InsertIllegal(self):
        mid = Illegal()
        mid.set_illegalid('30000')
        mid.set_userid('100005')
        mid.set_bookid('10003')
        mid.set_amount('10')
        mid.set_isprocessed('否')
        mid.set_illegaldate('2000-05-02')
        mid.set_illegaltype('损坏')
        try:
            self.Illegalapi.InsertIllegal(mid)
            print("InsertIllegal-OK", file=logfile)
        except:
            print("InsertIllegal-Error", file=logfile)

    def GetUserIllegal(self):
        ile = Illegal()
        ile.set_illegalid('10010')
        Display(self.Illegalapi.GetUserIllegal(ile))

    def BorrowToIllega(self):
        Display(self.Illegalapi.BorrowToIllega())

    def UpdateRecord(self):
        table = 'Illegal'
        key1 = 'illegalid'
        val1 = '13000'
        key2 = 'userid'
        val2 = '21000'
        Display(self.Illegalapi.UpdateRecord(table, key1, val1, key2, val2))

    def TestIllegalClient(self):
        self.InsertIllegal()
        self.GetUserIllegal()
        self.BorrowToIllega()
        self.UpdateRecord()


class RecommandClient(object):
    def __init__(self):
        self.recommandapi = RecommandAPI()

    def InsertRecommandRecord(self):
        test = Recommand()
        test.setbookname('哈哈p')
        test.setauthor('ni')
        test.setpublisher('ni')
        test.setversion('98')
        test.setrecomreason('good')
        try:
            self.recommandapi.InsertRecommandRecord(test, '11002')
            print('InsertRecommandRecord-OK', file=logfile)
        except:
            print('InsertRecommandRecord-Error', file=logfile)

    def GetRecommandShow(self):
        Display(self.recommandapi.GetRecommandShow('10001'))

    def GetRecommandRecord(self):
        Dict = {'userid': '11000'}
        Display(self.recommandapi.GetRecommandRecord(Dict))

    def TestRecommandClient(self):
        self.InsertRecommandRecord()
        self.GetRecommandShow()
        self.GetRecommandRecord()

class UserTypeClient(object):
    def __init__(self):
        self.usertypeapi = UserTypeAPI()

    def GetUserType(self):
        Display(self.usertypeapi.GetUserType('10010'))

    def GetUserTypeRecord(self):
        Display(self.usertypeapi.GetUserTypeRecord())

    def TestUserTypeClient(self):
        self.GetUserType()
        self.GetUserTypeRecord()

class Client(object):
    def __init__(self):
        TestUserClient = UserClient()
        TestUserClient.TestUserClient()
        TestAdminClient = AdminClient()
        TestAdminClient.TestAdminClient()
        TestBookClient = BookClient()
        TestBookClient.TestBookClient()
        TestBorrowClient = BorrowClient()
        TestBorrowClient.TestBorrowClient()
        TestIllegalClient = IllegalClient()
        TestIllegalClient.TestIllegalClient()
        TestRecommandClient = RecommandClient()
        TestRecommandClient.TestRecommandClient()
        TestUserTypeClient = UserTypeClient()
        TestUserTypeClient.TestUserTypeClient()

if __name__ == '__main__':
    Client()
