import threading
from time import ctime,sleep
import time

def music(func):
    for i in range(2):
        print ("Begin listening to %s. %s" %(func,ctime()))
        sleep(4)
        print("end listening %s"%ctime())

def move(func):
    for i in range(2):
        print ("Begin watching at the %s! %s" %(func,ctime()))
        sleep(5)
        print('end watching %s'%ctime())

threads = []
t1 = threading.Thread(target=music,args=('七里香',))
threads.append(t1)
t2 = threading.Thread(target=move,args=('阿甘正传',))
threads.append(t2)

if __name__ == '__main__':

    for t in threads:
        # t.setDaemon(True)
        t.start()
        # t.join()
    # t1.join()
    t2.join()########考虑这三种join位置下的结果？

    print ("all over %s" %ctime())



#
# def addNum():
#     global num #在每个线程中都获取这个全局变量
#     # num-=1
#
#     temp=num
#     print('--get num:',num )
#     time.sleep(0.1)
#     num =temp-1 #对此公共变量进行-1操作
#
#
# num = 100  #设定一个共享变量
# thread_list = []
# for i in range(100):
#     t = threading.Thread(target=addNum)
#     t.start()
#     thread_list.append(t)
#
# for t in thread_list: #等待所有线程执行完毕
#     t.join()
#
# print('final num:', num )

def addNum():
    global num #在每个线程中都获取这个全局变量
    # num-=1
    lock.acquire()
    temp=num
    print('--get num:',num )
    #time.sleep(0.1)
    num =temp-1 #对此公共变量进行-1操作
    lock.release()

num = 100  #设定一个共享变量
thread_list = []
lock=threading.Lock()

for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)

for t in thread_list: #等待所有线程执行完毕
    t.join()

print('final num:', num )


class myThread(threading.Thread):
    def doA(self):
        lockA.acquire()
        print(self.name,"gotlockA",time.ctime())
        time.sleep(3)
        lockB.acquire()
        print(self.name,"gotlockB",time.ctime())
        lockB.release()
        lockA.release()

    def doB(self):
        lockB.acquire()
        print(self.name,"gotlockB",time.ctime())
        time.sleep(2)
        lockA.acquire()
        print(self.name,"gotlockA",time.ctime())
        lockA.release()
        lockB.release()
    def run(self):
        self.doA()
        self.doB()
if __name__=="__main__":

    lockA=threading.Lock()
    lockB=threading.Lock()
    threads=[]
    for i in range(5):
        threads.append(myThread())
    for t in threads:
        t.start()
    for t in threads:
        t.join()#等待线程结束，后面再讲。




