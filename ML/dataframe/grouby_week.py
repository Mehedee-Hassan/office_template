ddtemp['date2'] = pd.to_datetime(ddtemp['date'])
ddtemp = ddtemp.drop('date',axis=1)

ddtemp.groupby(['date', pd.Grouper(key='date2', freq='W-MON')])['count'].sum().reset_index().sort_values('date')
weekly =dd.groupby(pd.Grouper(key='date',freq='W-Mon')).sum()
weekly.plot()
