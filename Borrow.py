from DBPool import Mysql
from Book import BookAPI

class BorrowAPI(object):
    #插入借阅表记录,传入一个接口
    def InsertBorrowRecord(self,List):
        mysql = Mysql()
        sql = "insert into borrow(borrowid,userid,bookid,borrowdate,presretdate,actretdate) values(%s,%s,%s,%s,%s,%s)"
        try:
            mysql.insertMany(sql, List)
            mysql.end('commit')
            print("insert success!")
        except Exception as e:
            print("except")
            mysql.end(None)
        mysql.dispose()
    #用户借书的接口，需要传入用户id和书籍id,如果借书成功就修改借阅表
    def BorrowBook(self,UID,BID):
        book = BookAPI()
        record = book.GetBookByField({'bookid':BID})
        print(record[0][11])
        if(record[0][11] == '正常'):
            print("You can borrow this book!")
            if(input("Do you want to borrow this book?(press YES to borrow)") == 'YES'):
                print("Successful borrowing!")
                addborr = BorrowAPI()
                addborr.InsertBorrowRecord([('30000',UID,BID,'2017-03-06','2017-03-20','2017-05-09')])
            else:
                print("You don't want to borrow this book......OK")
        else:
            print("Abnormal book state,you can't borrow this book!")
bo = BorrowAPI()
# bo.InsertBorrowRecord([('30000','10001','100045','2017-03-06','2017-03-20','2017-05-09')])
# bo.BorrowBook('30000','100016')



