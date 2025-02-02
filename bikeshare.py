import time
import pandas as pd
import numpy as np

# Dictionary containing city data file names.
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
   
    print('Hello! Let\'s explore some US bikeshare data!')

    # Get user input for city.
    while True:
        city = input("Choose a city: Chicago, New York City, or Washington: ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid input. Please choose a valid city.")
    
    # Get user input for month
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("Choose a month: January, February, March, April, May, June, or 'all' to select all months: ").lower()
        if month in months:
            break
        else:
            print("Invalid input. Please choose a valid month or 'all'.")
    
    # Get user input for day
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input("Choose a day: Monday, Tuesday, ..., Sunday, or 'all' to select all days: ").lower()
        if day in days:
            break
        else:
            print("Invalid input. Please choose a valid day or 'all'.")
    
    print('-' * 40)
    return city, month, day

def load_data(city, month, day):
    
    try:
        # Load city data into a dataframe
        df = pd.read_csv(CITY_DATA[city])
    except FileNotFoundError:
        print(f"Data file for {city} not found. Please make sure the file exists.")
        exit()

    # Convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month, day, and hour from Start Time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    df['hour'] = df['Start Time'].dt.hour

    # Filter by month if user specified one
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_index = months.index(month) + 1
        df = df[df['month'] == month_index]

    # Filter by day if user specified one
    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
   
    print('\nCalculating the most frequent times of travel...\n')
    start_time = time.time()

    # Most common month
    common_month = df['month'].mode()[0]
    print(f"Most common month: {common_month}")

    # Most common day of the week
    common_day = df['day_of_week'].mode()[0]
    print(f"Most common day: {common_day}")

    # Most common start hour
    common_hour = df['hour'].mode()[0]
    print(f"Most common start hour: {common_hour}")

    print(f"\nThis took {time.time() - start_time:.2f} seconds.")
    print('-' * 40)

def station_stats(df):
    
    print('\nCalculating the most popular stations and trips...\n')
    start_time = time.time()

    # Most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f"Most common start station: {common_start_station}")

    # Most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f"Most common end station: {common_end_station}")

    # Most frequent trip combination
    df['trip'] = df['Start Station'] + " to " + df['End Station']
    common_trip = df['trip'].mode()[0]
    print(f"Most common trip: {common_trip}")

    print(f"\nThis took {time.time() - start_time:.2f} seconds.")
    print('-' * 40)

def trip_duration_stats(df):
   
    print('\nCalculating trip duration statistics...\n')
    start_time = time.time()

    # Total travel time
    total_duration = df['Trip Duration'].sum()
    print(f"Total travel time: {total_duration} seconds")

    # Average travel time
    mean_duration = df['Trip Duration'].mean()
    print(f"Average travel time: {mean_duration:.2f} seconds")

    print(f"\nThis took {time.time() - start_time:.2f} seconds.")
    print('-' * 40)

def user_stats(df):
   
    print('\nCalculating user statistics...\n')
    start_time = time.time()

    # Counts of user types
    user_types = df['User Type'].value_counts()
    print(f"User types:\n{user_types}")

    # Counts of genders (if available)
    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()
        print(f"\nGender counts:\n{gender_counts}")

    # Birth year statistics (if available)
    if 'Birth Year' in df:
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f"\nEarliest birth year: {earliest_year}")
        print(f"Most recent birth year: {most_recent_year}")
        print(f"Most common birth year: {common_year}")

    print(f"\nThis took {time.time() - start_time:.2f} seconds.")
    print('-' * 40)

def display_raw_data(df):
   
    start = 0
    while True:
        show_data = input("Would you like to see 5 lines of raw data? Enter 'yes' or 'no': ").lower()
        if show_data == 'yes':
            print(df.iloc[start:start + 5])
            start += 5
        elif show_data == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def main():
   
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input("\nWould you like to restart? Enter 'yes' or 'no': ").lower()
        if restart != 'yes':
            break

if __name__ == "__main__":
    main()
