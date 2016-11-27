import os
import sys
#from collections import Counter
import operator
f1 = open("true_label.txt","r")
f2 = open("result.txt","r")
true_label = list()
cluster = dict()
for line in f1:
    line = line.strip()
    index, label = list(map(int,line.split("\t")))
    true_label.append(label)

for line in f2:
    line = line.strip()
    index, cluster_id = list(map(int,line.split("\t")))
    if cluster_id in cluster:
        cluster[cluster_id].append(index)
    else:
        cluster[cluster_id]=[index]

major_label = list()
for i in range(10):
    major_label.append(None)
    frequency = dict()
    for j in cluster[i]:
        if true_label[j] in frequency:
            frequency[true_label[j]]+=1
        else:
            frequency[true_label[j]]=1
    major_label[i]=max(frequency.iteritems(),key=operator.itemgetter(1))[0]
    #print ("major label of cluster%d is %s")%(i,major_label[i])

total_correct_count = 0
for i in range(10):
    cluster_id = i
    cluster_size = len(cluster[i])
    label = major_label[i]
    correct_count = 0
    for j in cluster[i]:
        if label == true_label[j]:
            correct_count+=1
    total_correct_count += correct_count
    accuracy = float(correct_count)/float(cluster_size)
    print ("cluster%d:\nsize:%s\tmajor label:%s\tcorrect count:%s\taccuracy:%s\t")%(i,cluster_size,label,correct_count,accuracy)
total_accuracy = float(total_correct_count)/10000
print ("total accuracy is %s")%total_accuracy
