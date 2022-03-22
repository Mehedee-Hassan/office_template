df["date2"] = pd.to_datetime(df["date2"]).dt.strftime("%Y%m%d")
