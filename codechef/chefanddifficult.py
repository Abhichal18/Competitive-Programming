def Left_index(points): 
    minn = 0
    for i in range(1,len(points)): 
        if points[i][0] < points[minn][0]: 
            minn = i
        elif points[i][0] == points[minn][0]: 
            if points[i][1] > points[minn][1]: 
                minn = i 
    return minn 
  
def orientation(p, q, r): 
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1]) 
  
    if val == 0: 
        return 0
    elif val > 0: 
        return 1
    else: 
        return 2
  
def convexHull(points, n,count,point):  
    if n < 3:
        print(count)
        return
    l = Left_index(points) 
    hull = [] 
    p = l 
    q = 0
    c=count
    while(True):  
        hull.append(p) 
        q = (p + 1) % n 
  
        for i in range(n):  
            if(orientation(points[p],  
                           points[i], points[q]) == 2): 
                q = i 
        p = q 
        if(p == l): 
            break
    pointslst=[]
    for each in hull: 
        q=points[each][0]
        w=points[each][1]
        pointslst.append([q,w])
    if point in pointslst:
        points=[]
    else:
        c+=1
    for item in pointslst:
        if item in points:
            points.remove(item)
    convexHull(points,len(points),c,point)

for _ in range(int(input())):
    n,q=map(int,input().split())
    lst=list()
    for i in range(n):
        x,y=map(int, input().split())
        lst.append([x,y])
    for i in range(q):
        l=lst[:]
        a,b=map(int,input().split())
        l.append([a,b])
        c=0
        point=[a,b]
        convexHull(l,len(l),c,point)