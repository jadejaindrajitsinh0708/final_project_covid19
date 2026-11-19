import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 

print("1. Load CSV File ")
try:
    data_input =input("Enter CSV File Name :")
    if data_input == ('covid19.csv'):
        data=pd.read_csv(data_input)
        data['Last_Update'] = pd.to_datetime(data['Last_Update'])
        print('File Loaded Successfully')
        menu="""
1.EXPLORE DATASET 
2.CLEAN DATASET
3.DATA ANALYSIS  
4.DATA VISIALIZATION 
5.ANALYSIS RESULTS    """ 

        
        print(menu)
        choice=int(input("Enter Your Choice :"))

        if choice == 1 :
              menu1="""
*********EXPLORE DATASET*********
1. Display First 5 Rows
2. Display Last 5 Rows
3. Display Column Names
4. Display Data Types
5. Display Dataset Information
6. Display Statistical Summary
        """
              print(menu1)

              choice= int(input('Enter Your Choice :'))
              if choice == 1 :
                  
                  print(data.head(5))
              elif choice == 2:
                  print(data.tail(5))

              elif choice == 3 :
                  print(data.columns)
              elif choice == 4 :
                  print(data.dtypes)
              elif choice == 5:
                  data.info()
              elif choice == 6 :
                  print(data.describe())
              else :
                  print("ENVALID CHOICE!!   ")


        elif choice == 2 :
            menu2=""" 
            1. Check Missing Values
            2. Handle Missing Values
            3. Remove Duplicate Rows       
            4. Check Invalid Values
        """
            print(menu2)
            choice=int(input('Enter Your Choice :'))
            if choice == 1:
                print(data.isnull().sum())

            if choice ==2:

                print("1. Remove Missing Values") 
                print('2. Fill Missing Values')
                choice=int(input("Enter Your Choice :"))

                if choice == 1 :
                    datad=data.dropna()
                    print(datad)
                    print("Missing Values Removed Successfully")
                elif choice == 2:
                    value = float(input("Enter Value to Fill Missing Values: "))
                    datad=data.fillna(value)
                    print(datad)
                    print(f"Missing Values Filled With {value} Successfully")   

                    # print(datad.info())
                else :
                    print("ENTER VALID CHOICE !!")
                        
            elif choice == 3:
                print("1. show the duplicates row :")
                print("2. remove the Duplicates row :")

                choice=int(input("Enter your choice :"))
                if choice == 1 :
                    data.duplicated().sum()
                    print(data)
                elif choice ==2 :
                    data.drop_duplicates(inplace=True)
                    print(data)
                    print("row remove succssesfully ")
                    print(data.duplicated().sum())
                else:
                    print('INVALID INPUT !!')



            elif choice ==4:
                print(data[data['Deaths'] < 0])
                print(data[data['Recovered'] < 0])
                print(data[data['Confirmed'] < 0])

        elif choice == 3:
            print('*****DATA ANALYSIS******')
            menu3="""
        1	Total Confirmed Cases
        2	Total Deaths
        3	Total Recovered
        4	Total Active Cases
        5	Maximum & Minimum Cases
        6	Average Cases
        7	Country-wise Cases
        8	Country-wise Deaths
        9	Top 10 Countries


""" 
            print(menu3)

            choice=int(input("Enter your select number :"))
            if choice ==1:
                total_confirmed = data["Confirmed"].sum()
                print('total_confirmed',total_confirmed)
            elif choice ==  2:
                total_deaths = data['Deaths'].sum()
                print("total_deaths",total_deaths)
            elif choice == 3: 
                total_Recovered = data["Recovered"].sum() 
                print("Total Recovered",total_Recovered)

            elif choice == 4:
                Total_Active_Cases = data['Active'].sum()
                print("Total Active Cases",Total_Active_Cases)

            elif choice == 5 :
                Maximum_Minimum_Cases = data['Confirmed'].max()
                print("MAXIMUM CASES ",Maximum_Minimum_Cases)

                Minimum = data["Confirmed"].min()
                print("MINIMUM CASES ",Minimum)



            elif choice == 6 :
                Average = data['Confirmed'].mean()
                print("Average Cases",Average)

            elif choice == 7 :
                Country_wise_Cases= data.groupby("Country_Region")['Confirmed'].sum().reset_index()
                print("COUNTRY WISE CASES ")
                print(Country_wise_Cases)

            elif choice == 8 :
                Country_wise_Deaths = data.groupby("Country_Region")['Deaths'].sum().reset_index()
                print("COUNTRY WISE DEATHS")
                print(Country_wise_Deaths)

            elif choice == 9 :
                top_10 = data.groupby('Country_Region')['Confirmed'].sum().nlargest(10)
                print(top_10)
        elif choice == 4  :
            print("DATA VISIALIZATION ")
            menu4 ="""
            1. Bar chart
            2. Pie chart
            3. line chart
            4. Scatter Plot
            5. Histogram  """     
            print(menu4)
            choice = int(input(" Enter your select Chart number :"))

            if choice == 1 :

                print("***** BAR CHART *****")
                print("Top 10 Countries with Highest Confirmed Cases")
                top_10 = data.groupby('Country_Region')['Confirmed'].sum().nlargest(10)
                top_10.plot(kind='bar', figsize=(10,5), color='skyblue')
                plt.title("Top 10 Countries - Confirmed Cases")
                plt.xlabel("Country")
                plt.ylabel("Confirmed Cases")
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.legend( bbox_to_anchor=(1,1))
                plt.show()

            elif choice == 2:

                print("***** PIE CHART *****")
                print("COVID-19 Cases Distribution")

                total = data[['Deaths', 'Recovered', 'Active']].sum()

                total.plot(kind='pie',
                            autopct='%1.1f%%',
                              figsize=(7,7))

                plt.title("COVID-19 Cases Distribution")
                plt.ylabel("")
                plt.show()

            elif choice == 3:
                print("***** LINE CHART *****")
                print("COVID-19 Confirmed Cases Trend Over Time")
                trend = data.groupby('Last_Update')['Confirmed'].sum()
                trend.plot(kind='line',
                            marker='o',
                              figsize=(10,5))
                plt.title("COVID-19 Confirmed Cases Trend")
                plt.xlabel("Date")
                plt.ylabel("Confirmed Cases")
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()

            elif choice == 4 :
                print("***** SCATTER PLOT *****")
                print("Confirmed vs Recovered Cases")
                top_5 = data.groupby('Country_Region')['Confirmed'].sum().nlargest(4).index
                new_data = data[data['Country_Region'].isin(top_5)]
                plt.figure(figsize=(10, 6))
                sns.scatterplot(
                    data=new_data,
                    x='Confirmed',
                    y='Recovered',
                    hue='Country_Region',
                    s=100
                )
                plt.title("Confirmed vs Recovered Cases")
                plt.xlabel("Confirmed Cases")
                plt.ylabel("Recovered Cases")
                plt.legend(title="Country Name")
                plt.tight_layout()
                plt.show()

            elif choice == 5 :
                print("***** HISTOGRAM *****")
                print("Confirmed Cases Distribution")
                plt.hist(data['Confirmed'],
                          bins=20, color='skyblue',
                            edgecolor='black')
                plt.title("Confirmed Cases Distribution")
                plt.xlabel("Confirmed Cases")
                plt.ylabel("Number of Countries")
                plt.show()

            else :
                print("INVALID CHOICE !!!")

        elif choice == 5:


            print("***** ANALYSIS RESULTS *****")

            print("Total Confirmed Cases:", data['Confirmed'].sum())

            print("Total Deaths:", data['Deaths'].sum())

            print("Total Recovered:", data['Recovered'].sum())

            print("Total Active Cases:", data['Active'].sum())

            print("Maximum Confirmed Cases:", data['Confirmed'].max())

            print("Minimum Confirmed Cases:", data['Confirmed'].min())

            print("Average Confirmed Cases:", data['Confirmed'].mean())

            print("Total Countries:", data['Country_Region'].nunique())

        else :
            print(" !!!INVALID CHOICE PLEASE ENTER CORRECT CHOICE !!! ")
    else :

        print("!! WRONG FILE NAME PLEASE ENTER CORRECT CSV FILE NAME  !!")

except:
    print(' !!❌ INVALID INPUT PLEASE ENTER CORRECT INPUT ❌!!')