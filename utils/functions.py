# custom functions 

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score

from utils.config_reader import config_reader

config = config_reader('../config/config.json')
random_state =  config.random_state



def outliers_tukey(data:pd.DataFrame, feature:str, log_scale=False):
    """
    Identification of outliers by J.Tukey method
    - DataFrame;
    - feature to process
    - log_scale. If True, the data will be in the log scale else not.
    """
    if log_scale:
        x = np.log(data[feature])
    else:
        x = data[feature]
        
    IQR = data[feature].quantile(.75) - data[feature].quantile(.25)
  
    lower_bound = data[feature].quantile(.25) - 1.5*IQR
    upper_bound = data[feature].quantile(.75) + 1.5*IQR 
    
    outliers = data[(x < lower_bound) | (x > upper_bound)]
    cleaned = data[(x > lower_bound) & (x < upper_bound)]
    
    print('Boundaries: ',lower_bound.round(), upper_bound.round())
    boundaries = {'lower_bound':lower_bound, 
                  'upper_bound':upper_bound}
    
    return outliers, cleaned, boundaries

def get_quantity_canceled(data:pd.DataFrame)->pd.Series:
    """Returns either number of goods canceled per unique customer or NaN

    Args:
        data (DataFrame): dataframe

    Returns:
        Series: integral number of canceled goods
    """
  
    quantity_canceled = pd.Series(np.zeros(data.shape[0]), index=data.index)    
    negative_quantity = data[(data['Quantity'] < 0)].copy()
    for index, col in negative_quantity.iterrows():
        
        # get the dataframe of unique customers
        df_test = data[(data['CustomerID'] == col['CustomerID']) &
                       (data['StockCode']  == col['StockCode']) & 
                       (data['InvoiceDate'] < col['InvoiceDate']) & 
                       (data['Quantity'] > 0)].copy()
        
        # the return transaction doesn't have a customer
        if (df_test.shape[0] == 0): 
            # mark as a NaN
            quantity_canceled.loc[index] = np.nan
            
        # the return transaction has one counterparty
        elif (df_test.shape[0] == 1): 
            index_order = df_test.index[0]
            quantity_canceled.loc[index_order] = -col['Quantity']       
        
        # the return transaction has multiple counterparties
        elif (df_test.shape[0] > 1): 
            df_test.sort_index(axis=0 ,ascending=False, inplace = True)
                    
            for ind, val in df_test.iterrows():
                if val['Quantity'] < -col['Quantity']: 
                    continue
                
                quantity_canceled.loc[ind] = -col['Quantity']
                break  
              
    return quantity_canceled


def get_clustering_metrics(data:pd.DataFrame, ranges:tuple)->pd.DataFrame:
    """Get following metrics  with k-means algorythm: silhouette, inertia, and davies_bouldin_score (Calculate the extent of cluster uniqueness)

    Args:
        X (pd.DataFrame): feature matrix
        ranges (tuple): given range of clusters for an estimation

    Raises:
        ValueError: if  ranges does not contain 2 elements


    Returns:
        float: silhouette metrics
    """ 
    if len(ranges) != 2:
        raise ValueError("Ranges must cosist of 2 variables")  
    
    silhouette_res = {"silhouette": [], "cluster": [], 'inertia':[], 'db_score':[]} 
    
    for cluster_num in range(ranges[0],ranges[1]):
        # get clustering results to calculate metrics
        k_means =  KMeans(n_clusters=cluster_num, init='k-means++', 
                          n_init=10, random_state=random_state).fit(data)

        # metrics
        silhouette = silhouette_score(data, k_means.predict(data))
        inertia = k_means.inertia_
        db_score = davies_bouldin_score(data, k_means.labels_)
        
        silhouette_res["cluster"].append(cluster_num)
        silhouette_res["silhouette"].append(silhouette)
        silhouette_res["inertia"].append(inertia)
        silhouette_res["db_score"].append(db_score)
        
    silhouette_df = pd.DataFrame(silhouette_res)

    return  silhouette_df