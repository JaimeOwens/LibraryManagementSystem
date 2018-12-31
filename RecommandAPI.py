from SQLFactories import Mysql
from Recommand import Recommand

class RecommandAPI(object):

    # 插入一条推荐记录，插入成功返回1
    def InsertRecommandRecord(self, obj, id):
        recom = []
        recom.append(id)
        recom.append(obj.getbookname())
        recom.append(obj.getauthor())
        recom.append(obj.getpublisher())
        recom.append(obj.getversion())
        recom.append(obj.getrecomreason())
        recom.append('待定')
        reco = tuple(recom)
        List = []
        List.append(reco)
        mysql = Mysql()
        try:
            sql = "insert into recommand(userid,bookname,author,publisher,version,recomreason,statue)" + \
                  "values(%s, %s, %s, %s, %s, %s, %s)"
            sql2 = "select * from recommand where userid='" + id + "'"
            print(sql2)
            rs = mysql.getAll(sql2)
            print(rs)
            count = len(rs)
            print(count)
            sql3 = "select useridentity from user where userid = '" + id + "'"
            print(sql3)
            s = mysql.getOne(sql3)
            print(s[0])
            sql4 = "select * from usertype where useridentity = '" + s[0] + "'"
            print(sql4)
            result = mysql.getOne(sql4)
            print(result[2])
            if(count >= result[2]):
                print("can't more recommand")
            else:
                mysql.insertMany(sql, List)
                mysql.end('commit')
                print("insert success!")
                return 1
        except Exception as e:
            print("insert failed!")
            mysql.end(None)
        mysql.dispose()

    # 用于普通用户显示,返回对象的元组
    def GetRecommandShow(self, id):
        mysql = Mysql()
        sql = "select * from recommand where userid='" + id + "'"
        try:
            User = mysql.getAll(sql)
            if len(User) == 0:
                print("No recommand found!")
            else:
                #print("The recommand you found:")
                if User:
                    rs = []
                    for row in User:
                        user = Recommand()
                        user.setbookname(row[1])
                        user.setauthor(row[2])
                        user.setpublisher(row[3])
                        user.setversion(row[4])
                        user.setrecomreason(row[5])
                        user.setstatue(row[6])
                        rs.append(user)
                    rs = tuple(rs)
                    return rs
        except Exception as e:
            print("query error!")
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

# 插入推荐
#test = RecommandAPI()
#user = Recommand()
#user.setbookname('哈哈p')
#user.setauthor('ni')
#user.setpublisher('ni')
#user.setversion('98')
#user.setrecomreason('good')
#test.InsertRecommandRecord(user, '11002')

# 查询推荐
#test = RecommandAPI()
#rs = test.GetRecommandShow('11000')
#for i in rs:
#    print(i.getbookname())