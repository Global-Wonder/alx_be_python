from datetime import datetime, timedelta

def display_current_datetime():
    """
    Gets the current date and time and prints it in YYYY-MM-DD HH:MM:SS format.
    The current date/time is stored in the variable `current_date`.
    """
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted}")
    return current_date  # return it in case other functions want to reuse it

def calculate_future_date(days):
    """
    Adds `days` (int) to the current date and prints the resulting date in YYYY-MM-DD format.
    The future date is saved in the variable `future_date`.
    """
    # Use current moment as base
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    return future_date

def main():
    # show the current date/time and keep a reference if needed
    current_date = display_current_datetime()

    # Ask the user for number of days and validate input
    while True:
        user_input = input("Enter the number of days to add to the current date: ").strip()
        try:
            days = int(user_input)
            break
        except ValueError:
            print("Invalid input. Please enter an integer number of days (e.g., 10 or -5).")

    # calculate and print future date
    calculate_future_date(days)

if __name__ == "__main__":
    main()
