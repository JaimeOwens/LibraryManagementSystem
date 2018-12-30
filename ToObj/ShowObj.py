from MiddleBook import  MiddleBook
from MiddleBorrow import MiddleBorrow
from Middleillegal import Middleillegal

class ShowObj:
    #book转换成obj
    def ShowBook(self,Tum):
        List = []
        for record in Tum:
            #每条记录处理
            books = MiddleBook()
            books.set_bookid(record[0])
            books.set_bookname(record[1])
            books.set_author(record[2])
            books.set_pages(record[3])
            books.set_collecttime(record[4])
            books.set_version(record[5])
            books.set_major(record[6])
            books.set_discipline(record[7])
            books.set_isbn(record[8])
            books.set_booklanguage(record[9])
            books.set_publisher(record[10])
            books.set_status(record[11])
            books.set_abstract(record[12])
            books.set_stack(record[13])
            books.set_shelf(record[14])
            books.set_floor(record[15])
            books.set_bookvalue(record[16])
            List.append(books)
        result = tuple(List)
        return result
    #借阅转换成obj
    def ShowBorrow(self,Tum):
        List = []
        for record in Tum:
            #每条记录处理
            borrowed = MiddleBorrow()
            borrowed.set_borrowid(record[0])
            borrowed.set_userid(record[1])
            borrowed.set_bookid(record[2])
            borrowed.set_borrowdate(record[3])
            borrowed.set_presretdate(record[4])
            borrowed.set_actretdate(record[5])
            List.append(borrowed)
        result = tuple(List)
        return result
    #违章转换成obj
    def ShowIlleal(self,Tum):
        List = []
        for record in Tum:
            #每条记录处理
            illegal = Middleillegal()
            illegal.set_illegalid(record[0])
            illegal.set_userid(record[1])
            illegal.set_bookid(record[2])
            illegal.set_amount(record[3])
            illegal.set_isprocessed(record[4])
            illegal.set_illegaldate(record[5])
            illegal.set_illegaltype(record[6])
            List.append(illegal)
        result = tuple(List)
        return  result

