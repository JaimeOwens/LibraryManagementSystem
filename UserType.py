from SQLFactories import Mysql

class UserTypeAPI(object):
# 插入删改功能仅限管理员
# 普通用户只读

    def GetUserType(self, id):
        mysql = Mysql()
        sql = "select useridentity from user where userid = '" + id + "'"
        s = mysql.getOne(sql)
        sql1 = "select * from usertype where useridentity = '" + s[0] + "'"
        result = mysql.getOne(sql1)
        print("最多可同时借阅书籍数目：%s\t最多可一次性推荐书籍数目：%s\t一本书免费借阅期限：%s" % (result[1], result[2], result[3]))
        return result

    # 用于管理员查看
    def GetUserTypeRecord(self):
        mysql = Mysql()
        sql = "select * from usertype"
        rs = mysql.getAll(sql)
        for row in rs:
            print("身份：%s\t同时可借最多图书数目：%s\t一次性最多可推荐图书数目：%s\t免费借阅期限：%s\t" % (row[0], row[1], row[2], row[3]))
        return rs

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
            print("update succes!")
        except Exception as e:
            print("update error!")
            mysql.end(None)
        mysql.dispose()

