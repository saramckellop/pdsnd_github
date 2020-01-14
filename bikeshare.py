import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze, if invalid information is input an error message is displayed.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    city = input('What city would you like to explore first? \nPlease enter Chicago, New York City or Washington.: ').lower()
    try:
        while city == ('chicago', 'new york city', 'washington'):
            print('Okay\,\ {} it is!'.format.city.title())
    except:
        print('That\'s not a valid city, please try again.')

    month = input('What month would you like to analyze?: ').lower()
    try:
        while month == ('january', 'february', 'march', 'april', 'may', 'june'):
            print('Let\'s look at {}.'.format.month.title())
        if month == ('all'):
            print('We can look at them all!')
    except:
        print('That is an invalid input.')

    day = input('What day would you like to investigate?: ').lower()
    try:
        while day == ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print( 'Let\'s review {}.'.format.day.title())
        if day == ('all'):
            print('We can investigate them all!')
    except:
        print('That is not a valid day, please try again.')

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

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel; including
       the most popular start month by index number,
       the most popular start day of the week and
       the most popular start hour.
       """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    df['Start Date'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('{} is the most popular Start Month.'.format(popular_month))


    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day'] = df['Start Time'].dt.day
    popular_day = df['day'].mode()
    print('{} is the most popular Start Day.'.format(popular_day))


    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()
    print('{} is the most popular Start Hour.'.format(popular_day))

    print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip
       by delineating the most commonly used start station,
       the most commonly used end station and the most
       frequent combination of start and end station trips.
       """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    start_stations = df['Start Station'].mode()[0]
    print('The count of the most commonly used Start Station is:',start_stations)


    end_stations = df['End Station'].mode()[0]
    print('The count of the most commonly used End Station is:',end_stations)


    most_frequent_combo = df[['Start Station', 'End Station']].mode().loc[0]
    print('The most frequent combination of start and end stations is: {} & {}.'.format(most_frequent_combo[0], most_frequent_combo[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    total_travel_time = df['Trip Duration'].sum()
    print(total_travel_time)

    mean_travel_time = df['Trip Duration'].mean()
    print(mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users categorized by
       user type, gender and birth year where applicable.
       """

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    user_types = df['User Type'].value_counts()
    print(user_types)

    if 'Gender' in df.columns:
        gender_types = df['Gender'].value_counts()
        print(gender_types)
    else:
        print('Gender column does not exist for this city.')


    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        print('Earliest birth year recorded:', earliest_birth_year)
    else:
        print('Birth Year column does not exist for this city.')


    if 'Birth Year' in df.columns:
        most_recent_birth_year = df['Birth Year'].max()
        print('Most recent birth year recorded:', most_recent_birth_year)
    else:
        print('Birth Year column does not exist for this city.')


    if 'Birth Year' in df.columns:
        most_common_birth_year = df['Birth Year'].mean()
        print('Most common birth year recorded:', most_common_birth_year)
    else:
        print('Birth Year column does not exist for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)


def display_data(df):
    """ Allows the user to choose to see more data in groups of 5 rows.
    """

    raw_data = input('Would you like to analyze 5 more rows of data? \nType yes or no.').lower()
    index1 = 0
    index2 = 5

    while True:
        if raw_data == 'yes':
            print(df[df.columns[0: ]].iloc[index1:index2])
            index1 += 5
            index2 += 5
            more_columns = input('Would like like to analyze 5 more rows?').lower()
            if more_columns not in ('yes', 'y'):
                break
        else:
            break


def main():
    """ Allows the user to choose to restart the project or to end the project.
    """

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
           break


if __name__ == "__main__":
	main()
