from datetime import datetime, timedelta

current_date = datetime.now()

result_date = current_date - timedelta(days=5)


print("Current Date:", current_date.strftime("%Y-%m-%d"))
print("Result Date (after subtracting 5 days):", result_date.strftime("%Y-%m-%d"))
