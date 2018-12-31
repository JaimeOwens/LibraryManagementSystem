from SQLFactories import Mysql
from User import User

class UserAPI(object):

    # 插入一条用户记录，插入成功返回1
    def InsertUserRecord(self, obj):
        # 将所有value加入一个list
        listforinsert = [obj.getid(), obj.getusername(), obj.getpassword(), obj.getfaculty(), obj.getdepartment(),
                         obj.getage(), obj.getgendar(), obj.getuseridentity(), obj.getuserconnection(), obj.getstatus()]
        #转化为元组
        listforinsert = (tuple(listforinsert))
        #加入list
        List = []
        List.append(listforinsert)
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

    # 按userid查询user表，该方法主要用于用户自己显示
    def GetUserShow(self, id):
        mysql = Mysql()
        sql = "select * from user where userid = '" + id + "'"
        temp = mysql.getOne(sql)
        #print("%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s" % (User[0], User[1], User[3], User[4], User[5], User[6], User[7], User[8], User[9]))
        #return User
        user = User()
        user.username = temp[1]
        user.password = temp[2]
        user.faculty = temp[3]
        user.department = temp[4]
        user.age = temp[5]
        user.gendar = temp[6]
        user.useridentity = temp[7]
        user.userconnection = temp[8]
        user.status = temp[9]
        return user


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

    # 根据id、passwd字段查询user表，匹配用户成功返回userid
    def matchIsUser(self, userid, password):
        mysql=Mysql()
        sql = "select * from user where userid = '" + userid + "' and password = '" + password + "'"
        if(mysql.getOne(sql) != False):
            #print("login success!")
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
            mysql.end('commit')
            print("update success!")
        except Exception as e:
            print("update error!")
            mysql.end(None)
        mysql.dispose()


#test insert
#user = User()
#user.setid('11002')
#user.setusername('sanshui')
#user.setpassword('123456')
#user.setfaculty('信息')
#user.setdepartment('计算机')
#user.setage('20')
#user.setgendar('female')
#user.setuseridentity('硕士')
#user.setuserconnection('8088888')
#user.setstatus('正常')
#User = UserAPI()
#User.InsertUserRecord(user)

#test update
#User.UpdateRecord('user', 'password', '456123', 'userid', user.getid())

#test delete
#User.DeleteRecord('user', 'userid', '11001')

#test query
#User = UserAPI()
#user = User.GetUserShow('11002')
#str = user.getdepartment()
#print(str)