# web_shop_customers_segmentation



## Content

* [Summary](README.md#Summary)  
* [Project description](README.md#Project-description)  
* [Data and methods](README.md#Data-and-methods)
* [Results](README.md#Results) 
* [Project structure](README.md#Project-structure)
* [Tables](README.md#Tables)  

---

## Summary
 

## Project description
To increase its revenue, companies customized their pricing models for every customer segment. Although these pricing strategies are a fundamental part of any digital company's business models, they may differ by time. Customer segment sizes as well as customers behavior within the segment are subjects of continuous change since they depends of multiple factors such as: economy, competitors prices, perception of goods worth, location, season, and so on. Recent improvements in Artificial Intelligence an Machine learnig allow to create better pricing models that consequently increases competition between online retail platforms. To win this challenge, a company has to identify new customer needs and segments constantly to 
customize its pricing strategies.

The project is devoted to clients segmentation for an UK web shop  with several unsupervised clustering algorithms. Segmentation helps to identify common customer behavior patterns and allows to target customers with tailored marketing strategies. 

## Data and methods
The dataset contains information about 541909 different transactions which have been recorded between the years 2010 and 2011. These transactions, however, include canceled purchases which should be deducted to calculate fair integral value of transactions by customer. In result, the mean customer value is $21 \pm 68 $ sterlings (fig.1). Meanwhile other [encoded events](https://www.kaggle.com/code/fabiendaniel/customer-segmentation/notebook) (fig.2 , table 1) such as shipment expenditures, bank charges, and etc. should not be accounted because they hinder understanding of real purchasing power of clients.

<center> <img src = "./figures/fig_1.png"  alt="drawing" style="width:400px;"> <img src = "./figures/fig_2.png"  alt="drawing" style="width:400px;"></center>

Analyzing customer revenue distribution by country it can be seen that most transactions are from the UK (82 %); customers from the Netherlands and Ireland generate about 3% each, and other countries returns about 12 % in sum.

<center> <img src = "./figures/fig_3.png"  alt="drawing" style="width:400px;"> </center>


The optimal number of clusters was identified using several techniques such as: enertia estimation (fig.1 A), and elbow methods (fig.1 B). The silhouette method indicates that it would be better to spread customers by 3 distinct clusters that is easy to use and understand. In contrast to the silhouette method, clustering by the distortion score and inertia do not clearly shows the optimal number of clusters.



## Results
For the bank perspective, it is worth to increase revenue from credit loans. Charges value depends of sum of purchases, as well as of other related factors. Thus two main features were chosen to represent clustering results such as credit limit and Payments. 

To get best results several clustering algorythms were compared: k-means, DBSCAN, agglomerative clustering. DBSCAN, for instance did not recognized distinct clusters since the data is rather evenly distributed within the analyzed features. Unlike DBSCAN, Agglomerative Clustering as well as K-means splitted the data well. The latter method identified 3 clusters of customers  and colored them as follows (fig.3):
* 0 (green color, on the left bottom corner) - 6209 customers with low credit limit, and payments from low to moderate.
* 1 (orange color, on the right bottom corner) - 2556 customers with moderate and high credit limits and payments
- 2 (blue color on the right top corner) - 185 customers with large amount of payments.

<center> <img src = "./figures/fig_3.png"  alt="drawing" style="width:600px;"> </center>

As it can be seen from the fig.3 above, clusters are imbalanced. Thus it is not known whether clusters posses of common dinstinct features  

Customers within the largest 0th segment can be characterized by following features (by descenidg of the feature significance):
- large purchases and big expenditures
- borrowing cash against the card's line of credit
- they rarely repaid borrowed sum on their credit balance
- their 'MINIMUM_PAYMENTS' amounts are quite large of $ 677 \pm 19347$ of a currency. In case the credit card minimum payments due value is calculated as 5% from the total outstanding amount, borrowers owe some succifient amounts of money to the bank
- most of users has a positive card balance of $ 936 \pm 19347$, and notably, the balance is updated regularly

In result, the 0th segment represent the most active customers in terms of revenue generation for the bank.

<center> <img src = "./figures/fig_4.png"  alt="drawing" style="width:400px;"> <img src = "./figures/fig_5.png"  alt="drawing" style="width:400px;"> 
<img src = "./figures/fig_6.png"  alt="drawing" style="width:400px;"> </center> 


## Project structure

<details>
  <summary>display project structure </summary>


```Python
web_shop_customers_segmentation
├── .git
├── .gitignore
├── config
│   └── config.json         # configuration parameters
├── data                    # data archive
│   └── webshop_data.zip  
├── figures                 # images storage
│   ├── fig_1.png
.....
│   └── fig_6.png
├── LICENSE
├── models                  # models storage
├── notebooks               # project notebooks storage
│   └── webshop_segmentation.ipynb
├── project tree.ipynb
├── README.md
└── utils                   # custom functions and applications
    ├── config_reader.py
    └──  functions.py
    

```
</details>

## Tables

<details>
  <summary>Table 1.  statuses</summary>

|code| status |
|:-- | :-- |
| POST| POSTAGE  |
| C2  | shipment costs |
| M   | Manual   |
| BANK CHARGES|Bank Charges   |
| PADS | PADS TO MATCH ALL CUSHIONS |   
| DOT  | DOTCOM POSTAGE |
| D    | Discount       | 

</details>