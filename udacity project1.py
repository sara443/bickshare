
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


cities=['chicago','new york city','washington']
monthes=['january', 'february', 'march', 'april', 'may', 'june','all']
days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']
def right_input(input_u):
    while True:
        user_input=input(input_u)
        user_input.lower()
        try:
            if user_input in cities:
                break
            elif  user_input in monthes:
                break

            elif user_input in days:
                break
            else:
                if user_input not in cities:
                    print("wrong city")
                if user_input not in monthes:
                    print("wrong month")
                if user_input not in days:
                    print("wrong day")
        except ValueError:
            print("the input is wrong")
    return user_input

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
    city = right_input("Would you like to see the data for chicago, new york city or washington?")
    # get user input for month (all, january, february, ... , june)
    month = right_input("Which Month (all, january, ... june)?")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = right_input("Which day? (all, monday, tuesday, ... sunday)")
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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week, hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print(" popular_month = ",df['month'].mode()[0])


    # display the most common day of week
    print("popular_day_of_week =", df['day_of_week'].mode()[0])



    # display the most common start hour
    print ("popular_common_start_hour =", df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("popular_start_station = ",df['Start Station'].mode()[0])



    # display most commonly used end station
    print("popular_end_station =", df['End Station'].mode()[0])


    # display most frequent combination of start station and end station trip
    print("group_field=",df.groupby(['Start Station','End Station']).size().sort_values(ascending=False).head(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("total_travel_time =", df['Trip Duration'].sum())


    # display mean travel time
    print("mean_travel_time =", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User Type Stats:')
    print(df['User Type'].value_counts())
    if city != 'washington':
        # Display counts of gender

        print("gender counts",df['Gender'].value_counts())
        # Display earliest, most recent, and most common year of birth

        print("most_common_year = ",df['Birth Year'].mode()[0])

        print("most_recent_year = ",df['Birth Year'].max())

        print("earliest_year =", df['Birth Year'].min())

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def raw_data(df):

    the_rows = 5
    start = 0
    end = the_rows - 1    # use index values for rows

    print('\n    Would you like to see some raw data from the current dataset?')
    while True:
        raw_data = input('      (y or n):  ')
        if raw_data.lower() == 'y':
            # display show_rows number of lines, but display to user as starting from row as 1
            # e.g. if rows_start = 0 and rows_end = 4, display to user as "rows 1 to 5"
            print('\n    Displaying rows {} to {}:'.format(start + 1, end + 1))

            print('\n', df.iloc[start : end + 1])
            start += the_rows
            end += the_rows


            print('\n    Would you like to see the next {} rows?'.format(the_rows))
            continue
        else:
            break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
