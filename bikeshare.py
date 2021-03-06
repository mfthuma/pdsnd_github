import time
import pandas as pd
import numpy as np
#This file is actually the template file; I submitted the code through the terminal in that project.
#I figure this template is fine for this git project anyway :-)

#This reads in the three data files
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in ('chicago', 'new york city', 'washington'):
        try:
            city = str(input('Enter the city you want to explore (Chicago, New York City, or Washington): ')).lower()
        except:
            print('\n')
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ''
    while month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
        try:
            month = str(input('Enter a month to filter by a single month (January, February, March, April, May, June), or \'None\': ')).lower()
            if month == 'none': month = 'all'
        except:
            print('\n')
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
        try:
            day = str(input('Enter a weekday name to filter by day (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday), or \'None\': ')).lower()
            if day == 'none': day = 'all'
        except:
            print('\n')
            break

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
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['Month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['Day of Week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # use the index of the months list to get the corresponding name
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    popular_month = df['Month'].mode()[0]
    popular_month_name = months[popular_month - 1]
    print('The most common month: {} ({})'.format(popular_month, popular_month_name))

    # TO DO: display the most common day of week
    popular_weekday = df['Day of Week'].mode()[0]
    print('The most common day of the week: ', popular_weekday)

    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    popular_hour = df['Hour'].mode()[0]
    print('The most common start hour: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        #df = load_data(city, month, day)

        #time_stats(df)
        #station_stats(df)
        #trip_duration_stats(df)
        #user_stats(df)

        #restart = input('\nWould you like to restart? Enter yes or no.\n')
        #if restart.lower() != 'yes':
        #    break


if __name__ == "__main__":
	main()
