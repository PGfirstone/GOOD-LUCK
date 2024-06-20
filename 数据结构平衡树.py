class AVLnode():
    def __init__(self,data):
        self.data=data
        self.height=0  #计算父节点的BF
        self.left=None
        self.right=None


class AVLtree():
    def __init__(self):
        self.root=None
    def getBF(self,fNode):
        bf_l=fNode.left.height+1 if fNode.left is not None else 0
        bf_r = fNode.right.height+1 if fNode.right is not None else 0
        return abs(bf_l-bf_r)
    def __findParent(self,fNode):
        c_node=self.root
        parent=c_node
        while True:
            if c_node.data==fNode.data or c_node.data==fNode.data:
                return parent
            parent = c_node
            if c_node.data >= fNode.data:
                c_node = c_node.left
            else:
                c_node = c_node.right
    def adjustLL(self,fNode):
        pNode=self.__findParent(fNode)
        if fNode == self.root:
            self.root=fNode.left
        else:
            pNode.left=fNode.left
        fNode.left.right=fNode
        fNode.left=None
        bf = self.getBF(fNode)  #调整bf得分
        fNode.height = bf
        if  pNode.left is None:
            bf = self.getBF(self.root)
            self.root.height = bf
        else:
            bf = self.getBF(pNode.left)
            pNode.left.height = bf
    def adjustRR(self,fNode):
        pNode=self.__findParent(fNode)
        if fNode==self.root:
            self.root=fNode.right
        else:
            pNode.right=fNode.right
        fNode.right.left=fNode
        fNode.right=None
        bf = self.getBF(fNode)  #调整bf得分
        fNode.height = bf
        if  pNode.right is None:
            bf = self.getBF(self.root)
            self.root.height = bf
        else:
            bf = self.getBF(pNode.right)
            pNode.right.height = bf
    def adjustLR(self, fNode):
        subNode = fNode.left
        subNode.left = subNode.right
        subNode.right = None
        self.adjustLL(fNode)
    def adjustRL(self, fNode):
        subNode=fNode.right
        subNode.right=subNode.left
        subNode.left=None
        self.adjustRR(fNode)
    def adjust(self,fNode,cType):
        if cType=="LL":
            self.adjustLL(fNode)
        elif cType=="RR":
            self.adjustRR(fNode)
        elif cType=="RL":
            self.adjustRL(fNode)
        elif cType=="LR":
            self.adjustLR(fNode)
    def insert(self,node_obj):
        nodeStack=[]
        adjustStr=""
        if self.root is None:
            self.root=node_obj
        else:
            c_Node=self.root
            while True:
                nodeStack.append(c_Node)
                if c_Node.data>=node_obj.data:
                    adjustStr=adjustStr+"L"
                    if c_Node.left is None:
                        c_Node.left=node_obj
                        break
                    else:
                        c_Node=c_Node.left
                else:
                    adjustStr = adjustStr + "R"
                    if c_Node.right is None:
                        c_Node.right=node_obj
                        break
                    else:
                        c_Node=c_Node.right
            #计算BF
            while True:
                if len(nodeStack)==0:
                    break
                f_node=nodeStack.pop()
                bf=self.getBF(f_node)
                f_node.height = bf
                if bf>=2:
                    self.adjust(f_node,adjustStr[-2:])
                    break
    def DLR(self,tNode):   #先序遍历（DLR）：根节点->左子树->右子树
        print(f"f[{tNode.data}]",end=", ")
        if tNode.left is not None:
            self.DLR(tNode.left)
        if tNode.right is not None:
            self.DLR(tNode.right)
def test():
    ATree=AVLtree()
    node=AVLnode(44)
    ATree.insert(node)
    ATree.insert(AVLnode(45))
    ATree.insert(AVLnode(50))
    ATree.insert(AVLnode(65))

    ATree.DLR(ATree.root)
    print()
    ATree.insert(AVLnode(73))
    ATree.DLR(ATree.root)

if __name__ == "__main__":
    test()
