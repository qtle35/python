
import queue


a=[]
q=queue.Queue()
q.put('1')
q.put('2')
while len(a)<1000:
    x=q.get()
    if x.count('2')>x.count('1')+x.count('0'):
        a.append(x)
    q.put(x+'0')
    q.put(x+'1')
    q.put(x+'2')

t=int(input())
while t>0:
    n=int(input())
    for i in range(n): print(a[i],end=' ')
    print()
    t-=1