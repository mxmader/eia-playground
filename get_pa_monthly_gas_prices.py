#!/usr/bin/env python3
import requests
import os

api_key = os.environ.get('eia_api_key')
base_url = 'http://api.eia.gov/series'
series_id = 'NG.N3035PA3.M'
local_filename = '{}.json'.format(series_id)

# NOTE the stream=True parameter below
with requests.get(base_url, params={'api_key=': api_key,
                                    'series_id': series_id},
                  stream=True) as r:
    r.raise_for_status()
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                # f.flush()

print('wrote: {}'.format(local_filename))
