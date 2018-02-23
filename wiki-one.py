import snap

graphfilename = "C:\Python27\HW1\wiki-vote.txt"
schema = snap.Schema()
context = snap.TTableContext()
schema.Add(snap.TStrTAttrPr("srcID", snap.atStr))
schema.Add(snap.TStrTAttrPr("dstID", snap.atStr))
sample_table = snap.TTable.LoadSS(schema, graphfilename, context, "\t", snap.TBool(False))

# graph will be an object of type snap.PNGraph
graph = snap.ToGraph(snap.PNGraph, sample_table, "srcID", "dstID", snap.aaFirst)
#no of nodes
Count = snap.CntNonZNodes(graph)
print "Count of nodes with degree greater than 0 is %d" % Count
#no of edges
Count = snap.CntOutDegNodes(graph, 0)
print "Count of nodes with out-degree 0 is %d" % Count
#no of nodes with zero in-degree
Count = snap.CntInDegNodes(graph, 0)
print "Count of nodes with in-degree 0 is %d" % Count
#no of directed edges
Count = snap.CntUniqDirEdges(graph)
print "Count of directed edges is %d" % Count
#no of undirected edges
Count = snap.CntUniqUndirEdges(graph)
print "Count of undirected edges is %d" % Count
#no of self edges
Count = snap.CntSelfEdges(graph)
print "Count of self edges is %d" % Count
#no of unique bi-directional/reciprocated edges
Count = snap.CntUniqBiDirEdges(graph)
print "Count of unique bidirectional edges is %d" % Count

#no of nodes with out-degree greater than 10
OutDegV = snap.TIntPrV()
snap.GetNodeOutDegV(graph, OutDegV)
count_od = 0
for item in OutDegV:
    if (item.GetVal2()>10):
        count_od =count_od+1
print "Count of nodes with more than 10 outgoing edges %d" % count_od

#no of nodes with in-degree greater than 10
InDegV = snap.TIntPrV()
snap.GetNodeInDegV(graph, InDegV)
count_in = 0
for item in InDegV:
    if (item.GetVal2()< 10):
        count_in =count_in+1
print "Count of nodes with fewer than 10 incoming edges %d" % count_in

