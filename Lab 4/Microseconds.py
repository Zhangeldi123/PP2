from datetime import datetime


current_datetime = datetime.now()


result_datetime = current_datetime.replace(microsecond=0)

print("Original Datetime:", current_datetime.strftime("%Y-%m-%d %H:%M:%S.%f"))
print("Result Datetime (without microseconds):", result_datetime.strftime("%Y-%m-%d %H:%M:%S"))