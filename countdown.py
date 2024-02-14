import requests
import datetime

def get_match_start_time(event_key, match_number, api_key):
    url = f"https://www.thebluealliance.com/api/v3/match/{event_key}_qm{match_number}"
    headers = {"X-TBA-Auth-Key": api_key}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        match_data = response.json()
        start_time = match_data['time']
        return start_time
    else:
        print(f"Error: {response.status_code}")
        return None

def unix_epoch_to_datetime(unix_epoch_time):
  return datetime.datetime.utcfromtimestamp(unix_epoch_time)

def compare_times(current_time, specified_time):
  nowSeconds = current_time.hour*3600 + current_time.minute*60 + current_time.second
  matchSeconds = specified_time.hour*3600 + specified_time.minute*60 + specified_time.second
  dSeconds = abs(nowSeconds - matchSeconds)
  return datetime.timedelta(seconds=dSeconds)


current_datetime = datetime.datetime.now()

    # Replace these values with your actual event key, match number, and API key
event_key = "2022casj"  # Example: "2022week0"
match_number = "2"  # Example: "1"
api_key = "5ZKfZwsaymxkFPLITQ6ouKISEqV6b6IKABmg79JdDYtgTEIQkIznJRc2cVy35mcz"  # Example: "abcd1234efgh5678"

start_time = get_match_start_time(event_key, match_number, api_key)
if start_time:
    unix_epoch_time = start_time

    datetime_obj = unix_epoch_to_datetime(unix_epoch_time)
    print(compare_times(current_datetime, datetime_obj))
    print(f"Current datetime: {current_datetime}")
    print("Datetime:", datetime_obj)

