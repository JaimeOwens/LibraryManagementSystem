from DBPool import Mysql

class Recommand(object):

    # 插入一条推荐记录，插入成功返回1
    def InsertRecommandRecord(self, List):
        mysql = Mysql()
        sql = "insert into recommand(userid,bookname,author,publisher,version,recomreason,statue)" \
              + "values(%s, %s, %s, %s, %s, %s, '待定')"
        try:
            mysql.insertMany(sql, List)
            mysql.end('commit')
            print("insert success!")
            return 1
        except Exception as e:
            print("insert failed!")
            mysql.end(None)
        mysql.dispose()

    # 按字段查询用户记录，输入为元组，输出包括user表所有字段.该方法主要用于管理员查询
    def GetRecommandRecord(self, Dict):
        mysql = Mysql()
        sql = "select * from recommand where "
        keys = tuple(Dict.keys())
        vals = tuple(Dict.values())
        Len = len(Dict)
        for i in range(Len):
            if (i != Len - 1):
                sql = sql + keys[i] + "='" + str(vals[i]) + "' and "
            else:
                sql = sql + keys[i] + "='" + str(vals[i]) + "'"
        try:
            User = mysql.getAll(sql)
            if len(User) == 0:
                print("No recommand found!")
            else:
                print("The recommand you found:")
                if User:
                    for row in User:
                        print("%s\t%s\t%s\t%s\t%s\t%s\t%s" % (
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        except Exception as e:
            print("query error!")
        mysql.dispose()


#test = Recommand()
#list = [('11000', '高数p', '无名', '北京林业大学出版社', '最牛版', '太好看')]
#test.InsertRecommandRecord(list)
#test.GetRecommandRecord({'userid': '11000'})