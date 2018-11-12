# from multiprocessing import Process, Queue
#
# def f(q,n):
#     q.put([42, n, 'hello'])
#
# if __name__ == '__main__':
#     q = Queue()
#     p_list=[]
#     for i in range(3):
#         p = Process(target=f, args=(q,i))
#         p_list.append(p)
#         p.start()
#     print(q.get())
#     print(q.get())
#     print(q.get())
#     for i in p_list:
#             i.join()

from multiprocessing import Process, Pipe

def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()

def fm(parent_conn):
    parent_conn.send([42, '回复子进程', 'hello'])
    parent_conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())  # prints "[42, None, 'hello']"
    fm(parent_conn)
    print(child_conn.recv())
    p.join()



