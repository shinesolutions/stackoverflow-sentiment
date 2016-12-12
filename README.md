# Stack Overflow Sentiment
This simple project uses Google BigQuery &amp; Google Cloud Natural Language API to analyse a user's Stack Overflow comment sentiment. Developed using Python 2.7.x (but should work with Python 3.5). The queries and datasets used are all public. You can find the links below.

##Links

###Google Tools
https://cloud.google.com/natural-language/
https://cloud.google.com/bigquery/

###Google APIs
https://github.com/GoogleCloudPlatform/google-cloud-python/tree/master/bigquery
https://github.com/GoogleCloudPlatform/google-cloud-python/tree/master/language

###Motivation
https://hackernoon.com/the-decline-of-stack-overflow-7cb69faa575d#.lybav9o7b
http://stackexchange.com/users/85265/andrew-barber?tab=activity

##Dependencies
There are some Python modules needed. Simply run this.
```pip install -r requirements.txt```

##Public stuff

###Datasets

####Stack Overflow Public Dataset (BigQuery)
Here's the public dataset in BigQuery for Stackoverflow
https://bigquery.cloud.google.com/dataset/bigquery-public-data:stackoverflow

####My Public Dataset (BigQuery)
Here you can find the tables that I created after running the comments through the natural language API.
https://bigquery.cloud.google.com/dataset/stackoverflow-sentiment:sentiment_user_237838
