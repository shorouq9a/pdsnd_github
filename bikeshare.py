import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which city do you want to analyze, please choose chicago, new york city or washington ?\n").lower()
        if city in ('chicago','new york city','washington'):
            break
        else:
            print("\nPlease write the correct city name!")
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nChoose a month from january TO june, OR write 'all' to see the whole six months?\n").lower()
        if month in ("january", "february", "march", "april", "may", "june", "all"):
            break
        else:
            print("\nSorry, you have to write the name of one of the six months")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nNow choose the day you prefer 'monday, 'tuesday' ... 'sunday' or type 'all' to view all?\n").lower()
        if day in ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"):
            break
        else:
            print("\n!!!, please type a day of the week")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df["Start Time"] = pd.to_datetime(df["Start Time"])

    df["month"] = df["Start Time"].dt.month
    df["weekday"] = df["Start Time"].dt.day_name()

    if month != "all":
        months=["january", "february", "march", "april", "may", "june"]
        month = months.index(month) +1
        df = df[df["month"] == month]


    if day != "all":
        df = df[df["weekday"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most popular month is ", df["month"].mode()[0])

    # display the most common day of week
    print("\nThe most popular day is ", df["weekday"].mode()[0])

    # display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    print("\nThe most popular start hour is ", df["hour"].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most commonly used start station is ", df["Start Station"].mode()[0])

    # display most commonly used end station
    print("\nThe most commonly used end station is ", df["End Station"].mode()[0])

    # display most frequent combination of start station and end station trip
    combination_Station = (df["Start Station"] + ' & ' + df["End Station"]).mode()[0]
    print("\nMost frequent combination of start station and end station trip is:", combination_Station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total travel time is", df["Trip Duration"].sum())

    # display mean travel time
    print("Agerager travel time is", df["Trip Duration"].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Count of user types is: ", df["User Type"].value_counts())

    # Display counts of gender
    if "Gender" in df:
        print("Count of gender is: ", df["Gender"].value_counts())

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        earliest_year = df["Birth Year"].min()
        print("\nThe earliest year of brith is: {}".format(earliest_year))
        most_recent = df["Birth Year"].max()
        print("\nThe most recent year of brith is: {}".format(most_recent))
        most_common = df["Birth Year"].mode()[0]
        print("\nThe most common year of brith is: {}".format(most_common))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# function to display data
def display_raw(df):
    raw = 0
    while True:
        msg = input("\Do you want to display 5 raws of data as well, 'Y' OR 'N'?\n").lower()
        if msg == 'n':
            break
        elif msg == 'y':
            print(df[raw:raw+5])
 # to add 5 rows from the data 
            raw += 5
        else:
            print("\nPlease enter 'y' OR 'n'")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
