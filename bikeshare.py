import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



def display_data(df):
    show_data = "yes"
    counter = 0
    while show_data == "yes" or counter >= len(df):
        print(df[counter:counter+5])
        counter += 5
        show_data = input('\nWould you like to see more rows of this data? Enter yes or no.\n')
        show_data = show_data.lower()

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
        try:
            city = ""
            cities = ['chicago' , 'new york city' , 'washington']
            while not city in cities:
                city = input("Would you like to see data for Chicago, New York city, or Washington: ")
                if not city in cities:
                    print("Please! Enter one of the given words (Chicago, New York City, or Washington)")
                city = city.lower()
            break
        except Exception as e:
            print("Exception occurred: {}".format(e))



    month = "all"
    day = "all"
    available_filters = ['month', 'day', 'both', 'none']
    specified_filter = ''
    while not specified_filter in available_filters:
        specified_filter = input('Would you like to filter the data by month, day, both, or not at all? Type "none" for no time filter: ').lower()
        if not specified_filter in available_filters:
            print("Please! Enter one of the given options")

    if specified_filter == "none":
        month = "all"
        day = "all"

    elif specified_filter == "month":
        # get user input for month (all, january, february, ... , june)
        while True:
            try:
                month = ""
                months = ['january', 'february', 'march', 'april', 'may', 'june']
                while not month in months:
                    month = input("Which month? January, February, March, April, May, OR June? Please type out the full month name: ")
                    if not month.lower() in months:
                        print("Please! Enter the name of the months from the given months ONLY")
                    month = month.lower()
                break
            except Exception as e:
                print("Exception occurred: {}".format(e))
    elif specified_filter == "day":
        #specific_day = {'M': "Monday" , 'Tu': "Tuesday", 'W': "Wednesday", 'Th': "Thursday", 'F': "Friday", 'Sa': "Satuarday", 'Su': "Sunday"}
        while True:
            try:
                temp_day = ""
                days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'satuarday', 'sunday']
                while not temp_day in days:
                    temp_day = input("Which day? Please type a day Monday, Tuesday, Wednesday, Thursday, Friday, Satuarday, Sunday: ").lower()
                    if not temp_day in days:
                        print("Please! Enter one of the given days")
                day = days.index(temp_day)
                break
            except Exception as e:
                print("Exception occurred: {}".format(e))
    else: #both
        # get user input for month (all, january, february, ... , june)
        while True:
            try:
                month = ""
                months = ['january', 'february', 'march', 'april', 'may', 'june']
                while not month in months:
                    month = input("Which month? January, February, March, April, May, OR June? Please type out the full month name: ")
                    if not month.lower() in months:
                        print("Please! Enter the name of the months from the given months ONLY")
                    month = month.lower()
                break
            except Exception as e:
                print("Exception occurred: {}".format(e))

        # get user input for day of week (all, monday, tuesday, ... sunday)
        while True:
            try:
                temp_day = ""
                days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'satuarday', 'sunday']
                while not temp_day in days:
                    temp_day = input("Which day? Please type a day Monday, Tuesday, Wednesday, Thursday, Friday, Satuarday, Sunday: ").lower()
                    if not temp_day in days:
                        print("Please! Enter one of the given days")
                day = days.index(temp_day)
                break
            except Exception as e:
                print("Exception occurred: {}".format(e))



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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])


    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_of_week

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = month.lower()
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'satuarday', 'sunday']
        day = day.lower()
        day = days.index(day)
        df = df[df['day_of_week'] == day]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    all_months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June'}
    print("The most common month {}".format(all_months[df['month'].mode()[0]]))

    # display the most common day of week
    all_days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Satuarday', 6: 'Sunday'}
    print("The most common day of week {}".format(all_days[df['day_of_week'].mode()[0]]))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("Most popular Start Station: ", df['Start Station'].mode()[0])

    # display most commonly used end station
    print("Most popular End Station: ", df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    print("These are the most popular Start & End Station respectively: ({} {})".format(df['Start Station'].mode()[0] , df['End Station'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Totatl travel time = ", df['Trip Duration'].sum())

    # display mean travel time
    print("Mean of travel time = ", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Counts of user types: ", df['User Type'].value_counts())

    # Display counts of gender
    if 'Gender' in df:
        print("Counts of gender: ", df['Gender'].value_counts())
    else:
        print("No gender data to share")


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print("Below are the earliest, most recent, and most common year of birth respectively")
        print("{} , {} , {} ".format(df['Birth Year'].min() , df['Birth Year'].max() , df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        answer = ''
        available_answers = ['yes', 'no']
        while not answer in available_answers:
            answer = input("Do you want to see 5 rows of data? ").lower()
            if not answer in available_answers:
                print("Please! Enter a valid answer")
            else:
                if answer == 'no':
                    break
                display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
