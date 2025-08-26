import pandas as pd
import numpy as np
from datetime import datetime

# File to save customer records
DATA_FILE = "customers.csv"

# Sample items (like menu)
items = ["Pizza", "Burger", "Pasta", "Sandwich", "Coffee"]
prices = np.array([200, 120, 150, 100, 80])   # using numpy array

# Load existing customer data if available
try:
    customers_df = pd.read_csv(DATA_FILE)
except FileNotFoundError:
    customers_df = pd.DataFrame(columns=["Name", "Orders", "Total", "DateTime"])

def display_items():
    print("\nAvailable Items:")
    for i, (item, price) in enumerate(zip(items, prices), start=1):
        print(f"{i}. {item} - Rs.{price}")

def place_order(customer_name):
    global customers_df   # ✅ Declare global

    display_items()
    order_list = []
    total = 0

    while True:
        choice = input("\nEnter item number to order (or 0 to finish): ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                break
            elif 1 <= choice <= len(items):
                qty = int(input(f"Enter quantity of {items[choice-1]}: "))
                cost = prices[choice-1] * qty
                order_list.append(f"{items[choice-1]} x{qty} (Rs.{cost})")
                total += cost
            else:
                print("Invalid choice, try again.")
        else:
            print("Enter a valid number.")

    # Current date & time
    order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\nYour Order Summary:")
    for o in order_list:
        print("-", o)
    print("Total Bill:", total)
    print("Order Date & Time:", order_time)

    # Save order (always add a new row with timestamp)
    new_row = pd.DataFrame([[customer_name, ", ".join(order_list), total, order_time]], 
                           columns=["Name", "Orders", "Total", "DateTime"])
    customers_df = pd.concat([customers_df, new_row], ignore_index=True)

    # Save to CSV
    customers_df.to_csv(DATA_FILE, index=False)
    print("\nCustomer data saved successfully!\n")

def view_customers():
    if customers_df.empty:
        print("No records yet.")
    else:
        print("\n--- Customer Records ---")
        print(customers_df)

def average_custom_range():
    if customers_df.empty:
        print("No records yet.")
        return
    
    # Convert DateTime column to datetime type
    customers_df["DateTime"] = pd.to_datetime(customers_df["DateTime"])

    # User inputs
    date_str = input("Enter date (YYYY-MM-DD) or press Enter for all dates: ").strip()
    start_time_str = input("Enter start time (HH:MM, 24-hr) or press Enter for 00:00: ").strip()
    end_time_str = input("Enter end time (HH:MM, 24-hr) or press Enter for 23:59: ").strip()

    # Default values
    if not start_time_str:
        start_time_str = "00:00"
    if not end_time_str:
        end_time_str = "23:59"

    try:
        # Build datetime filters
        if date_str:
            start_dt = pd.to_datetime(f"{date_str} {start_time_str}")
            end_dt = pd.to_datetime(f"{date_str} {end_time_str}")
            mask = (customers_df["DateTime"] >= start_dt) & (customers_df["DateTime"] <= end_dt)
        else:
            # No date filter → just filter by time (ignores date)
            start_hour, start_minute = map(int, start_time_str.split(":"))
            end_hour, end_minute = map(int, end_time_str.split(":"))
            mask = (
                (customers_df["DateTime"].dt.hour * 60 + customers_df["DateTime"].dt.minute >= start_hour*60 + start_minute)
                & (customers_df["DateTime"].dt.hour * 60 + customers_df["DateTime"].dt.minute <= end_hour*60 + end_minute)
            )

        filtered = customers_df.loc[mask]

        if filtered.empty:
            print("\nNo orders found in the given range.")
        else:
            avg_total = filtered["Total"].mean()
            print("\n--- Orders in Selected Range ---")
            print(filtered)
            print(f"\nAverage order amount in selected range is Rs.{avg_total:.2f}")
    except Exception as e:
        print("Error:", e)
        print("Please enter valid date/time format!")

def main():
    while True:
        print("\n--- Customer Ordering System ---")
        print("1. Add/Order for Customer")
        print("2. View All Customers")
        print("3. Average Orders (Choose Date & Time Range)")
        print("4. Exit")

        choice = input("Enter your choice: ")

        match choice:   # Python’s version of switch-case
            case "1":
                name = input("Enter customer name: ").strip()
                place_order(name)
            case "2":
                view_customers()
            case "3":
                average_custom_range()
            case "4":
                print("Exiting program... Goodbye!")
                break
            case _:
                print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
