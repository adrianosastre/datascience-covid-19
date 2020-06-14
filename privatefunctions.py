def add6ColFile (date, df, main_df) :
    
  nrows = 0
  for index, row in df.iterrows():
    nrows = nrows + 1
    country = row['Country/Region']
    if country == 'Mainland China' :
      country = 'China'

    main_df = main_df.append(
      {
        "Date": date,
        "Country": country,
        "State": row['Province/State'],
        "TotalConfirmed": row['Confirmed'],
        "TotalDeaths": row['Deaths'],
        "TotalRecovered": row['Recovered']
      }
    , ignore_index=True)

    if nrows % 100 == 0 :
      print('.')
    else :
      print('.', end = '')

  print('\n')
  return main_df

def add8ColFile(date, df, main_df) :  

  nrows = 0
  for index, row in df.iterrows():
    
    nrows = nrows + 1
    country = row['Country/Region']
    if country == 'Mainland China' :
      country = 'China'

    main_df = main_df.append(
      {
        "Date": date,
        "Country": country,
        "State": row['Province/State'],
        "TotalConfirmed": row['Confirmed'],
        "TotalDeaths": row['Deaths'],
        "TotalRecovered": row['Recovered'],
        "Latitude": row['Latitude'],
        "Longitude": row['Longitude']
      }
    , ignore_index=True)

    if nrows % 100 == 0 :
      print('.')
    else :
      print('.', end = '')

  print('\n')
  return main_df

def add12ColFile(date, df, main_df) :

  nrows = 0
  for index, row in df.iterrows():

    nrows = nrows + 1
    main_df = main_df.append(
      {
        "Date": date,
        "Country": row['Country_Region'],
        "State": row['Province_State'],
        "City": row['Admin2'],
        "TotalConfirmed": row['Confirmed'],
        "TotalDeaths": row['Deaths'],
        "TotalRecovered": row['Recovered'],
        "Latitude": row['Lat'],
        "Longitude": row['Long_']
      }
    , ignore_index=True)

    if nrows % 100 == 0 :
      print('.')
    else :
      print('.', end = '')

  print('\n')
  return main_df

def add14ColFile(date, df, main_df) :

  nrows = 0
  for index, row in df.iterrows():

    nrows = nrows + 1
    main_df = main_df.append(
        {
          "Date": date,
          "Country": row['Country_Region'],
          "State": row['Province_State'],
          "City": row['Admin2'],
          "TotalConfirmed": row['Confirmed'],
          "TotalDeaths": row['Deaths'],
          "TotalRecovered": row['Recovered'],
          "Latitude": row['Lat'],
          "Longitude": row['Long_'],
          "IncidenceRate": row['Incidence_Rate'],
          "CaseFatalityRatio": row['Case-Fatality_Ratio']
        }
      , ignore_index=True)
    
    if nrows % 100 == 0 :
      print('.')
    else :
      print('.', end = '')

  print('\n')
  return main_df