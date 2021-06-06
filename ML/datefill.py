prediction_until = "2021-03-31"
dataarray = []

for pid in pid_list:
  # do pid process

    dd = df[df["pid"] == pid]
    start_train = dd.iloc[0]['date']

    

    print("pid = ",str(pid))

    datelist = pd.date_range(start=dd.iloc[0]['date'], end=prediction_until)
    predictdatelist = pd.date_range(start=start_prediction, end=prediction_until)

    dd["date"] = pd.to_datetime(dd["date"])

    dd = dd.set_index('date')

    for a in datelist:
        if str(a.date()) in dd.index:
            
            dataarray.append({'pid':pid,'date': str(a.date()), 'count':int(dd.loc[str(a.date())]['count']) })
                    
        else:
            pass
            dataarray.append({'pid':pid,'date': str(a.date()), 'count': 0})


dd2 = pd.DataFrame(dataarray)
