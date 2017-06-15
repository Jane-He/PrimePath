import os
import copy
g_NodeCount = 0

def ReadGraph(file):
    Graph = []
    global g_NodeCount
    with open(file, 'r') as f:
        g_NodeCount = int(f.readline().strip("\n"))
        while True:
            line = f.readline()
            if not line:break
            line = line.strip("[]\n")
            line = line.replace(' ', '')
            tmpline = list(line.split(","))
            tmpline = [int(element) for element in tmpline]
            if tmpline[0] == -1:
                tmpline = []
            Graph.append(tmpline)
    return Graph

# def GetSimplePath(Graph):
#     SimplePath = []
#     l_SimplePath = []
#     for i in range(g_NodeCount):             #将所有节点存到列表中
#         Path = []
#         Path.append(i)
#         SimplePath.append(Path)
#         l_SimplePath.append(Path)
    
#     Path = []
#     while(len(l_SimplePath) > 0):
#         Path = l_SimplePath.pop()                  #获得一条SimplePath
#         if(len(Path) > 1 and Path[0] == Path[-1]):     #首尾相连的路径
#             continue
        
#         EdgeEndNode = Path[len(Path) - 1]       #SimplePath的尾节点       
#         EdgeStartNode = Path[0]                 #SimplePath的首节点
#         EdgeEndNode_EndNodes = Graph[EdgeEndNode]      #和SimplePath尾节点相连的节点

#         if(EdgeEndNode_EndNodes != []):
#             for EdgeEndNode_EndNode in EdgeEndNode_EndNodes:          #如果节点不在SimplePath中，或者节点和SimplePath首节点相同，增加一条SimplePath
#                 if(EdgeEndNode_EndNode not in Path or EdgeStartNode == EdgeEndNode_EndNode):
#                     tmpPath = Path + [EdgeEndNode_EndNode]                #why replace Path.append(EdgeEndNode_EndNode) is error
#                     if(tmpPath not in SimplePath):
#                         SimplePath.append(tmpPath)
#                         l_SimplePath.append(tmpPath)
#     SimplePath.sort(key = len)
#     return SimplePath

def GetPrimePath1(Graph):
    PrimePath = []
    l_SimplePath = []
    for i in range(g_NodeCount):             #将所有节点存到列表中
        Path = []
        Path.append(i)
        l_SimplePath.append(Path)
        PrimePath.append(Path)
    
    Path = []
    while(len(l_SimplePath) > 0):
        
        Path = l_SimplePath.pop()                  #获得一条SimplePath
        if(len(Path) > 1 and Path[0] == Path[-1]):     #首尾相连的路径
            continue
        
        EdgeEndNode = Path[len(Path) - 1]       #SimplePath的尾节点       
        EdgeStartNode = Path[0]                 #SimplePath的首节点
        EdgeEndNode_EndNodes = Graph[EdgeEndNode]      #和SimplePath尾节点相连的节点

        if(EdgeEndNode_EndNodes != []):
            for EdgeEndNode_EndNode in EdgeEndNode_EndNodes:          #如果节点不在SimplePath中，或者节点和SimplePath首节点相同，增加一条SimplePath
                if(EdgeEndNode_EndNode not in Path or EdgeStartNode == EdgeEndNode_EndNode):
                    tmpSimplePath = Path + [EdgeEndNode_EndNode]                #why replace Path.append(EdgeEndNode_EndNode) is error
                    
                    bFlag = False
                    # if(tmpSimplePath not in PrimePath):
                    tmpSimplePathBuf =',' + ','.join([str(i) for i in tmpSimplePath]) + ','
                    for tmpPrimePath in PrimePath:
                        tmpPrimePathBuf = ',' + ','.join([str(i) for i in tmpPrimePath]) + ','
                        if(tmpSimplePathBuf.find(tmpPrimePathBuf) != -1): #PrimePath里面有Path在新Path中
                            PrimePath.remove(tmpPrimePath)
                        elif(tmpPrimePathBuf.find(tmpSimplePathBuf) != -1):
                            bFlag = True
                    if(bFlag == False):
                        PrimePath.append(tmpSimplePath)
                    l_SimplePath.append(tmpSimplePath)
    PrimePath = sorted(PrimePath, key=lambda a: (len(a), a))
    return PrimePath

# def GetPrimePath(SimplePath):
#     l_SimplePath = SimplePath[:]
#     PrimePath = []

#     while(len(l_SimplePath) > 0):
#         bFlag = False
#         Path = l_SimplePath.pop()
#         for TmpPath in SimplePath:
#             TmpPathBuf = ','.join([str(i) for i in TmpPath])
#             PathBuf = ','.join([str(i) for i in Path])
#             if(PathBuf != TmpPathBuf and TmpPathBuf.find(PathBuf) != -1):
#                 bFlag = True
#         if(bFlag == False):
#             PrimePath.append(Path)

#     return PrimePath

def Print_PrimrPath(PrimePath, file):
    with open(file, 'w') as f:
        f.write(str(len(PrimePath)))
        f.write("\n")
        for tmpPath in PrimePath:
            tmpPathBuf ='[' + ', '.join([str(i) for i in tmpPath]) + ']'
            f.write(tmpPathBuf)
            f.write("\n")
    
if __name__== '__main__':
    ############## 获取当前文件路径 #############
    current_path = os.path.dirname(os.path.abspath("PrimePath.py"))
    testcase = 'GetPrimePathGraph.txt'

    ############## 读文件 #############
    readfile_path = os.path.join(current_path,'testingcase', testcase)
    l_Graph = ReadGraph(readfile_path)
    
    ############## 获取PrimePath #############
    PrimePath = GetPrimePath1(l_Graph)
    
    ############## PrimePath写入文件 #############
    readfile_path = os.path.join(current_path,'answer', testcase)
    Print_PrimrPath(PrimePath, readfile_path)

    ############## 控制台输出 #############
    print(len(PrimePath))
    for tmpPath in PrimePath:
        print(tmpPath)
 

    
