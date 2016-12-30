# Stack Overflow Sentiment
This simple project uses Google BigQuery &amp; Google Cloud Natural Language API to analyse Stack Overflow comment sentiment. Developed using Python 2.7.x (but should work with Python 3.x though too). The queries and datasets used are all public. You can find the links below.

##Links

###Blog post
https://shinesolutions.com/2016/12/20/analysing-stack-overflow-comment-sentiment-using-google-cloud-platform/

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

####Best day to post a question on Stack Overflow
https://bigquery.cloud.google.com:443/savedquery/1056242102418:63c31fe61a7c4d53ae3ef22f30203881

####Correctly spelled BigQuery - it's one word! :-)
https://bigquery.cloud.google.com:443/savedquery/1056242102418:b4117babd35c41e78aa0ab8c69f42257

####Overall % sentiment
https://bigquery.cloud.google.com:443/savedquery/1056242102418:864b7503d0d3407bb97b08350fbdc311

####Overall sentiment counts
https://bigquery.cloud.google.com:443/savedquery/1056242102418:9a7847826552407aa690db60a1276feb

####Average sentiment
https://bigquery.cloud.google.com:443/savedquery/1056242102418:7b4dccb9c54b45ed86c4876df5e4794a

####Comments on questions asked by noobs for 2016 and for JavaScript, Java and Python tags
https://bigquery.cloud.google.com:443/savedquery/1056242102418:1c6c51620ee24e878cb361e0e236426b

####Counts of negative comments
https://bigquery.cloud.google.com:443/savedquery/1056242102418:57b1910592874c3fa4db79a103797cd9
