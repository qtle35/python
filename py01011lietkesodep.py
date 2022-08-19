from asyncio import Queue
import queue


t=int(input())
while t>0:
    n=int(input())
    q=queue.Queue()
    q.put("2")
    q.put("4")
    q.put("6")
    q.put("8")
    while True:
        tmp=q.get()
        m=tmp+tmp[::-1]
        if int(m)>=n: break
        print(m,end=" ")
        q.put(tmp+"0")
        q.put(tmp+"2")
        q.put(tmp+"4")
        q.put(tmp+"6")
        q.put(tmp+"8")
        m=""
    print()
    t-=1
