# Stackoverflow Sentiment
This simple project uses Google BigQuery &amp; Google Cloud Natural Language API to analyse a user's Stackoverflow comment sentiment. Developed using Python 2.7.x (but should work with Python 3.5). The queries and datasets used are all public. You can find the links below.

##Links

###Google Tools
https://cloud.google.com/natural-language/
https://cloud.google.com/bigquery/

###Motivation
https://hackernoon.com/the-decline-of-stack-overflow-7cb69faa575d#.lybav9o7b
http://stackexchange.com/users/85265/andrew-barber?tab=activity

##Dependencies
There are some Python modules needed. Simply run this.
```pip install -r requirements.txt```

##Public stuff

###Datasets

####Stackoverflow Public Dataset (BigQuery)
Here's the public dataset in BigQuery for Stackoverflow
https://bigquery.cloud.google.com/dataset/bigquery-public-data:stackoverflow

####My Public Dataset (BigQuery)
Here you can find the tables that I created after running the comments through the natural language API.
https://bigquery.cloud.google.com/dataset/stackoverflow-sentiment:sentiment_user_237838

###Queries

####stackoverflow_comment_sentiment
The query used to join the results of the sentiment analysis back to the Stackoverflow comment dataset
https://bigquery.cloud.google.com:443/savedquery/1056242102418:ef19879113674493b4c405d53d5856ae

####average sentiment
Calculates the average sentiment
https://bigquery.cloud.google.com:443/savedquery/1056242102418:7d30623b78dc4dc18f850296e27b8d14

####average_sentiment_by_month_and_year
The sentiment aggregated by month and year
https://bigquery.cloud.google.com:443/savedquery/1056242102418:117d7f326c824d0a9a5f6a26936d165f

####top_ten_negative_sentiment_comments
The top ten negatively scored comments
https://bigquery.cloud.google.com:443/savedquery/1056242102418:77a53cfc96dd4e1aa5378902fcd88297

####top_ten_positive_sentiment_comments
The top ten positively scored comments
https://bigquery.cloud.google.com:443/savedquery/1056242102418:fe549533d12e4f6ab61b25fbcfcc96ec

###Data Studio Report (Data Studio)
This is the (very simple) chart I created for looking at the trend of sentiment over time
https://datastudio.google.com/open/0B_46UYrhJn-ZbmFVSE5uMlR6d0k
