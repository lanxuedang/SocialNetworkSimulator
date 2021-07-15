def SaveGraph(graph, path, MADict):
    a = open(path, "w")
    nNodes = graph.GetNodes()
    nEdges = graph.GetEdges()
    seqences = []
    seqences.append(str.format("Nodes#{0}#Edges#{1}\n", nNodes, nEdges))
    for node in graph.Nodes():
        seqences.append(str.format("{0}#{1}#{2}\n", node.GetId(), MADict[str(node.GetId())][0], MADict[str(node.GetId())][1]))
    for EI in graph.Edges():
        seqences.append(str.format("{0},{1}\n", EI.GetSrcNId(), EI.GetDstNId()))
    a.writelines(seqences)
    a.close()

import snap
import csv
def ReadData(filepath):
    data = []
    with open(filepath, "r") as fp:
        reader = csv.reader(fp, dialect=csv.excel)
        for rows in reader:
            data.append(rows)
    return data

path = "C:\\SocialNetworkSimulator\\Tweets\\Vaccine\\"

MAData = ReadData(path + "TOP30MAPoints.csv")
MADict = {}
for i in range(1, len(MAData)):
    MADict[MAData[i][8]] = [MAData[i][10], MAData[i][11]]



graph = snap.TUNGraph.New()
for i in range(30):
    graph.AddNode(i)
for i in range(30):
    for j in range(30):
        graph.AddEdge(i, j)
SaveGraph(graph, "C:\\SocialNetworkSimulator\\Tweets\\Vaccine\\CityNetwork.txt", MADict)
