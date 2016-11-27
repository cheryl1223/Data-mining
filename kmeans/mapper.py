import sys, math, random

centroid_file = open("centroid.txt","r")
centroids = list()

for line in centroid_file:
    line = line.strip()
    word = list(map(float,line.split()))
    cluster_id = int(word[0])
    centroid = word[1:785]
    centroids.append((cluster_id,centroid))

def distance(a,b):
    dist = 0
    for i in range(len(a)):
        dist += (a[i]-b[i]) ** 2
    return dist ** 0.5
def nearest_centroid(a):
    nearest_cluster_id = None
    nearest_distance = float("inf")
    for centroid in centroids:
        dist = distance(centroid[1],a)
        if dist < nearest_distance:
            nearest_cluster_id = centroid[0]
            nearest_distance = dist
    return nearest_cluster_id

index = 0
for line in sys.stdin:
    line = line.strip("")
    word  = list(map(int,line.split(",")))
    nearest_cluster_id = nearest_centroid(word[1:])
    print("%s\t%s\t%s")%(nearest_cluster_id,index,word[1:])
    index+=1
