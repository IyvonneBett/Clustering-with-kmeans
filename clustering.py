import pandas
df = pandas.read_csv('AirlinesCluster.csv')
print(df)
#clustering only works better with continous variables (ie money)
# not categorical variables

subset = df[['FlightMiles','FlightTrans','DaysSinceEnroll']]  # cluster by 3 flight miles flight trans days since enroll
# we proceed using the subset with columns only
array =subset.values
features = array[:, 0:3] # no outcome so we do clustering

# we import a model
from sklearn.cluster import KMeans
model = KMeans(n_clusters=6, random_state= 42) # we try first with 3 clusters the more clusters the more specific random state makes it well balanced
model.fit(features) # clustering process
print('Clustering...Finished')

#we find out the 3 clusters and members present in those clusters /centronoids are cluster centers 75 and 90 A same cluster
centronoids = model.cluster_centers_
dataframe = pandas.DataFrame(centronoids, columns= ['FlightMiles','FlightTrans','DaysSinceEnroll'])

print(dataframe)

#pull out data from any cluster

subset['label'] = model.labels_
cluster = subset[subset['label']==3]
print(cluster)

import xlwt
cluster.to_excel('cluster3.xls', columns=['FlightMiles','FlightTrans','DaysSinceEnroll'])

# sign in : test@modkenya.com
# pass: mwas1234@#

