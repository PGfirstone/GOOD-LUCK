import numpy as np
import matplotlib.pyplot as plt  
class Edge():
    def __init__(self,vertex_index,endpoint_index,weight=0):
        self.vertex_index=vertex_index  #初始化 源节点
        self.endpoint_index=endpoint_index    #目标节点
        self.weight=weight                    #权重
    def __lt__(self, other):  # 小于
        return self.weight < other.weight
    def __eq__(self, other):  # 等于
        return self.weight == other.weight
    def __str__(self):
        return f"[{self.vertex_index}]---{self.weight}---[{self.endpoint_index}]"
class Graph():
    def __init__(self):
        self.edge_index=[[],[],[]]    #Coo格式存储 邻接矩阵
        self.nodeList=[]              #顶点矩阵
    def addNode(self,node_obj):
        self.nodeList.append(node_obj)
    def setEdgeIndex(self,edge_index_coo):  #直接给COO格式  邻接矩阵
        self.edge_index = edge_index_coo
    def addEdge(self,vertex_index,endpoint_index,weight=0):    #单条边的添加
        self.edge_index[0].append(vertex_index)
        self.edge_index[1].append(endpoint_index)
        self.edge_index[2].append(weight)
    def toDense(self):      #转换成邻接矩阵
        node_number=len(self.nodeList)
        dense=np.zeros((node_number,node_number),dtype=int)
        for i in range(len(self.edge_index[0])):
            dense[self.edge_index[0][i]][self.edge_index[1][i]]=self.edge_index[2][i]
        return dense
    def toUndirectedGraph(self):
        self.edge_index[0].extend(self.edge_index[1])
        self.edge_index[1].extend(self.edge_index[0][:len(self.edge_index[1])])
        self.edge_index[2].extend(self.edge_index[2])

    def MST_Kruskal(self):...
    def ShortestPath(self,starNode_I):...


def test():
    G=Graph()
    for j in range(9):
        G.addNode(str(j))

    edge_index_cool=[[0,1, 1,2,2,3, 3, 4,5,6,7,7,8,2],
                    [1,2, 7,3,8,4, 5, 5,6,7,8,0,6,5],
                     [4,8,11,7,2,9,14,10,2,1,7,8,6,2]]
    G.setEdgeIndex(edge_index_cool)
    G.toUndirectedGraph()
    print(G.toDense())

if __name__ =="__main__":
    test()