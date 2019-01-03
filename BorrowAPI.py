from SQLFactories import Mysql
from BookAPI import BookAPI
from MiddleLayer import MiddleLayer
from Borrow import Borrow
from Book import Book
import datetime


class BorrowAPI(object):
    # get max borrowid
    def GetMaxBorrowid(self):
        mysql = Mysql()
        sql = "select max(borrowid) from borrow"
        result = mysql.getAll(sql)
        mysql.dispose()
        result = result[0]
        result = result[0]
        return result

    # 获取num个借阅表记录，num = 0时获取所有
    def GetBorrowRecord(self, num=0):
        mysql = Mysql()
        if (str(num) == '0'):
            sqlAll = "select * from borrow"
        else:
            sqlAll = "select * from borrow limit " + str(num)
        result = mysql.getAll(sqlAll)
        print("borrowid\tuserid\tbookid\tborrowdate\tpresretdate\tactretdate")
        if result:
            for row in result:
                print("%s\t%s\t%s\t%s\t%s\t%s" % \
                      (row[0], row[1], row[2], row[3], row[4], row[5]))
        mysql.dispose()
        if result == False:
            print('no record')
            return 0
        show = MiddleLayer()
        tums = show.ShowBorrow(result)
        return tums

    # 按字段获取借阅记录
    def GetBorrowRecordByField(self, obj):
        # 拼接
        Seq = []
        Val = []
        if obj.get_borrowid() != '':
            Seq.append('borrowid')
            Val.append(obj.get_borrowid())
        if obj.get_userid() != '':
            Seq.append('userid')
            Val.append(obj.get_userid())
        if obj.get_bookid() != '':
            Seq.append('bookid')
            Val.append(obj.get_bookid())
        if obj.get_borrowdate() != '':
            Seq.append('borrowdate')
            Val.append(obj.get_borrowdate())
        if obj.get_presretdate() != '':
            Seq.append('presretdate')
            Val.append(obj.get_presretdate())
        if obj.get_actretdate() != '':
            Seq.append('actretdate')
            Val.append(obj.get_actretdate())
        Dict = dict(zip(Seq, Val))
        mysql = Mysql()
        sql = "select * from borrow where "
        keys = tuple(Dict.keys())
        vals = tuple(Dict.values())
        Len = len(Dict)
        for i in range(Len):
            if (i != Len - 1):
                sql = sql + keys[i] + "='" + str(vals[i]) + "' and "
            else:
                sql = sql + keys[i] + "='" + str(vals[i]) + "'"
        Bor = mysql.getAll(sql)
        if Bor == False:
            print('no record')
        # Book = mysql.getAll(sql)
        # if Book == False:
        #     print('no record')
        # if len(Book) == 0:
        #     print("No borrow record found!")
        # else:
        #     print("The borrow record you found:")
        #     if Book:
        #         for row in Book:
        #             print("%s\t%s\t%s\t%s\t%s\t%s" % (row[0], row[1], row[2], row[3], row[4], row[5]))
        mysql.dispose()
        show = MiddleLayer()
        tums = show.ShowBorrow(Bor)
        return tums

    # 插入借阅表记录,传入一个接口
    def InsertBorrowRecord(self, obj):
        # obj->list
        List = [obj.get_borrowid(), obj.get_userid(), obj.get_bookid(), obj.get_borrowdate(), obj.get_presretdate(),
                obj.get_actretdate()]
        Tum = tuple(List)
        List = []
        List.append(Tum)
        print(List)
        mysql = Mysql()
        sql = "insert into borrow(borrowid,userid,bookid,borrowdate,presretdate,actretdate) values(%s,%s,%s,%s,%s,%s)"
        try:
            mysql.insertMany(sql, List)
            mysql.end('commit')
            print("insert success!")
            return True
        except Exception as e:
            print("except")
            mysql.end(None)
        mysql.dispose()
        return False

    # 用户借书的接口，需要传入用户id和书籍id,如果借书成功就修改借阅表
    def BorrowBook(self, uid, bid):
        # 获取系统时间当作借阅时间并计算出应该归还的时间
        borrow_time = datetime.datetime.now().strftime('%Y-%m-%d')
        return_time = (datetime.datetime.now() + datetime.timedelta(days=90)).strftime('%Y-%m-%d')
        book = BookAPI()
        bo = Book()
        bo.set_bookid(bid)
        record = book.GetBookByField(bo)
        record = record[0]
        print(record.get_status())
        if (record.get_status() == '正常'):
            print("You can borrow this book!")
            if (input("Do you want to borrow this book?(press YES to borrow)") == 'YES'):
                print("Successful borrowing!")
                addborr = BorrowAPI()
                obj = Borrow()
                # 获取borrowid的最大值
                borrowid = int(addborr.GetMaxBorrowid()) + 1
                print(borrowid)
                obj.set_borrowid(borrowid)
                obj.set_userid(uid)
                obj.set_bookid(bid)
                obj.set_borrowdate(borrow_time)
                obj.set_presretdate('0000-00-00')
                obj.set_actretdate(return_time)
                addborr.InsertBorrowRecord(obj)
                book2 = BookAPI()
                # 修改图书状态
                book2.UpdateRecord('book', 'status', '在借', 'bookid', bid)
            else:
                print("You don't want to borrow this book......OK")
        else:
            print("Abnormal book state,you can't borrow this book!")

    # 按照当前系统时间返回借阅表中超时违章的记录
    def RetureIllegalRecord(self):
        mysql = Mysql()
        # 获取系统时间
        systime = datetime.datetime.now().strftime('%Y-%m-%d')
        # 返回超过系统时间还未还的图书借阅记录
        # sql = "select * from borrow where actretdate < '" + systime + "' and presretdate = '0000-00-00'"
        sql = "select * from borrow where actretdate < '" + "1996-01-01" + "' and presretdate = '0000-00-00'"
        result = mysql.getAll(sql)
        mysql.dispose()
        if (result == False):
            print('no record')
            return 0
        show = MiddleLayer()
        tums = show.ShowBorrow(result)
        return tums

    # 对借阅表进行修改
    # 可调用Book.py的UpdateRecord()函数
    # 改
    def UpdateRecord(self, table, key1, val1, key2, val2):  # key1和val1是修改键和值，val1和val2是条件键和值，如果是val是非数字，则需要写成'"数"'传入
        mysql = Mysql()
        sql = "update " + table + " set " + key1 + "='" + val1 + "' where " + key2 + "='" + val2 + "'"
        try:
            mysql.update(sql, None)
            # mysql.update("update book")
            mysql.end('commit')
            print("update success!")
        except Exception as e:
            print("except")
            mysql.end(None)
        mysql.dispose()


bo = BorrowAPI()
# bo.GetMaxBorrowid()

# objs = bo.GetBorrowRecord(5)
# for i in objs:
#     print(i.get_bookid())


# s = Borrow()
# s.set_userid('10000')
# res = bo.GetBorrowRecordByField(s)
# print(res)

# test = Borrow()
# test.set_borrowid('50000')
# test.set_userid('10000')
# test.set_bookid('100000')
# test.set_borrowdate('2017-03-06')
# test.set_presretdate('2017-03-20')
# test.set_actretdate('2017-05-09')
# bo.InsertBorrowRecord(test)


# bo.BorrowBook('30000','101060')
print(bo.RetureIllegalRecord())
