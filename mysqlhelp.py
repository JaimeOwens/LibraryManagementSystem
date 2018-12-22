import pymysql as db
from test import Mysql
from _sqlite3 import Row

# #申请资源
# mysql = Mysql()
#
# sqlAll = "SELECT tb.uid as uid, group_concat(tb.goodsname) as goodsname FROM ( SELECT goods.uid AS uid, IF ( ISNULL(goodsrelation.goodsname), goods.goodsID, goodsrelation.goodsname ) AS goodsname FROM goods LEFT JOIN goodsrelation ON goods.goodsID = goodsrelation.goodsId ) tb GROUP BY tb.uid"
# result = mysql.getAll(sqlAll)
# if result :
#     print ("get all")
#     for row in result :
#         print ("%s\t%s"%(row["uid"],row["goodsname"]))
# sqlAll = "SELECT tb.uid as uid, group_concat(tb.goodsname) as goodsname FROM ( SELECT goods.uid AS uid, IF ( ISNULL(goodsrelation.goodsname), goods.goodsID, goodsrelation.goodsname ) AS goodsname FROM goods LEFT JOIN goodsrelation ON goods.goodsID = goodsrelation.goodsId ) tb GROUP BY tb.uid"
# result = mysql.getMany(sqlAll,2)
# if result :
#     print ("get many")
#     for row in result :
#         print ("%s\t%s"%(row["uid"],row["goodsname"]))
#
#
# result = mysql.getOne(sqlAll)
# print ("get one")
# print ("%s\t%s"%(result["uid"],result["goodsname"]))
#
# #释放资源
# mysql.dispose()


#申请资源
class BookAPI(object):
    #获取任何表中的所有记录
    #写完
    def GetAllBookRecord(self):
        mysql = Mysql()
        str = input("input the table name:")
        sqlAll= "SELECT * FROM " + str
        print(sqlAll)
        result = mysql.getAll(sqlAll)
        if result :
            print ("get all")
            for row in result :
                print("%s\t%s" % (row["ID"], row["Name"]))
        mysql.dispose()
    def GetOneBookRecord(self):
        mysql = Mysql()
        str = input("input the sql to delete a book record:")
        print("Received input is:%s"%str)
        sqlAll=str
        result = mysql.getOne(sqlAll)
        print("get one")
        print("图书ID：%s\tName：%s"%(result["ID"],result["Name"]))
        mysql.dispose(self)
    #按分类查找图书
    def GetBook_type(self):
        mysql = Mysql()
        str = input("input the sql to delete a book record:")
        print("Received input is:%s" % str)
        sqlAll=str
        result = mysql.getMany(sqlAll,2)
        if result :
            print("get many")
            for row in result :
                print("图书ID：%s\tName：%s"%(result["ID"],result["Name"]))
        mysql.dispose()

    #插入图书的一条记录
    #成功
    def InsertOneBookRecord(self,num):
        mysql = Mysql()
        #插入图书
        #sql
        table = input("input the sql to delete a book record:")
        sql = "insert into " + table + "(ID,Name,Author,Page)\n" + "values(%s,%s,%s,%s)"          #修改
        #val
        val = []
        for i in range(num):
            para = input("第" + str(i) + "个字段为：")
            if para.isdigit() == True:
                val.append(para)
            else:
                val.append(str(para))
        tup = list(val)
        try:
            count = mysql.insertOne(sql,val)
            mysql.end('commit')
            print("insert success！")
        except Exception as e:
            mysql.end(None)
        mysql.dispose()

    #插入图书多条记录

    #删除一条图书记录
    def DeleteOneBookRecord(self,key,val):#key字段名 val值
        mysql = Mysql()
        table = input("input the table name:")
        sql = "delete from " + table + " where " + str(key) + "=" + str(val)
        try:
            mysql.delete(sql,None)
        except Exception as e:
            print("except")
            mysql.end(None)
        mysql.dispose()

add = BookAPI()
add.DeleteOneBookRecord('ID',5)


# sqlAll = ""
# result = mysql.getAll(sqlAll)
# if result :
#     print ("get all")
#     for row in result :
#         print ("%s\t%s"%(row["uid"],row["goodsname"]))
# #释放资源
# mysql.dispose()

