from datetime import datetime

# Get user input for the two dates
date1_str = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date2_str = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")

# Convert user input strings to datetime objects
date1 = datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")

# Calculate the time difference
time_difference = int(date2 - date1)
if time_difference < 0:
     real_time_difference = time_difference + 2*time_difference
else:
     real_time_difference = time_difference

# Extract the difference in seconds
difference_in_seconds = real_time_difference.total_seconds()

# Display the result
print(f"Date 1: {date1}")
print(f"Date 2: {date2}")
print(f"Difference in seconds: {difference_in_seconds} seconds")