from DBPool import Mysql
from MiddleBook import MiddleBook
from ShowObj import ShowObj


class BookAPI(object):
    # 获取任何表中的所有记录,返回对象的元组
    def GetAllBookRecord(self,num):
        mysql = Mysql()
        if(str(num) == '0'):
            sqlAll = "select * from book"
        else:
            sqlAll= "select * from book limit " + str(num)
        result = mysql.getAll(sqlAll)
        # print("bookid\tbookname\tauthor\tpages\tcollecttime\tversion\tmajor\tdiscipline\tisbn\tbooklanguage\tpublisher\tstatus\tabstract\tstack\tshelf\tfloor\tbookvalue")
        # if result :
        #     for row in result :
                # print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" %(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16]))
        mysql.dispose()
        if result == False:
            print('no record')
            return 0
        show = ShowObj()
        tums = show.ShowBook(result)
        return tums
    #按分类查找图书
    #按discipline字段分类
    def GetBookByDis(self,desci):
        mysql = Mysql()
        Dis_List = mysql.getAll("select * from book where discipline = '" + desci +"'")
        # print("Classification of " + desci + ":\n")
        # print("bookid\tbookname\tauthor\tpages\tcollecttime\tversion\tmajor\tdiscipline\tisbn\tbooklanguage\tpublisher\tstatus\tabstract\tstack\tshelf\tfloor\tbookvalue")
        # if Dis_List:
        #     for row in Dis_List:
        #         print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" %(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16]))
        mysql.dispose()
        if Dis_List == False:
            print('no record')
            return 0
        show = ShowObj()
        tums = show.ShowBook(Dis_List)
        return tums
    #按major字段分类
    def GetBookByMaj(self,maj):
        mysql = Mysql()
        Maj_List = mysql.getAll("select * from book where major = '" + maj +"'")
        # #Dis_List = Dis_List.decode('utf-8')
        # print(Maj_List)
        # print("Classification of " + maj + ":\n")
        # print("bookid\tbookname\tauthor\tpages\tcollecttime\tversion\tmajor\tdiscipline\tisbn\tbooklanguage\tpublisher\tstatus\tabstract\tstack\tshelf\tfloor")
        # if Maj_List:
        #     for row in Maj_List:
        #         print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" %(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16]))
        mysql.dispose()
        if Maj_List == False:
            print('no record')
            return 0
        show = ShowObj()
        tums = show.ShowBook(Maj_List)
        return tums
    #按字段查询
    #返回查询到的书籍数量
    def GetBookByField(self,obj):
        # 拼接成Dict函数
        # 例：{'bookid': '100014', 'author': '韩强军'}
        Seq = []
        Val = []
        if obj.get_bookid() != '':
            Seq.append('bookid')
            Val.append(obj.get_bookid())
        if obj.get_bookname() != '':
            Seq.append('bookname')
            Val.append(obj.get_bookname())
        if obj.get_author() != '':
            Seq.append('author')
            Val.append(obj.get_author())
        if obj.get_pages() != '':
            Seq.append('pages')
            Val.append(obj.get_pages())
        if obj.get_collecttime() != '':
            Seq.append('collecttime')
            Val.append(obj.get_collecttime())
        if obj.get_version() != '':
            Seq.append('version')
            Val.append(obj.get_version())
        if obj.get_major() != '':
            Seq.append('major')
            Val.append(obj.get_major())
        if obj.get_discipline() != '':
            Seq.append('discipline')
            Val.append(obj.get_discipline())
        if obj.get_isbn() != '':
            Seq.append('isbn')
            Val.append(obj.get_isbn())
        if obj.get_booklanguage() != '':
            Seq.append('booklanguage')
            Val.append(obj.get_booklanguage())
        if obj.get_publisher() != '':
            Seq.append('publisher')
            Val.append(obj.get_publisher())
        if obj.get_status() != '':
            Seq.append('status')
            Val.append(obj.get_status())
        if obj.get_abstract() != '':
            Seq.append('abstract')
            Val.append(obj.get_abstract())
        if obj.get_stack() != '':
            Seq.append('stack')
            Val.append(obj.set_stack())
        if obj.get_shelf() != '':
            Seq.append('shelf')
            Val.append(obj.get_shelf())
        if obj.get_floor() != '':
            Seq.append('floor')
            Val.append(obj.get_floor())
        if obj.get_bookvalue() != '':
            Seq.append('bookvalue')
            Val.append(obj.get_bookvalue())

        Dict = dict(zip(Seq,Val))

        mysql = Mysql()
        sql = "select * from book where "
        keys = tuple(Dict.keys())
        vals = tuple(Dict.values())
        Len = len(Dict)
        for i in range(Len):
            if (i != Len-1):
                sql = sql + keys[i] + "='" + str(vals[i]) + "' and "
            else:
                sql = sql + keys[i] + "='" + str(vals[i]) + "'"
        Book = mysql.getAll(sql)
        if Book == False:
            print('no record')
            return 0
        # if len(Book) == 0:
        #     print("No books found!")
        # else:
        #     print("The book you found:")
        #     if Book:
        #         for row in Book:
        #
        #             print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" %\
        #                   (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],\
        #                  row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16]))
        mysql.dispose()
        show = ShowObj()
        tums = show.ShowBook(Book)
        return tums
    #插入图书记录，列表传入
    def InsertBookRecord(self,obj):
        #obj->list
        List = [obj.get_bookid(),obj.get_bookname(),obj.get_author(),obj.get_pages(),obj.get_collecttime(),obj.get_version(),obj.get_major(),obj.get_discipline(),obj.get_isbn(),obj.get_booklanguage(),obj.get_publisher(),obj.get_status(),obj.get_abstract(),obj.get_stack(),obj.get_shelf(),obj.get_floor(),obj.get_bookvalue()]
        Tum = tuple(List)
        List = []
        List.append(Tum)
        print(List)
        mysql = Mysql()
        # 插入图书
        # sql
        sql = "insert into book(bookid,bookname,author,pages,collecttime,version,\
        major,discipline,isbn,booklanguage,publisher,status,abstract,stack,shelf,floor,bookvalue) " + \
              "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        # val
        try:
            mysql.insertMany(sql, List)
            mysql.end('commit')
            print("insert success！")
        except Exception as e:
            print('error')
            mysql.end(None)
        mysql.dispose()
    #输入表名、字段和条件，删除一条记录(通用)
    def DeleteRecord(self,table,key,val):#key字段名 val值
        mysql = Mysql()
        sql = "delete from " + table + " where " + str(key) + "=" + str(val)
        try:
            mysql.delete(sql,None)
            mysql.end('commit')
            print("delete success!")
        except Exception as e:
            print("error")
            mysql.end(None)
        mysql.dispose()
    #更改数据表记录,输入条件字段和修改字段（通用）
    def UpdateRecord(self,table,key1,val1,key2,val2):#key1和val1是修改键和值，val1和val2是条件键和值，如果是val是非数字，则需要写成'"数"'传入
        mysql = Mysql()
        sql = "update " + table + " set " + key1 + "='" + val1 + "' where " + key2 + "='" + val2 + "'"
        try:
            mysql.update(sql,None)
            # mysql.update("update book")
            mysql.end('commit')
            print("update succes!")
        except Exception as e:
            print("error")
            mysql.end(None)
        mysql.dispose()


add = BookAPI()
# # 返回对象
# print(add.GetBookByDis("气象学"))
# print(add.GetBookByMaj("工业技术"))
# print(add.GetBookByName("地下地上中级概论"))

# # 传入一个对象插入
# test = MiddleBook()
# test.set_bookid('300001')
# test.set_bookname('1')
# test.set_author('1')
# test.set_pages('1')
# test.set_collecttime('2010-09-17')
# test.set_version('1')
# test.set_major('1')
# test.set_discipline('1')
# test.set_isbn('133-314-2343-16-2')
# test.set_booklanguage('1')
# test.set_publisher('1')
# test.set_status('1')
# test.set_abstract('1')
# test.set_stack('1')
# test.set_shelf('1')
# test.set_floor('2')
# test.set_bookvalue('1')
# add.InsertBookRecord(test)

# add.DeleteRecord('book','bookid','300000')
# add.UpdateRecord('book','bookname','Unix编程','bookid','300000')@修改bookid为300000时候的bookname值为Unix编程

# 修改后，传入一个obj，返回元组
# test.set_bookid('100003')
# res = add.GetBookByField(test)
# print(res)




