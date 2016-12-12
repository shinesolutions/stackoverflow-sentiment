import argparse
import csv
import os

from google.cloud import bigquery
from google.cloud import language
from google.cloud.bigquery import SchemaField

def main(credential_file):
    # Auth stuff setup
    # -----------------

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_file
    language_service = language.Client()
    bigquery_service = bigquery.Client()

    # Fetch users comments from BigQuery public dataset
    # -------------------------------------------------

    QUERY = '''
                SELECT id,text FROM `stackoverflow-sentiment.sentiment_user_237838.all_comments`
                  WHERE post_id IN (
                SELECT CAST(id AS INT64) FROM `bigquery-public-data.stackoverflow.posts_answers`
                  WHERE owner_user_id != '237838')
            '''
    query = bigquery_service.run_sync_query(QUERY)
    query.timeout_ms = 60000
    query.use_legacy_sql = False
    query.use_query_cache = True
    query.run()

    # Prepare a file writer to write a CSV and load to BigQuery
    # ---------------------------------------------------------

    csv_file = open('../sentiment.csv', 'wt')
    writer = csv.writer(csv_file)
    writer.writerow(('id', 'score', 'magnitude'))

    # Create the dataset & table
    # --------------------------

    dataset = bigquery_service.dataset('sentiment_user_237838')
    if not dataset.exists:
        dataset.create()
    SCHEMA = [
        SchemaField('comment_id', 'INTEGER', mode='required'),
        SchemaField('score', 'FLOAT', mode='required'),
        SchemaField('magnitude', 'FLOAT', mode='required')
    ]
    table = dataset.table('comment_sentiments', SCHEMA)
    if table.exists:
        table.delete  # truncate
    table.create()

    # Run each comment through the natural language API to get the sentiment of the comment
    # -------------------------------------------------------------------------------------

    records_processed = 0
    for row in query.rows:
        comment_id, comment = row[0], row[1]
        records_processed += 1
        print('Processing record %d with comment: "%s"' % (records_processed, comment))
        try:
            document = language_service.document_from_text(comment)
            sentiment = document.analyze_sentiment()
            writer.writerow((comment_id, sentiment.score, sentiment.magnitude))
        except Exception as e:
            print(e)

    # Upload the sentiment file to BigQuery as a table
    # ------------------------------------------------

    csv_file.flush()
    csv_file.close()
    with open(csv_file.name, 'rb') as readable:
        table.upload_from_file(readable, source_format='CSV', skip_leading_rows=1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('credential_file', help='Path to your service account key (JSON file)')
    args = parser.parse_args()
    main(args.credential_file)
