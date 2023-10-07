import twitter
import pandas as pd
import numpy as np
import os

# Attention: As of 5th may 2023, we no longer have developer access so the keys dont work
def oauth_login():
    CONSUMER_KEY = 'qdfdJzOYgSeZBOTP2L2vSLGes'
    CONSUMER_SECRET = 'fbtYDV2V2O2ZIVklKLAnRSqQo3aSO9lwJWw978XXl0gwMUrlor'
    OAUTH_TOKEN = '910314062176772096-veyDRBbYb54QqOU9r4jhIBADEaotHMb'
    OAUTH_TOKEN_SECRET = 'MV71HCd51fal91lzXiJeB501WR9eFEY8SpXEcQFnpyuZ4'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)

    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api


def twitter_search(twitter_api, q, max_results, lang='en', place_country='US', **kw):

    search_results = twitter_api.search.tweets(q=q, count=1000, lang=lang, place_country=place_country, **kw)

    statuses = search_results['statuses']

    max_results = min(1000, max_results)

    for _ in range(10):
        try:
            next_results = search_results['search_metadata']['next_results']
        except KeyError as e:
            break

        kwargs = dict([kv.split('=')
                       for kv in next_results[1:].split("&")])

        search_results = twitter_api.search.tweets(**kwargs)
        statuses += search_results['statuses']

        if len(statuses) > max_results:
            break

    return statuses


def save_to_pandas(data, fname):
    df = pd.DataFrame.from_records(data)
    df.to_csv(fname)
    return df


q = ['tech','Technology' ,'tech','computerscience', 'economy','capitalisim','elections ', 'government' , 'politics']

twitter_api = oauth_login()
for i in q:
    results = twitter_search(twitter_api, i, max_results=2000)

    df = save_to_pandas(results, '/Users/himanshuchuri/Desktop/SMDM/OldData/{0}us_csv.csv'.format(i))
    print(i)

#We downloaded files for each of the words in the list above and then amnually merged those files as per the topics mentioned in the report.
