def is_leap_year(year):
    """Check if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year=None):
    """Return the number of days in the given month, considering leap years for February."""
    month_days = {
        "January": 31,
        "February": 28,  # 29 in a leap year
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }
    
    days = month_days.get(month)
    if days is None:
        return "Invalid month name."
    if month == "February" and year is not None and is_leap_year(year):
        days = 29
    return days

def main():
    # Input: Entering month name
    month = input("Enter the month name: ")
    
    if month == "February":
        # For February, also ask for the year
        year = int(input("Enter the year: "))
        days = days_in_month(month, year)
    else:
        days = days_in_month(month)
    
    print(f"The number of days in {month} is: {days}")

# Run the main function
if __name__ == "__main__":
    main()
