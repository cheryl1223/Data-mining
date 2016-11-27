import sys, math, random

cur_cluster = list()
cur_cluster_id = None
cur_cluster_size = 0
new_centroid = list()

#f = open("result.txt","w")
for line in sys.stdin:
    cluster_id,index, data = line.split("\t")
    data =  [int(i) for i in data.strip('[]\n').split(",")]
    print ("%s\t%s")%(index,cluster_id)
    #f.write(("%s\t%s\n")%(index,cluster_id))
    if cur_cluster_id == cluster_id:
        cur_cluster.append(data)
        cur_cluster_size +=1
    else:
        if cur_cluster_size != 0:
            cur_centroid = [0 for i in range(784)]
            for i in range(784):
                cur_centroid[i] = float(sum(row[i] for row in cur_cluster))/cur_cluster_size
            new_centroid.append(cur_centroid)
        cur_cluster = list()
        cur_cluster_id = cluster_id
        cur_cluster_size = 1
        cur_cluster.append(data)
cur_centroid = [0 for i in range(784)]
for i in range(784):
    cur_centroid[i] = float(sum(row[i] for row in cur_cluster))/cur_cluster_size
new_centroid.append(cur_centroid)

o = open("new_centroid.txt", "w")
cluster_id = 0
for i in range(10):
    o.write(str(cluster_id)+" ")
    for j in range(784):
        o.write(str(new_centroid[i][j])+" ")
    o.write("\n")
    cluster_id+=1
