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
import sys

logfile = open("UnitTestLog", "w")


def DisplayAttributes(temp):
    print('\n'.join(['%s:%s' % item for item in temp.__dict__.items()]))


def DisplayResultSingle(funcname, result):
    print(funcname)
    try:
        DisplayAttributes(result)
    except:
        pass

def DisplayResultSet(funcname, result, args=None, limit=None):
    print(funcname)
    if args != None:
        print(args)
    try:
        # result = result[0]
        if limit != None:
            if isinstance(result, list):
                for item in result[0:limit]:
                    print(item)
            else:
                for item in result[0:limit]:
                    DisplayAttributes(item)
        else:
            if isinstance(result, list):
                for item in result:
                    print(item)
            else:
                for item in result:
                    DisplayAttributes(item)
    except Exception as e:
        pass


def DisplayResultBool(funcname, result, args=None):
    print(funcname)
    if args != None:
        print(args)
    if result == True:
        print("This object is existes")
    else:
        print("This object isn't existes")
    print()


class UserClient(object):
    def __init__(self):
        self.userapi = UserAPI()

    def MatchIsUser(self):
        funcname = sys._getframe().f_back.f_code.co_name
        args = ['10973', '941075']
        DisplayResultBool(funcname, self.userapi.matchIsUser(args[0], args[1]), args)

    def GetUserShow(self):
        funcname = sys._getframe().f_back.f_code.co_name
        args = ['10002']
        DisplayResultSingle(funcname, self.userapi.GetUserShow(args[0]))

    def InsertUserRecord(self):
        funcname = sys._getframe().f_back.f_code.co_name
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
        args = user
        DisplayResultBool(funcname, self.userapi.InsertUserRecord(user))
        DisplayAttributes(user)

    def GetUserRecord(self):
        funcname = sys._getframe().f_back.f_code.co_name
        Dict1 = {'faculty': '信息学院', 'status': '在借'}
        Dict2 = {'gender': 'female', 'useridentity': '教师'}
        Dict3 = {'faculty': '工学院', 'age': '20', 'status': '正常'}
        DisplayResultSet(funcname, self.userapi.GetUserRecord(Dict1), Dict1)
        DisplayResultSet(funcname, self.userapi.GetUserRecord(Dict2), Dict2)
        DisplayResultSet(funcname, self.userapi.GetUserRecord(Dict3), Dict3)

    def DeleteRecord(self):
        funcname = sys._getframe().f_back.f_code.co_name
        table = 'user'
        key = 'userid'
        val = '10088'
        args = [table, key, val]
        DisplayResultBool(funcname, self.userapi.DeleteRecord(args[0], args[1], args[2]), args)

    def TestUserClient(self):
        self.MatchIsUser()
        self.GetUserShow()
        self.InsertUserRecord()
        self.GetUserRecord()
        self.DeleteRecord()


class AdminClient(object):
    def __init__(self):
        self.adminapi = AdminAPI()

    def matchIsAdmin(self):
        funcname = sys._getframe().f_back.f_code.co_name
        args = ['256491', '439628']
        DisplayResultSet(funcname, self.adminapi.matchIsAdmin(args[0], args[1]), args)

    def GetAdminPermission(self):
        funcname = sys._getframe().f_back.f_code.co_name
        args = ['168452']
        DisplayResultSet(funcname, self.adminapi.GetAdminPermission(args[0]), args)

    def GetAdminRecord(self):
        funcname = sys._getframe().f_back.f_code.co_name
        DisplayResultSet(funcname, self.adminapi.GetAllAdminRecord())

    def TestAdminClient(self):
        self.matchIsAdmin()
        self.GetAdminPermission()
        self.GetAdminRecord()


