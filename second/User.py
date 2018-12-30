from DBPool import Mysql

class UserAPI(object):

    # 插入一条用户记录，插入成功返回1
    def InsertUserRecord(self, List):
        mysql = Mysql()
        sql = "insert into user(userid,username,password,faculty,department,age,gender,useridentity,userconnection" \
            ",status) " + "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        try:
            mysql.insertMany(sql, List)
            mysql.end('commit')
            print("insert success!")
            return 1
        except Exception as e:
            print("insert failed!")
            mysql.end(None)
        mysql.dispose()

    # 按userid查询user表和usertype表，该方法主要用于用户自己显示
    def GetUserShow(self, id):
        mysql = Mysql()
        sql = "select * from user where userid = '" + id + "'"
        User = mysql.getOne(sql)
        print("%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s" % (User[0], User[1], User[3], User[4], User[5], User[6], User[7], User[8], User[9]))

    # 查询最多usertype表，该方法用于user的个人信息显示
    def GetUserType(self, id):
        mysql = Mysql()
        sql = "select useridentity from user where userid = '" + id + "'"
        s = mysql.getOne(sql)
        sql1 = "select * from usertype where useridentity = '" + s[0] + "'"
        result = mysql.getOne(sql1)
        print("最多可同时借阅书籍数目：%s\t最多可一次性推荐书籍数目：%s\t一本书免费借阅期限：%s" % (result[1], result[2], result[3]))

    # 按字段查询用户记录，输入为元组，输出包括user表所有字段.该方法主要用于管理员查询
    def GetUserRecord(self, Dict):
        mysql = Mysql()
        sql = "select * from user where "
        keys = tuple(Dict.keys())
        vals = tuple(Dict.values())
        Len = len(Dict)
        for i in range(Len):
            if (i != Len-1):
                sql = sql + keys[i] + "='" + str(vals[i]) + "' and "
            else:
                sql = sql + keys[i] + "='" + str(vals[i]) + "'"
        try:
            User = mysql.getAll(sql)
            if len(User) == 0:
                print("No user found!")
            else:
                print("The user you found:")
                if User:
                    for row in User:
                        print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
        except Exception as e:
            print("query error!")
        mysql.dispose()

    def GetUserTypeRecord(self):
        mysql = Mysql()
        sql = "select * from usertype"
        rs = mysql.getAll(sql)
        for row in rs:
            print("身份：%s\t同时可借最多图书数目：%s\t一次性最多可推荐图书数目：%s\t免费借阅期限：%s\t" % (row[0], row[1], row[2], row[3]))

    # 按字段查询管理员记录，输入为元组，输出包括admin表所有字段
    def GetAdminRecord(self, Dict):
        mysql = Mysql()
        sql = "select * from admin where "
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
                print("No user found!")
            else:
                print("The user you found:")
                if User:
                    for row in User:
                        print("%s\t%s\t%s\t%s" % (row[0], row[1], row[2], row[3]))
        except Exception as e:
            print("query error!")
        mysql.dispose()

    # 根据id、passwd字段查询user表，匹配用户成功返回userid
    def matchIsUser(self, userid, password):
        mysql=Mysql()
        sql = "select * from user where userid = '" + userid + "' and password = '" + password + "'"
        if(mysql.getOne(sql) != False):
            #print("login success!")
            return True

    # 根据id、passwd字段查询admin表，匹配管理员成功返回adminid
    def matchIsAdmin(self, adminid, passwd):
        mysql=Mysql()
        sql="select * from admin where adminid = '" + adminid + "' and passwd = '" + passwd + "'"
        if(mysql.getOne(sql) != False):
            print("login success!")
            return True

    # 输入表名、字段和条件，删除一条记录(通用)
    def DeleteRecord(self, table, key, val):  # key字段名 val值
        mysql = Mysql()
        sql = "delete from " + table + " where " + str(key) + "=" + str(val)
        try:
            mysql.delete(sql, None)
            mysql.end('commit')
            print("delete success!")
        except Exception as e:
            print("delete error!")
            mysql.end(None)
        mysql.dispose()

    # 更改数据表记录,输入条件字段和修改字段（通用）
    def UpdateRecord(self, table, key1, val1, key2, val2):
    # key1和val1是修改键和值，val1和val2是条件键和值，如果是val是非数字，则需要写成'"数"'传入
        mysql = Mysql()
        sql = "update " + table + " set " + key1 + "='" + val1 + "' where " + key2 + "='" + val2 + "'"
        print(sql)
        try:
            mysql.update(sql, None)
            # mysql.update("update book")
            mysql.end('commit')
            print("update succes!")
        except Exception as e:
            print("update error!")
            mysql.end(None)
        mysql.dispose()

test=UserAPI()
#list=[('16100', '张三', '123456', '信息学院', '计算机', '20', 'male', '本科', '13088889999', '正常')]
#test.InsertUserRecord(list)
#test.DeleteRecord('user', 'userid', '11001')
#test.UpdateRecord('user', 'username', '三水', 'userid', '10000')
#test.GetUserRecord({'faculty':'信息学院', 'status':'在借'})
#test.GetAdminRecord({'adminid': '168452', 'passwd': '218493'})
#id = test.matchIsUser('11000', '123456')
#if (int(id)>0):
#    print("success")
#    print(id)
#id = test.matchIsAdmin('168452', '218493')
#if(int(id) > 0):
#    print(id)
#test.GetUserShow('16895')
#test.GetUserType('11000')
#test.GetUserTypeRecord()