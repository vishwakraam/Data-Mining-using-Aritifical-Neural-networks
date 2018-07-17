# Data-Mining-using-Aritifical-Neural-networks
Missing Data imputation using Self organizing map 

KNN clustering algorithm:

from fancyimpute import KNN    
# X is the complete data matrix
# X_incomplete has the same values as X except a subset have been replace with NaN

# 3 nearest rows which have a feature to fill in each row's missing features
X_filled_knn = KNN(k=3).complete(X_incomplete)
