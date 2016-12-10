from mnist import MNIST
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

mndata = MNIST('./data')
train_img, train_label = mndata.load_training()
test_img, test_label = mndata.load_testing()
train_images = np.array(train_img)
train_pca = PCA(n_components=25).fit_transform(train_images)
np.savetxt('train_pca.txt', train_pca, delimiter=',',fmt='%.4f')
train_labels = np.array(train_label)
np.savetxt('train_label.txt', train_labels, delimiter=',',fmt='%d')
test_images = np.array(test_img)
test_pca = PCA(n_components=25).fit_transform(test_images)
np.savetxt('test_pca.txt', test_pca, delimiter=',', fmt='%.4f')
test_labels = np.array(test_label)
np.savetxt('test_label.txt', test_labels, delimiter=',',fmt='%d')

