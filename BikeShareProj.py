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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    days = ['monday', 'tuesday', 'wednesday' , 'thursday', 'friday', 'saturday',  'sunday']
    while(True):

        try:
            city = str(input("Would you like to see data for Chicago, New York City, or Washington? ")).lower()
            if(city in CITY_DATA.keys()):
                break
            else:
                print("Please enter a valid city name.\n")

        except:
           print("Incorrect value, please enter a city name!\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    going = True
    while(going):
        try:
            inp = str(input('Would you like to filter the data by month, day, both, or not at all? Enter "none" for no time filter. ')).lower()
            filt = str(inp)
            if(inp == 'month'):
                while(True):
                    try:
                        month = str(input('Which month? January, February, March, April, May, or June? Please type out the full month name. ')).lower()
                        if(month in months):
                            day = 'all'
                            going = False
                            break

                        else:
                            print_m()

                    except:
                        print_m()
            #parse the input
            elif(inp =='day'):
                while(True):
                    try:
                        day = str(input('Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? Please type out the full day name. ')).lower()
                        if(day in days):
                            month = 'all'
                            going = False
                            break
                        else:
                            print_m()

                    except:
                        print_m()

            elif(inp == 'both'):

                while(True):
                    try:
                        month = str(input('Which month? January, February, March, April, May, or June? Please type out the full month name. ')).lower()
                        if(month in months):
                            day = 'all'
                            break

                        else:
                            print_m()
                    except:
                        print_m()

                while(True):
                    try:
                          day = str(input('Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? Please type out the full day name. ')).lower()
                          if(day in days):

                              month = 'all'
                              going = False
                              break
                          else:
                              print_m()
                    except:
                          print_m()



            elif(inp == 'none'):
                 month = 'all'
                 day = 'all'
                 going = False
        except:
            print("Unexcepted input, please try again...")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day, filt


def print_m():
    print("Please enter valid month.\n\n")

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


def time_stats(df, filt):
    """Displays statistics on the most frequent times of travel."""


    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    print("What is the most common month?")
    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    com_month = int(df['month'].mode()[0])
    count = df[df['month'] == com_month].count()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print("\nMost popular month: " + str(months[com_month - 1]).title() + ". Count: " + str(count) + ", Filter: " + str(filt) + "\n")

    print("\nWhat is the most common day of the week?\n")
    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    com_day = str(df['day_of_week'].mode()[0])
    count =  df[df['day_of_week'] == com_day].count()[0]
    print("\nMost popular day of week: " + str(com_day) + ". Count: " + str(count) + ", Filter: " + str(filt) + "\n\n")


    print("\nWhat is the most common hour?\n")
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    com_hour  = int(df['hour'].mode()[0])
    count =  df[df['hour'] == com_hour].count()[0]
    print("\nMost popular hour: " + str(com_hour) + ". Count: " + str(count) + ", Filter: " + str(filt) + "\n\n")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    m_start = df['Start Station'].mode()[0]
    count = df[df['Start Station'] == m_start].count()[0]
    print("Start Station: {}  , Count:  {}  \n").format(str(m_start), str(count))


    # TO DO: display most commonly used end station
    m_end = df['End Station'].mode()[0]
    count = df[df['End Station'] == m_end].count()[0]
    print("End Station:  {} , Count:  {}  \n").format(str(m_end), str(count))


    # TO DO: display most frequent combination of start station and end station trip
    print("Most popular trip: \n")
    comb = df.groupby(['Start Station', 'End Station']).apply(lambda x: x.mode())
    print("Start Station: {}   \nEnd Station: {} \n").format(str(comb.iloc[0][4]), str(comb.iloc[0][5]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_time = df['Trip Duration'].sum()
    print("Total duration: {} seconds.\n").format(str(tot_time))


    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("Avg Duration: {} seconds.\n").format(str(mean_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, wash):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("\n\nWhat is the breakdown of users?")
    user_types = df['User Type'].value_counts()
    print("Subscribers: " + str(user_types[0]))
    print("Customers: " + str(user_types[1]) + "\n")


    # TO DO: Display counts of gender
    if(wash != True):
        print("\nWhat is the breakdown of gender?")
        gen = df['Gender'].value_counts()
        print("Male: " + str(gen[0]))
        print("Female: " +str(gen[1]) + "\n")

    # TO DO: Display earliest, most recent, and most common year of birth
        print("What are the earliest, most recent, and most common years of birth?\n")
        sort_year = df.sort_values('Birth Year')
        earliest = sort_year['Birth Year'].iloc[0]
        recent = sort_year['Birth Year'].iloc[-1]

        com = df['Birth Year'].mode()[0]
        count = df[df['Birth Year'] == com].count()[0]
        print("Earliest: " + str(earliest) + ", Most recent: " + str(recent) + ", Most common: " + str(com) + ", count: " + str(count) + "\n\n")
    else:
        print("This city has no Gender or Birth Year data to share.\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day, filt = get_filters()
        df = load_data(city, month, day)

        time_stats(df, filt)
        station_stats(df)
        trip_duration_stats(df)
        #check if the city is Washinton
        wash = False
        if(city == 'washington'):
            wash = True

        user_stats(df, wash)
        dr = load_data(city, month, day)

        #set inital variables and prompt for displaying raw data
        start = 0
        end = 5
        while(True):

                raw = str(input("\nWould you like to view the raw data? Type 'yes' or 'no'.\n"))
                if(raw.lower() == 'yes'):
                    print(dr.iloc[start:end])

                elif(raw.lower() == 'no'):
                    break

                else:
                    print("\nPlease enter: 'yes' or 'no'\n")

                start = end
                end = start + 5


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
