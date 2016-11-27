import sys
import os
os.system('python centroid.py')
os.system('hadoop jar hadoop-streaming-2.7.1.jar -file ~/hw3/centroid.txt -file ~/hw3/mapper.py -file ~/hw3/reducer.py  -mapper ~/hw3/mapper.py -reducer ~/hw3/reducer.py -input /mnist_train/mnist_train.csv -output /result1')
os.system('hadoop dfs -rmr /result1')



def distance(a,b):
    dist = 0
    for i in range(len(a)):
        dist += (a[i]-b[i]) ** 2
    return dist ** 0.5

iteration = 0
while 1:
    f1 = open("centroid.txt","r")
    f2 = open("new_centroid.txt","r")
    centroids = list()
    new_centroids = list()
    for line in f1:
        line = line.strip()
        word = list(map(float,line.split()))
        label = int(word[0])
        centroid = word[1:785]
        #print len(centroid)
        centroids.append(centroid)
    for line in f2:
        line = line.strip()
        word = list(map(float,line.split()))
        label = int(word[0])
        centroid = word[1:785]
        #print len(centroid)
        new_centroids.append(centroid)
    difference = 0
    for i in range(10):
        difference += distance(centroids[i],new_centroids[i])
    print("%s\t%s")%(iteration,difference)
    if difference > 100:
        iteration += 1
        os.system('rm centroid.txt')
        os.system('cp new_centroid.txt centroid.txt')
        os.system('rm new_centroid.txt')
        os.system('hadoop jar hadoop-streaming-2.7.1.jar -file ~/hw3/centroid.txt -file ~/hw3/mapper.py -file ~/hw3/reducer.py  -mapper ~/hw3/mapper.py -reducer ~/hw3/reducer.py -input /mnist_train/mnist_train.csv -output /result1')
        os.system('hadoop dfs -rmr /result1')

 ')
    else:
        break
os.system('hadoop dfs -copyToLocal /result1 ~/hw3')
os.system('cat result1/part* > result.txt')
print("done")
