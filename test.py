from datetime import datetime

current_datetime = datetime.now()
print(current_datetime)

formatted_date = current_datetime.strftime("%d-%m-%Y")
print(formatted_date)


