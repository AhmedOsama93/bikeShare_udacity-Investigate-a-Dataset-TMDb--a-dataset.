#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import time
import pandas as pd
import numpy as np


months=['january', 'february' ,'march','aprile','may', 'june']

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']


def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('Would you like to see data for chicago, New York, or Washington?')
    city=input()
    while(city.lower() not in ['chicago', 'new york' , 'washington']):
        print('invalid input, Would you like to see data for chicago, New York, or Washington?')
        print('If you want to exit Enter exit')
        city=input()
        if city == 'exit':
              return 0
    
    
    # get user input for month (all, january, february, ... , june)
    print('Would you like to filter the data by month, day, both?')
    choose=input()
    while(choose.lower() not in ['month', 'day' , 'both']):
        print('invalid input, Would you like to filter the data by month, day, both?')
        print('If you want to exit Enter exit')
        choose=input()
        if choose == 'exit':
              return 0
            
            
    if choose == 'both':
            print('which month? all, January, February, March, Aprile, May, June?')
            month = input()
            while(month.lower() not in months):
                print('which month? all, January, February, March, Aprile, May, June?')
                print('If you want to exit Enter exit')
                month = input()
                if month == 'exit':
                           return 0
            
            print('which day? Please type your day name( sunday, monday, tuesday)')
            day = input()
            while(day.lower() not in days ):
                print('which day? Please type your day name( sunday, monday, tuesday)')
                print('If you want to exit Enter exit')
                day = input()
                if day == 'exit':
                    return 0

    elif choose == 'month':
        day='all'
        print('which month? all, January, February, March, Aprile, May, June?')
        month = input()
        while(month.lower() not in months):
                print('which month? all, January, February, March, Aprile, May, June?')
                print('If you want to exit Enter exit')
                month = input()
                if month == 'exit':
                        return 0
              
                        
    elif choose == 'day':
            month='all'
            print('which day? Please type your day name( sunday, monday, tuesdays)')
            day = input()
            while(day.lower() not in days ):
                print('which day? Please type your day name( sunday, monday, tuesday)')
                print('If you want to exit Enter exit')
                day = input()
                if day == 'exit':
                    return 0              
    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    month=month.lower()
    day=day.lower()
    city=city.lower()
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
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
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
     # display the most common month
    # extract month from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    countOfMostCommonMonth=df['month'].value_counts().max()
    mostCommonMonth=df['month'].mode()[0]
    print('MONTH')
    print('The most common Month          :   ',mostCommonMonth) 
    print('The count of most common Month :   ',countOfMostCommonMonth)
    print('------------------------------******************************************************************************')

    #------------------------------******************************************************************************
    # display the most common day of week
    # extract day from week from Start Time to create new columns
    df['day'] = df['Start Time'].dt.day_name()
    countOfMostCommonDay=df['day'].value_counts().max()
    mostCommonDay=df['day'].mode()[0]
    print('DAY')
    print('The most common Day            :   ',mostCommonDay)
    print('The count of most common Day   :   ',countOfMostCommonDay)
    print('------------------------------******************************************************************************')
    #------------------------------******************************************************************************
    #------------------------------******************************************************************************

    # display the most common start hour
    # extract hour from day from Start Time to create new columns
    df['hour'] = df['Start Time'].dt.hour
    countOfMostCommonHour=df['hour'].value_counts().max()
    mostCommonHour=df['hour'].mode()[0]
    print('HOUR')
    print('The most common Hour           :   ',mostCommonHour)
    print('The count of most common Hour  :   ',countOfMostCommonHour)
    print('------------------------------******************************************************************************')

    #------------------------------******************************************************************************
    #------------------------------******************************************************************************
    #------------------------------******************************************************************************
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    countOfMostCommonStartStation=df['Start Station'].value_counts().max()
    mostCommonStartStation=df['Start Station'].mode()[0]
    print("Most Start Station : ",mostCommonStartStation)
    print("count Start Station: ",countOfMostCommonStartStation)
    print('------------------------------******************************************************************************')

    # display most commonly used end station
    countOfMostCommonEndStation=df['End Station'].value_counts().max()
    mostCommonEndStation=df['End Station'].mode()[0]
    print("Most End Station   : ",mostCommonEndStation)
    print("count End Station  : ",countOfMostCommonEndStation)
    print('------------------------------******************************************************************************')

    # display most frequent combination of start station and end station trip

    mostCommonCombination=df[['Start Station','End Station']].mode().loc[0]
    countOfMostCommonCombination=df[['Start Station','End Station']].value_counts().max()
    print("Start Station      :  "+mostCommonCombination[0])
    print("End Station        :  "+mostCommonCombination[1])
    print(countOfMostCommonCombination)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    totalTravelTime=df['Trip Duration'].sum()
    print('total travel time :  ',totalTravelTime)

    # display mean travel time
    meanTravelTime=df['Trip Duration'].mean()
    print('mean travel time  :  ',meanTravelTime)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # Display counts of user types
    countsOfUserTypes=df['User Type'].value_counts()
    print(countsOfUserTypes)
    
    # Display counts of gender
    if city.lower() == 'washington':
        print('Washington don not have gender')
    else:
        countsOfGender=df['Gender'].value_counts()
        print(countsOfGender)
        # Display earliest, most recent, and most common year of birth
        birthYear=df['Birth Year']
        earliestYear=int(birthYear.min())
        print('the earliest birth year       : ', earliestYear)
        recentYear=int(birthYear.max())
        print('recent birth year             : ', recentYear)
        mostCommonBirthYear=int(birthYear.mode()[0])
        print('the most common year of birth : ', mostCommonBirthYear)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

main()





# In[ ]:




