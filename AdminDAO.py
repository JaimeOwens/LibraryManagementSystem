# -*- coding: UTF-8 -*-
from ObjectsClasses import *
from DBPool import Mysql

class AdminDAO:
    def matchIsAdmin(self, adminid, passwd):
        '''
        :param adminid:
        :param passwd:
        根据id、passwd字段查询admin表，匹配管理员成功返回adminid
        '''
        mysql = Mysql()
        sql = "select * from admin where adminid = '" + adminid + "' and passwd = '" + passwd + "'"
        if (mysql.getOne(sql) != False):
            print("login success!")
            adminpermission = self.getAdminPermission(mysql, adminid)
            return adminid, adminpermission

    def GetAdminPermission(self, mysql, adminid):
        sql = "select permission from admin where adminid ='" + adminid + "'"
        adminpermission = mysql.getOne(sql)
        return adminpermission

    def GetAdminRecord(self, Dict):
        '''
        :param Dict:
        按字段查询管理员记录，输入为元组，输出包括admin表所有字段
        '''
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
