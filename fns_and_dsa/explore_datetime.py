import datetime
def display_current_datetime():
    current_datetime = datetime.datetime.now()
    current_date = current_datetime.date()
    print(f"Current date and time: {current_datetime.strftime("%Y-%m-%d %H:%M:%S")}")
display_current_datetime()
number_of_days = int(input("Enter the number of days to add to the current date: "))
def calculate_future_date():
    current_datetime = datetime.datetime.now()
    future_date = current_datetime + datetime.timedelta(days=number_of_days)
    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")
calculate_future_date()