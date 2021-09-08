# check if first and last day difference is equal to the total

for pid in newpidlist:
    count = len(df3[df3['pid'] == pid])
    # print(str(tempdf3[tempdf3['pid'] == pid]['first_date'].dt.strftime('%Y-%m-%d').values[0] ))
    # print(str(tempdf3[tempdf3['pid'] == pid]['last_date'].dt.strftime('%Y-%m-%d').values[0] ))
    # print(pid)
    count2 = len(pd.date_range(str(tempdf3[tempdf3['pid'] == pid]['first_date'].dt.strftime('%Y-%m-%d').values[0] )  ,str(tempdf3[tempdf3['pid'] == pid]['last_date'].dt.strftime('%Y-%m-%d').values[0] )))

    
    if count != count2:
        print('false',pid)
