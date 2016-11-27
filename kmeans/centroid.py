i = open("mnist_train.csv","r")
o = open("centroid.txt", "w")
n = 10
import random
centroid_index = sorted(random.sample(range(0,59999),10))
print centroid_index
count = 0
cluster_id = 0
for line in i:
    if count in centroid_index:
        read = line.strip().split(",")
        o.write(str(cluster_id))
        o.write(" ")
        for n in range(len(read)):
            o.write(str(read[n]))
            o.write(" ")
        o.write("\n")
        cluster_id+=1
    count +=1
#i.close()
#o.close()
