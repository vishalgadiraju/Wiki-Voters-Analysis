import snap
import matplotlib
import matplotlib.pyplot as plt

graphfilename = "C:\Python27\HW1\wiki-vote.txt"
schema = snap.Schema()
context = snap.TTableContext()
schema.Add(snap.TStrTAttrPr("srcID", snap.atStr))
schema.Add(snap.TStrTAttrPr("dstID", snap.atStr))
sample_table = snap.TTable.LoadSS(schema, graphfilename, context, "\t", snap.TBool(False))

# graph will be an object of type snap.PNGraph
graph = snap.ToGraph(snap.PNGraph, sample_table, "srcID", "dstID", snap.aaFirst)

DegToCntV = snap.TIntPrV()
snap.GetOutDegCnt(graph, DegToCntV)
v1=[]
v2=[]

for item in DegToCntV:
 if item.GetVal1()==0:
     continue
 v1.append(item.GetVal1())
 v2.append(item.GetVal2())
plt.loglog(v1,v2, basex=10, basey=10)
plt.show()
