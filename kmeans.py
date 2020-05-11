import numpy as np
import pandas as pd
class KMeans:
    def __init__(self,k=3,maxIterations=300):
        self.k=k
        self.maxIterations=maxIterations
        self.tol=0.001
    def calcDistance(self,a,b):
        return np.linalg.norm(a-b)
    def cluster(self,dat):
        self.centroids = {}

        for i in range(self.k):
            self.centroids[i] = dat[np.random.randint(0,np.size(dat,0))]

        for i in range(self.maxIterations):
            self.classifications = {}

            for i in range(self.k):
                self.classifications[i] = []

            for featureset in dat:
                distances = [np.linalg.norm(featureset-self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(featureset)

            prev_centroids = dict(self.centroids)

            for classification in self.classifications:
                self.centroids[classification] = np.average(self.classifications[classification],axis=0)

            optimized = True

            for c in self.centroids:
                original_centroid = prev_centroids[c]
                current_centroid = self.centroids[c]
                if np.sum((current_centroid-original_centroid)/original_centroid*100.0) > self.tol:
                    #print(np.sum((current_centroid-original_centroid)/original_centroid*100.0))
                    optimized = False

            if optimized:
                break
        for x in range(self.k):
                print(self.centroids[x])



def main():
    k=3
    train_data = np.genfromtxt('clusters.csv', delimiter=',')
    km=KMeans()
    km.cluster(train_data)

if __name__=="__main__":
    main()
