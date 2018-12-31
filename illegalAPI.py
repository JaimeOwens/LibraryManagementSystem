from SQLFactories import Mysql
from BookAPI import BookAPI
from BorrowAPI import BorrowAPI
from UserAPI import UserAPI
from illegal import Illegal
from MiddleLayer import MiddleLayer
import random
import datetime


class IllegalAPI(object):
    # get max illegalid
    def GetMaxIllegalid(self):
        mysql = Mysql()
        sql = "select max(illegalid) from illegal"
        result = mysql.getAll(sql)
        mysql.dispose()
        result = result[0]
        result = result[0]
        return result

    # 供管理员调用
    # 插入违章表,接口为参数列表
    def InsertIllegal(self, obj):
        # obj->list
        List = [obj.get_illegalid(), obj.get_userid(), obj.get_bookid(), obj.get_amount(), obj.get_isprocessed(),
                obj.get_illegaldate(), obj.get_illegaltype()]
        Tum = tuple(List)
        List = []
        List.append(Tum)
        print(List)
        mysql = Mysql()
        sql = "insert into Illegal(illegalid,userid,bookid,amount,isprocessed,illegaldate,illegaltype) " + \
              "values(%s,%s,%s,%s,%s,%s,%s)"
        # val
        try:
            mysql.insertMany(sql, List)
            mysql.end('commit')
            print("insert success！")
        except Exception as e:
            mysql.end(None)
        mysql.dispose()

    # 查看某一个用户的违章记录
    def GetUserIllegal(self, obj):
        # 拼接
        Seq = []
        Val = []
        if obj.get_illegalid() != '':
            Seq.append('illegalid')
            Val.append(obj.get_illegalid())
        if obj.get_userid() != '':
            Seq.append('userid')
            Val.append(obj.get_userid())
        if obj.get_bookid() != '':
            Seq.append('bookid')
            Val.append(obj.get_bookid())
        if obj.get_amount() != '':
            Seq.append('amount')
            Val.append(obj.get_amount())
        if obj.get_isprocessed() != '':
            Seq.append('isprocessed')
            Val.append(obj.get_isprocessed())
        if obj.get_illegaldate() != '':
            Seq.append('illegaldate')
            Val.append(obj.get_illegaldate())
        if obj.get_illegaltype() != '':
            Seq.append('illegaltype')
            Val.append(obj.get_illegaltype())
        Ile = dict(zip(Seq, Val))
        mysql = Mysql()
        sql = "select * from illegal where "
        keys = tuple(Ile.keys())
        vals = tuple(Ile.values())
        Len = len(Ile)
        for i in range(Len):
            if (i != Len - 1):
                sql = sql + keys[i] + "='" + str(vals[i]) + "' and "
            else:
                sql = sql + keys[i] + "='" + str(vals[i]) + "'"
        Ilegal = mysql.getAll(sql)
        if Ilegal == False:
            print("No Illegal record!")
            return 0
            # else:
            #     print("Illegal records:")
            #     if Ilegal:
            #         for row in Ilegal:
            # print("%s\t%s\t%s\t%s\t%s\t%s\t%s" % (row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
        mysql.dispose()
        show = MiddleLayer()
        tums = show.ShowIllegal(Ilegal)
        return tums

    # num = 0查看所有记录，否则查看num条记录
    def GetAllIlegal(self, num):
        mysql = Mysql()
        if (str(num) == '0'):
            sqlAll = "select * from Illegal"
        else:
            sqlAll = "select * from Illegal limit " + str(num)
        result = mysql.getAll(sqlAll)
        # if result :
        #     for row in result :
        # print("%s\t%s\t%s\t%s\t%s\t%s\t%s" %(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
        mysql.dispose()
        show = MiddleLayer()
        tums = show.ShowIllegal(result)
        return tums

    # #用户登记还书超时情况
    def BorrowToIllega(self):
        borrow = BorrowAPI()
        user = UserAPI()
        ill_rec = borrow.RetureIllegalRecord()
        # ill_rec是违章记录的对象元组
        if ill_rec == 0:
            print('no Illegal record')
        else:
            for record in ill_rec:
                # 每条超时记录处理
                # 将用户的状态修改为不可借书的状态
                user.UpdateRecord('user', 'status', '超时', 'userid', record.get_userid())
                systime = datetime.datetime.now().strftime('%Y-%m-%d')
                acount = random.randint(1, 10)
                illegal = IllegalAPI()
                obj = Illegal()
                max = int(illegal.GetMaxIllegalid()) + 1
                obj.set_illegalid(max)
                obj.set_userid(record.get_userid())
                obj.set_bookid(record.get_bookid())
                obj.set_amount(acount)
                obj.set_isprocessed('否')
                # obj.set_illegaldate(systime)
                obj.set_illegaldate('1996-01-01')
                obj.set_illegaltype('超时')
                illegal.InsertIllegal(obj)

    # 改
    def UpdateRecord(self, table, key1, val1, key2, val2):  # key1和val1是修改键和值，val1和val2是条件键和值，如果是val是非数字，则需要写成'"数"'传入
        mysql = Mysql()
        sql = "update " + table + " set " + key1 + "='" + val1 + "' where " + key2 + "='" + val2 + "'"
        try:
            mysql.update(sql, None)
            # mysql.update("update book")
            mysql.end('commit')
            print("update succes!")
        except Exception as e:
            print("except")
            mysql.end(None)
        mysql.dispose()


ile = IllegalAPI()
# obj = Illegal()
# obj.set_userid('10009')
# res = ile.GetUserIllegal(obj)
# print(res)

# i是每一个记录
# res = ile.GetAllIlegal(3)
# for i in res:
#     print(i)

# ile.BorrowToIllega()

# mid = Illegal()
# mid.set_illegalid('30000')
# mid.set_userid('100005')
# mid.set_bookid('10003')
# mid.set_amount('10')
# mid.set_isprocessed('否')
# mid.set_illegaldate('2000-05-02')
# mid.set_illegaltype('损坏')
# ile.InsertIllegal(mid)
