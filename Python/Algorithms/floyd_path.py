import numpy as np

graph = np.array([[0,10,20,30,0,0],[0,0,0,0,0,7],[0,0,0,0,0,5],[0,0,0,0,10,0],[2,0,0,0,0,4],[0,5,7,0,6,0]])
print(graph)
print("\n")

v = len(graph)

# path reconstruction matrix
p = np.zeros(graph.shape)
for i in range(0,v):
    for j in range(0,v):
        p[i,j] = i
        if (i != j and graph[i,j] == 0): 
            p[i,j] = -30000 
            graph[i,j] = 30000 # set zeros to any large number which is bigger then the longest way

for k in range(0,v):
    for i in range(0,v):
        for j in range(0,v):
            if graph[i,j] > graph[i,k] + graph[k,j]:
                graph[i,j] = graph[i,k] + graph[k,j]
                p[i,j] = p[k,j]

# show p matrix
print(p)

def ConstructPath(p, i, j):
    i,j = int(i), int(j)
    if(i==j):
      print (i,)
    elif(p[i,j] == -30000):
      print (i,'-',j)
    else:
      ConstructPath(p, i, p[i,j]);
      print(j,)

# reconstruct the path from 0 to 4
ConstructPath(p, 0, 4)