class BookClient(object):
    def __init__(self):
        self.bookapi = BookAPI()

    def GetAllBookRecord(self):
        funcname = sys._getframe().f_back.f_code.co_name
        args = [5]
        DisplayResultSet(funcname, self.bookapi.GetAllBookRecord(args[0]), args)

    def GetBookByDis(self):
        funcname = sys._getframe().f_back.f_code.co_name
        args = [u'数学', u'矿业技术']
        for item in args:
            DisplayResultSet(funcname, self.bookapi.GetBookByDis(item), item, 2)

    def GetBookByMaj(self):
        funcname = sys._getframe().f_back.f_code.co_name
        args = [u'工业技术', u'数理科学与化学']
        for item in args:
            DisplayResultSet(funcname, self.bookapi.GetBookByMaj(item), item, 2)

    def GetBookByName(self):
        funcname = sys._getframe().f_back.f_code.co_name
        args = [u'Java', u'Python', u'C++']
        for item in args:
            DisplayResultSet(funcname, self.bookapi.GetBookByName(item), item, 2)

    def GetBookByField(self):
        funcname = sys._getframe().f_back.f_code.co_name
        book1 = Book()
        funcname = sys._getframe().f_back.f_code.co_name
        book1.set_author(u'韩国')
        book2 = Book()
        book2.set_version(u'第一版')
        book2.set_booklanguage(u'英文')
        book3 = Book()
        book3.set_publisher(u'清华大学出版社')
        book3.set_stack(u'一层')
        book3.set_floor(3)
        args = [book1, book2, book3]
        for item in args:
            DisplayResultSet(funcname, self.bookapi.GetBookByField(item), item, 2)

    def InsertBookRecord(self):
        funcname = sys._getframe().f_back.f_code.co_name
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
        args = [test]
        DisplayResultSet(funcname, self.bookapi.InsertBookRecord(args[0]), args[0], )

    def UpdateRecord(self):
        funcname = sys._getframe().f_back.f_code.co_name
        args = ['book', 'bookid', '300000', 'bookid', '300001']
        DisplayResultSet(funcname, self.bookapi.UpdateRecord(args[0], args[1], args[2], args[3], args[4]), args)

    def DeleteRecord(self):
        funcname = sys._getframe().f_back.f_code.co_name
        args = ['book', 'bookid', '300000']
        DisplayResultSet(funcname, self.bookapi.DeleteRecord(args[0], args[1], args[2]), args)

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
        funcname = sys._getframe().f_back.f_code.co_name
        DisplayResultSet(funcname, self.borrowapi.GetBorrowRecord(10))

    def GetBorrowRecordByField(self):
        funcname = sys._getframe().f_back.f_code.co_name
        borrow1 = Borrow()
        borrow1.set_borrowdate('2011-06-14')
        borrow2 = Borrow()
        borrow2.set_presretdate('2011-09-07')
        borrow3 = Borrow()
        borrow3.set_bookid('100048')
        args = [borrow1, borrow2, borrow3]
        for item in args:
            DisplayResultSet(funcname, self.borrowapi.GetBorrowRecordByField(item), item)

    def InsertBorrowRecord(self):
        funcname = sys._getframe().f_back.f_code.co_name
        test = Borrow()
        test.set_borrowid('50000')
        test.set_userid('10000')
        test.set_bookid('100000')
        test.set_borrowdate('2017-03-06')
        test.set_presretdate('2017-03-20')
        test.set_actretdate('2017-05-09')
        DisplayResultBool(funcname, self.borrowapi.InsertBorrowRecord(test), test)

    def BorrowBook(self):
        funcname = sys._getframe().f_back.f_code.co_name
        uid = '10000'
        bid = '100001'
        args = [uid, bid]
        DisplayResultBool(funcname, self.borrowapi.BorrowBook(args[0], args[1]), args)

    def ReturnOvertimeRecord(self):
        funcname = sys._getframe().f_back.f_code.co_name
        DisplayResultSet(funcname, self.borrowapi.RetureIllegalRecord())

    def UpdateBorrowRecord(self):
        funcname = sys._getframe().f_back.f_code.co_name
        table = "borrow"
        key1 = "borrowid"
        val1 = "10001"
        key2 = "status"
        val2 = "测试"
        args = [table, key1, val1, key2, val2]
        DisplayResultSet(funcname, self.borrowapi.UpdateRecord(args[0], args[1], args[2], args[3], args[4]), args)


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
        funcname = sys._getframe().f_back.f_code.co_name
        mid = Illegal()
        mid.set_illegalid('30000')
        mid.set_userid('100005')
        mid.set_bookid('10003')
        mid.set_amount('10')
        mid.set_isprocessed('否')
        mid.set_illegaldate('2000-05-02')
        mid.set_illegaltype('损坏')
        DisplayResultBool(funcname, self.Illegalapi.InsertIllegal(mid), mid)

    def GetUserIllegal(self):
        funcname = sys._getframe().f_back.f_code.co_name
        ile = Illegal()
        ile.set_illegalid('10010')
        DisplayResultSingle(funcname, self.Illegalapi.GetUserIllegal(ile))

    def BorrowToIllega(self):
        funcname = sys._getframe().f_back.f_code.co_name
        DisplayResultBool(funcname, self.Illegalapi.BorrowToIllega())

    def UpdateRecord(self):
        funcname = sys._getframe().f_back.f_code.co_name
        table = 'illegal'
        key1 = 'illegalid'
        val1 = '13000'
        key2 = 'userid'
        val2 = '21000'
        args = [table, key1, val1, key2, val2]
        DisplayResultBool(funcname, self.Illegalapi.UpdateRecord(table, key1, val1, key2, val2), args)

    def TestIllegalClient(self):
        self.InsertIllegal()
        self.GetUserIllegal()
        self.BorrowToIllega()
        self.UpdateRecord()


