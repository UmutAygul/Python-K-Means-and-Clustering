
from sklearn.cluster import KMeans,AffinityPropagation
from sklearn.cluster import DBSCAN

import itertools

import numpy as np
import matplotlib.pyplot as plt


from itertools import cycle
from sklearn.cluster import MeanShift, estimate_bandwidth

from sklearn.cluster import SpectralClustering

from sklearn.cluster import AgglomerativeClustering 
from sklearn.metrics import pairwise_distances_argmin_min


class Clustering:
    
    """! 
    The Mathematical functions of clustering classes.
    
    """
    def __init__(self):
        pass
    
    def spectralcluster(self,X):
        """! 
        SpectralCluster is calculated and printed here.
        @param x is stores the data read from X from txt
        @param X is the incoming data from txt
        @param pair takes the pairs of clusters
        @param far takes the Farthest points
        @param closest is the closest points of the clusters
        
        
        """
  
        self.bos()
        x=X
        # self.iterate=self.nc
        affinitychoosen="nearest_neighbors"
        sj = SpectralClustering(n_clusters=self.nc, affinity=affinitychoosen,
                                   assign_labels='kmeans').fit(x)
        self.labels=sj.labels_
        ##labels function
        b="Cluster labels:"+str(self.labels)
        amg=[]
    
        
        pair,far,c=self.farthandpair(self.nc,self.labels)
        
        self.pairs=pair
        
        
        
        for i in range (self.nc-1,-1,-1):
           
            y=(self.ClusterIndicesNumpy(i,self.labels))
            ss = np.average(x[y], axis=0) #https://blog.finxter.com/numpy-average-along-axis/
            amg.append(ss)
            plt.scatter(ss[0], ss[1],c="r",marker="x", s=70, linewidths=3, zorder=10) #merkezleri bas
            

        
        for i in range(len(x)):
            plt.text(x[i,0],x[i,1],str(i))
        
        closest, _ = pairwise_distances_argmin_min(amg, x)
        # print("Closest ones:",closest)
        
        plt.scatter(x[:, 0], x[:, 1], c=self.labels,
                    s=50, cmap='viridis');


        
        b="Closes ones: "+str(closest)+"\n"+b+"\n"+"Farthest ones: "+"["+str(far)+']'+'\n'+"Possible pairs "+str(self.pairs)
        
        # self.hubstext.setText(b)
        
        
        f=self.objective_function()
        f="\n"+"Objective Function :"+str(f)
        name="spectralcluster.png"
        self.ayni(name,self.labels)    
        b=b+str(f)
        self.label_6.setText(b)
        
        
        # plt.savefig(name)
        # plt.close()
        # plt.title(f'Estimated number of clusters = {len(closest)}')
        # self.labelpixmap(name)
        # self.clusterenable(True)
        
        
    def meanshift(self,X):
        """! 
        meanshift is calculated and printed here.
        @param X is the incoming data from txt
        @param labels_unique takes the different groups number
        
        @param oj takes the Objective function
        @param self.pairs takes the pairs of clusters
        
        
        """
  
        self.bos()
        X=self.X
        num_samples_total = len(X)

        bandwidth = estimate_bandwidth(X, quantile=self.quantile, n_samples=num_samples_total)
        
        meanshift = MeanShift(bandwidth=bandwidth).fit(X)
        ## Fit Mean Shift with Scikit
        self.labels = meanshift.labels_
        ##Labels
        
        labels_unique = np.unique(self.labels)
        n_clusters_ = len(labels_unique)
        self.nc=n_clusters_
        # self.iterate=self.nc
        closest, _ = pairwise_distances_argmin_min(meanshift.cluster_centers_, X)
        # print("Closest ones:",closest)

        
        cluster_center=meanshift.cluster_centers_
        plt.scatter(cluster_center[:, 0], cluster_center[:, 1],c="r",marker="x", s=70, linewidths=3, zorder=10) #merkezleri bas


        for i in range(len(X)):
            plt.text(X[i,0],X[i,1],str(i))
        

        pair,y,c=self.farthandpair(n_clusters_,self.labels)
        self.pairs=pair
        
        txt="Closest ones: "+str(closest)+"\n"+"Cluster labels: "+str(self.labels)+"\n"+"Farthest ones: "+"["+str(y)+']'+"\n"+"Possible pairs "+str(self.pairs)
        c=c+txt
        # self.hubstext.setText(txt)

        # Predict the cluster for all the samples
        P = meanshift.predict(X)

        # Generate scatter plot for training data
        colors = list(map(lambda x: '#3b4cc0' if x == 1 else '#b40426' if x == 2 else '#67c614' if x==3 else
                          '#2f4f4f' if x==4 else '#ffff00' if x==5 else '#ff1493'
                          if x==6 else '#ffa500' if x==7 else '#000000'if x==8 else '#00bfff' if x==9 else '#c71585', P))
        plt.scatter(X[:,0], X[:,1], c=colors, marker="o", picker=True)
        

        
        
        
        plt.title(f'Estimated number of clusters = {n_clusters_}')
        name="ms.png"
        self.ayni(name,cluster_center)
        oj=self.objective_function
        c=c+"\n"+"Objective function: "+str(oj)
        self.label_6.setText(c)
        # plt.savefig(name)
        # plt.close()

        # self.labelpixmap(name)
        # self.clusterenable(True)
        
        
        
    def hierarca(self,X): 
        """! 
        hierarca is calculated and printed here.
        @param hiear takes the specific hierarchical c. function
        
        
        """
        self.bos()
        X=self.X
        hier=AgglomerativeClustering(linkage=self.link)
        hier.fit(X)
        self.labels=hier.labels_
        unique_labels = list(set(self.labels))
        self.nc=len(unique_labels)
        # self.iterate=self.nc
        amg=[]

        colors = list(map(lambda x: '#3b4cc0' if x == 1 else '#b40426' if x == 2 else '#67c614' if x==3 else
                          '#2f4f4f' if x==4 else '#ffff00' if x==5 else '#ff1493'
                          if x==6 else '#ffa500' if x==7 else '#000000'if x==8 else '#00bfff' if x==9 else '#c71585', self.labels))
        plt.scatter(X[:,0], X[:,1], c=colors, marker="o", picker=True)
        for i in range(len(X)):
            plt.text(X[i,0],X[i,1],str(i))
        
        pair,far,c=self.farthandpair(len(unique_labels),self.labels)
        self.pairs=pair
        for i in range (len(unique_labels)-1,-1,-1):
            y=(self.ClusterIndicesNumpy(i,self.labels))
            ss = np.average(X[y], axis=0) #https://blog.finxter.com/numpy-average-along-axis/ #merkezleri bul
            amg.append(ss)
            plt.scatter(ss[0], ss[1],c="r",marker="x", s=70, linewidths=3, zorder=10) #merkezleri bas
            
     
        
        closest, _ = pairwise_distances_argmin_min(amg, X)
        
        
        
        a="Closes ones:"+str(closest)+"\n"+"Cluster labels:"+str(self.labels)+"\n"+"Farthest ones: "+"["+str(far)+']'+"\n"+"Pairs: "+str(self.pairs)
        c=c+a
        
        name="kmean.png"
        self.ayni(name,(unique_labels))
        oj=self.objective_function()
        c=c+"\n"+"Objective Function is:"+str(oj)
        
        self.label_6.setText(c)
        
        # plt.title('Estimated number of clusters: % d' % len(unique_labels))
        # plt.savefig(name)
        # plt.close()
        # self.labelpixmap(name)
        # self.clusterenable(True)
    
    

        
        
        
    def affinity(self,X):
        """! 
        affinity is calculated and printed here.
        @param af takes the specific hierarchical c. function
        
        
        """
        self.bos()
        X=self.X
        
        af = AffinityPropagation(max_iter=self.maxiter,convergence_iter=self.convergenceiter).fit(X)
        self.labels = af.labels_
        cluster_centers_indices = af.cluster_centers_indices_
        print(cluster_centers_indices)
        # print("Direk center olanlar. alt ust aynı.",cluster_centers_indices)
        cluster_center=af.cluster_centers_
        # self.iterate=len(cluster_center)

        for i in range(len(X)):
            plt.text(X[i,0],X[i,1],str(i))

        n_clusters_ = len(cluster_centers_indices)
        self.nc=n_clusters_


        

        x=''
        pair,y,c=self.farthandpair(n_clusters_,self.labels)
        self.pairs=pair
        
        b="Closest ones are:"+str(cluster_centers_indices)+"\n"+"Cluster labels:"+str(self.labels)+"\n"+"Farthest ones:"+"["+str(y)+']'+"\n"+"Possible Pairs: "+str(self.pairs)
        
        
        colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
        for k, col in zip(range(n_clusters_), colors):
            class_members = self.labels == k
            cluster_center = X[cluster_centers_indices[k]]
            plt.plot(X[class_members, 0], X[class_members, 1], col + '.') #nokta şeklinde belirtiyor tüm üyeleri 
            plt.plot(cluster_center[0], cluster_center[1], 'o',
                      markerfacecolor = col, markeredgecolor ='k',
                      markersize = 14)  #centerları büyük yuvarlağa alıyoruz.
          
            for x in X[class_members]:
                plt.plot([cluster_center[0], x[0]], 
                          [cluster_center[1], x[1]], col)#bağlantılar kuruyor
        
        name="aff.png"
        self.ayni(name,cluster_center)
        
        
        oj=self.objective_function()
        b=b+"\n"+c+"\n"+"Objective Function: "+str(oj)
        self.label_6.setText(b)
        
        
        # plt.title('Estimated number of clusters: % d' % n_clusters_)
        # plt.savefig(name)
        # plt.close()
        # self.labelpixmap(name)
        # self.clusterenable(True)
        
        
    def kmean(self,X):
        """! 
        K-mean is calculated and printed here.
        @param KMeans is a specific function fo Kmean
        @param The distance from the centers of all 10 points is calculated by taking the squares. One by one, the farthest one is chosen.
        

        """
        self.bos()
        X=self.X
        num_classes = self.nc
        # self.iterate=self.nc
        kmeans = KMeans(init=self.initv, n_clusters=num_classes,max_iter= self.mi,algorithm=self.algorit)
        kmeans.fit(X)
        centroids = kmeans.cluster_centers_

        self.labels=kmeans.labels_
        labels = kmeans.labels_
        plt.scatter(centroids[:, 0], centroids[:, 1], marker="x", s=70, linewidths=3, zorder=10) #merkezleri bas
        
        x=''
        
        for i in range (self.nc-1,-1,-1):

            y=(self.ClusterIndicesNumpy(i,labels))
            
            z='Cluster'+str(i)+"--->"
            
            x=z+' '+str(y)+"\n"+str(x)
        
        # self.nodextext.setText(str(x))
                
        P = kmeans.predict(X)
        
        # Generate scatter plot for training data
        colors = list(map(lambda x: '#3b4cc0' if x == 1 else '#b40426' if x == 2 else '#67c614' if x==3 else
                          '#2f4f4f' if x==4 else '#ffff00' if x==5 else '#ff1493'
                          if x==6 else '#ffa500' if x==7 else '#000000'if x==8 else '#00bfff' if x==9 else '#c71585', P))
        plt.scatter(X[:,0], X[:,1], c=colors, picker=True)  #for döngüsü yerine. noktaları bas
        
        
        for i in range(len(X)):
            plt.text(X[i,0],X[i,1],str(i))
            
        # dist=kmeans.transform(X)    
        # print(dist)
        
        center_dists = np.array([kmeans.transform(X)[i][y] for i,y in enumerate(labels)]) #10noktanın da merkezlerine olan uzaklığı
                                                                                        #kareler alınarak hesaplanıyo tek tek en uzak olan secılıyo
        self.central_nodes=center_dists
        # print(center_dists)
        
        max_indices = []
        for label in np.unique(kmeans.labels_):
            X_label_indices = np.where(labels==label)[0]
            max_label_idx = X_label_indices[np.argmax(center_dists[labels==label])]
            max_indices.append(max_label_idx)
        
        
        
        
        closest, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_, X)

        b="\n"+"Closest ones are:"+str(closest)
        
  
        self.pairs=list(itertools.combinations((max_indices), 2)) 

        
        a="Farthest of nodes: "+str(max_indices)+b+"\n"+"Cluster labels:"+str(labels)+"\n"+"Possible pairs: "+str(self.pairs)
        # self.hubstext.setText(str(a))
        x=x+a+"\n"
        
        po=[]
        for i in range (len(self.pairs)):
            
            po.append(max_indices[0]
                            +0.75*(abs(max_indices[0]-max_indices[1]))
                                    +max_indices[1])
        
        self.objective_func=po[np.argmax(po)]
        print(po)
        # print("Objective Function:",self.objective_func)
        name="kmean.png" 
        self.ayni(name,centroids)
        
        self.label_6.setText(x+("Objection function is:")+str(self.objective_func))
        # plt.title('Estimated number of clusters: % d' % len(centroids))  
        # plt.savefig(name)
        # plt.close()
        # self.labelpixmap(name)
        # self.clusterenable(True)
     