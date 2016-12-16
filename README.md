# Stack Overflow Sentiment
This simple project uses Google BigQuery &amp; Google Cloud Natural Language API to analyse Stack Overflow comment sentiment. Developed using Python 2.7.x (but should work with Python 3.5). The queries and datasets used are all public. You can find the links below.

##Links

###Google Tools
https://cloud.google.com/natural-language/
https://cloud.google.com/bigquery/

###Google APIs
https://github.com/GoogleCloudPlatform/google-cloud-python/tree/master/bigquery
https://github.com/GoogleCloudPlatform/google-cloud-python/tree/master/language

###Motivation
https://cloud.google.com/blog/big-data/2016/12/google-bigquery-public-datasets-now-include-stack-overflow-q-a

##Dependencies
There are some Python modules needed. Simply run this.
```pip install -r requirements.txt```

##Public stuff

###Datasets

####Stack Overflow Public Dataset (BigQuery)
Here's the public dataset in BigQuery for Stackoverflow
https://bigquery.cloud.google.com/dataset/bigquery-public-data:stackoverflow

####My Public Dataset (BigQuery)
Here you can find the tables that I created with my queries and the results of the NL-API
https://bigquery.cloud.google.com/dataset/stackoverflow-sentiment:sentiment

###Queries

####comments_on_accepted_answers with either JavaScript, Java or Python tags
https://bigquery.cloud.google.com:443/savedquery/1056242102418:bc02f8082e1148a5bde33da5a247ea88

####comments_on_all_answers with either JavaScript, Java or Python tags
https://bigquery.cloud.google.com:443/savedquery/1056242102418:575f631a65b7448baf54c340477f1e97