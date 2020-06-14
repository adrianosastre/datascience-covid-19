def add6ColFile (date, df, main_df) :

  df = df.rename(columns =
    {
      'Last Update' : 'Date',
      'Country/Region' : 'Country',
      'Province/State' : 'State',
      'Confirmed' : 'TotalConfirmed',
      'Deaths' : 'TotalDeaths',
      'Recovered': 'TotalRecovered'
    }
  )

  df['Date'] = date

  main_df = main_df.append(df)
  return main_df

def add8ColFile(date, df, main_df) :

  df = df.rename(columns =
    {
      'Last Update' : 'Date',
      'Country/Region' : 'Country',
      'Province/State' : 'State',
      'Confirmed' : 'TotalConfirmed',
      'Deaths' : 'TotalDeaths',
      'Recovered': 'TotalRecovered'
    }
  )

  df['Date'] = date

  main_df = main_df.append(df)
  return main_df

def add12ColFile(date, df, main_df) :


  df = df.rename(columns =
    {
      'Last_Update' : 'Date',
      'Country_Region' : 'Country',
      'Province_State' : 'State',
      'Admin2' : 'City',
      'Lat' : 'Latitude',
      'Long_' : 'Longitude',
      'Confirmed' : 'TotalConfirmed',
      'Deaths' : 'TotalDeaths',
      'Recovered': 'TotalRecovered',
      'Active': 'TotalActive'
    }
  )

  df['Date'] = date

  df = df.drop(columns=['FIPS', 'Combined_Key'])

  main_df = main_df.append(df)
  return main_df

def add14ColFile(date, df, main_df) :

  df = df.rename(columns =
    {
      'Last_Update' : 'Date',
      'Country_Region' : 'Country',
      'Province_State' : 'State',
      'Admin2' : 'City',
      'Lat' : 'Latitude',
      'Long_' : 'Longitude',
      'Confirmed' : 'TotalConfirmed',
      'Deaths' : 'TotalDeaths',
      'Recovered': 'TotalRecovered',
      'Active': 'TotalActive',
      'Incidence_Rate': 'IncidenceRate',
      'Case-Fatality_Ratio': 'CaseFatalityRatio'
    }
  )

  df['Date'] = date

  df = df.drop(columns=['FIPS', 'Combined_Key'])

  main_df = main_df.append(df)
  return main_df