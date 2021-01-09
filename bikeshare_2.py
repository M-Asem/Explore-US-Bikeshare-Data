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
        try:
            city = input('To view the available bikeshare data, type one of the following cities: chicago, new york city, washington: ').lower()
            if city in {'chicago','new york city','washington'}:
                break #To break the loop#
        except KeyboardInterrupt:
            print('\nNO Input Taken!')
        else:
            print('That\'s invalid input.')
        
                
    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('To view the available bikeshare data, type:\n The month name or (all) for all the months included: ').lower()
            if month in {'january','february','march', 'april', 'may', 'june', 'all'}:
                break#To break the loop#
        except KeyboardInterrupt:
            print('\nNO Input Taken!')
        else:
            print('That\'s invalid input.')


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('To view the available bikeshare data, type:\n The day name or (all) for all the days included: ').lower()
            if day in {'monday','tuesday','wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'}:
                break#To break the loop#
        except KeyboardInterrupt:
            print('\nNO Input Taken!')
        else:
            print('That\'s invalid input.')

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
    
    df = pd.read_csv(CITY_DATA[city])#To read from CSV sheets#

    #Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    #Filter by month if applicable
    if month != 'all':
        #Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        #Filter by month to create the new dataframe
        df = df[df['month'] == month]

    #Filter by day of week if applicable
    if day != 'all':
        #Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
 
    print('\nFILTER SECTION:\nCity: {}\nMonth: {}\n Day: {}'.format(city, month, day))

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Args: Data Frame
    return: time statistics"""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['month'] = df['Start Time'].dt.month
    print('popular month: ', df['month'].mode()[0])

    # display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday
    popular_day = df['day_of_week'].mode()[0]
    print('popular day: ', popular_day)
    
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('popular hour: ', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args: Data Frame
    return: stations statistics"""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode().to_string(index = False)
    print('most commonly used start station: ', start_station)

    # display most commonly used end station
    end_station = df['End Station'].mode().to_string(index = False)
    print('most commonly used end station: ', end_station)

    # display most frequent combination of start station and end station trip
    df['rout'] = df['Start Station'] + "-" + df['End Station']
    print('most commonly used frequent combination : ', df['rout'].mode())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args: Data frame
    return: trip duration statistics"""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df["Start Time"] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ', total_travel_time)

    # display mean travel time
    mean_travel_time = round(df['Trip Duration'].mean())
    print('Mean travel time: ', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users.
    Args: Data frame
    return: Users' statistics"""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print('User types are: ', user_type)

    # Display counts of gender
    try:
        user_gender = df['Gender'].value_counts()
        print('User genders are: ', user_gender)
    except KeyError:
        print('No gender existed')
        

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        print('Earliest year of birth: ', earliest_year)
    except KeyError:
        print('No gender existed')
    
    try:
        recent_year = df['Birth Year'].max()
        print('Most recent year of birth: ', recent_year)
    except KeyError:
        print('No gender existed')
    
    try:
        common_year = df['Birth Year'].mode()
        print('Most common year of birth: ', common_year)
    except KeyError:
        print('No gender existed')
    
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def display_raw_data(city):
    ''' Display 5 lines of raw data upon request
    
    Args: Data frame
    
    Returns: none '''
    
    print('To check raw data..... \n')
    display_raw = input('\n Would you like to see the raw data? Enter yes or no.\n')
    while display_raw == 'yes':
        try:
            for chunk in pd.read_csv(CITY_DATA[city],chunksize=5):
                print(chunk)
                display_raw = input('\nWould you like to see another 5 rows of the raw data? Enter yes or no.\n')
                if display_raw != 'yes':
                    print('Thank You')
                    break #breaking out of the for loop#
            break#breaking out of the for loop#
        except KeyboardInterrupt:
            print('Proceeding')
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        
        display_raw_data(city)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()