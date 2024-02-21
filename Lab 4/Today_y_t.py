from datetime import datetime, timedelta


current_date = datetime.now()

yesterday_date = current_date - timedelta(days=1)
tomorrow_date = current_date + timedelta(days=1)

print("Current Date:", current_date.strftime("%Y-%m-%d"))
print("Yesterday:", yesterday_date.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow_date.strftime("%Y-%m-%d"))