class RecommandClient(object):
    def __init__(self):
        self.recommandapi = RecommandAPI()

    def InsertRecommandRecord(self):
        funcname = sys._getframe().f_back.f_code.co_name
        test = Recommand()
        test.setbookname('革命导论全新版本')
        test.setauthor('切格瓦拉')
        test.setpublisher('人民邮电出版社')
        test.setversion('第一版')
        test.setrecomreason('指明社会进步的方向')
        DisplayResultBool(funcname, self.recommandapi.InsertRecommandRecord(test, '10099'), test)

    def GetRecommandShow(self):
        funcname = sys._getframe().f_back.f_code.co_name
        DisplayResultSet(funcname, self.recommandapi.GetRecommandShow('10001'))

    def GetRecommandRecord(self):
        funcname = sys._getframe().f_back.f_code.co_name
        Dict = {'userid': '10088'}
        DisplayResultSet(funcname, self.recommandapi.GetRecommandRecord(Dict), Dict)

    def TestRecommandClient(self):
        self.InsertRecommandRecord()
        self.GetRecommandShow()
        self.GetRecommandRecord()


class UserTypeClient(object):
    def __init__(self):
        self.usertypeapi = UserTypeAPI()

    def GetUserType(self):
        funcname = sys._getframe().f_back.f_code.co_name
        DisplayResultSet(funcname, self.usertypeapi.GetUserType('10010'))


    def GetUserTypeRecord(self):
        funcname = sys._getframe().f_back.f_code.co_name
        DisplayResultSet(funcname, self.usertypeapi.GetUserTypeRecord())

    def TestUserTypeClient(self):
        self.GetUserType()
        self.GetUserTypeRecord()


class Client(object):
    def __init__(self):
        # TestUserClient = UserClient()
        # TestUserClient.TestUserClient()
        # TestAdminClient = AdminClient()
        # TestAdminClient.TestAdminClient()
        # TestBookClient = BookClient()
        # TestBookClient.TestBookClient()
        # TestBorrowClient = BorrowClient()
        # TestBorrowClient.TestBorrowClient()
        # TestIllegalClient = IllegalClient()
        # TestIllegalClient.TestIllegalClient()
        # TestRecommandClient = RecommandClient()
        # TestRecommandClient.TestRecommandClient()
        TestUserTypeClient = UserTypeClient()
        TestUserTypeClient.TestUserTypeClient()


if __name__ == '__main__':
    Client()
