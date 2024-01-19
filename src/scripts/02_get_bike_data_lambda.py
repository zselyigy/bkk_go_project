from datetime import datetime
import pandas as pd
import requests

# get the headers of the taxi data
url = 'https://futar.bkk.hu/api/query/v1/ws/otp/api/where/bicycle-rental.json?key=bd29005b-80cb-499b-968b-c7be1e6b3d37&version=3&appVersion=1&includeReferences=false'

response = requests.get(url)
raw_data = response.json()

# create a DataFrame from the detailed data
bicycle_rental = pd.DataFrame(raw_data['data']['list'])

# write the DataFrame to csv with a unique time id
timestamp_milliseconds = raw_data['currentTime'] / 1000  # Convert milliseconds to seconds
formatted_date_time = datetime.utcfromtimestamp(timestamp_milliseconds).strftime('%Y-%m-%d-%H-%M')

bicycle_rental.to_csv('bicycle_rental_data_' + str(formatted_date_time) + '.csv',
                      index=False)
