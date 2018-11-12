import sys
import pymysql
reload(sys)
sys.setdefaultencoding('utf-8')
class DB(object):
 def __init__(self,host='127.0.0.1',port=3306,user='root',passwd='123',database=''):
  self.__host=host
  self.__port=port
  self.__user=user
  self.__passwd=passwd
  self.__database=database
  self.__open=False
  print ('__init__')

 def __connect__(self):
  if self.__open == False:
   print ('connect db...' )
   self.__conn = MySQLdb.connect(host=self.__host , port=self.__port , user=self.__user , passwd=self.__passwd,charset='utf8')
   self.__open = True
   self.autocommit(1)
 def __executeSql__(self,sql):
  self.__connect__()
  self.__executor = self.__conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
  self.__executor.execute('use '+self.__database) #切换数据库
  return self.__executor.execute(sql)

 def executeQueryForObject(self , sql):
  self.__executeSql__(sql)
  return self.__executor.fetchone()
 '''
 返回key=value 字典
 '''
 def executeQueryAll(self , sql):
  self.__executeSql__(sql)
  return self.__executor.fetchall()

 def executeUpdate(self ,sql='' , isAutoCommit=False):
  c = self.__executeSql__(sql)
  if isAutoCommit == True:
   self.commit() #提交事务
  return c
 '''
 #提交事务
 '''
 def commit(self):
   self.__conn.commit() #提交事务

 '''
 #关闭数据库，释放资源
 '''
 def closeDB(self):
  if not self.__conn is None:
   print ('close db...')
   self.__conn.commit() #提交事务
   self.__conn.close()
 def print_parameters(self):
  print (self.__user )
  print (self.__passwd)
  print (self.__host)
  print (self.__port)
'''
if __name__ == '__main__':
 db=DB(database='tb2013')
 #db.print_parameters()
 #db.executeSql('select * from tb_user')
 print db.executeQueryForObject('select count(*) as count from tb_user')
 _rows = db.executeQueryAll('select userid,nick from tb_user limit 10');
 print _rows
 for row in _rows:
  print row
  print 'nick:%s' % str(row['nick'])
 print db.executeUpdate(sql='update tb_user set nick=\'test\' where userid=95084397',isAutoCommit=True)
 db.closeDB()
'''

# def connection(self):
#     print ("start to connect mysql", extra=self.kwargs)
#     cnx = _ConnectionProxy(inst=mysql.connector.connect(**self.kwargs))
#     cnx.
"""
