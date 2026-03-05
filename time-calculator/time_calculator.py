** start of main.py **

def add_time(start, duration, start_day=None):
    # Split start time into hours, minutes, and period (AM/PM)
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    
    # Split duration into hours and minutes
    duration_hour, duration_minute = map(int, duration.split(':'))
    
    # Convert start time to 24-hour format
    if period == 'PM':
        start_hour += 12
    
    # Calculate total minutes
    total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute
    
    # Calculate days and remaining minutes
    days = total_minutes // (24 * 60)
    remaining_minutes = total_minutes % (24 * 60)
    
    # Calculate hours and minutes for the result
    result_hour = remaining_minutes // 60
    result_minute = remaining_minutes % 60
    
    # Determine period (AM or PM) and adjust hour if necessary
    if result_hour < 12:
        new_period = 'AM'
    else:
        new_period = 'PM'
        result_hour -= 12
    if result_hour == 0:
        result_hour = 12
    
    # Convert day of week to index
    day_index = None
    if start_day:
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        start_day_index = days_of_week.index(start_day.capitalize())
        day_index = (start_day_index + days) % 7
    
    # Determine additional day/days later
    days_later = ""
    if days == 1:
        days_later = " (next day)"
    elif days > 1:
        days_later = f" ({days} days later)"
    
    # Determine day of the week for the result
    new_day = ""
    if day_index is not None:
        new_day = ", " + days_of_week[day_index]
    
    # Construct result string
    result_time = f"{result_hour}:{result_minute:02d} {new_period}{new_day}{days_later}"
    
    return result_time


** end of main.py **

