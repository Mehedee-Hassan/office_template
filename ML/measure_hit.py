def measure(ttdf):
    import pprint as pp
    # expecting @tdf= [['real','pred]]
    measure={'hit_nonzero':0,'miss_nonzero':0,'hit_zero':0,'zero_real':0,'zero_pred':0,'hit_diff_error':0,'miss_diff_error':0}
    hit_diff_error_count= 0
    miss_diff_error_count =0

    for i,r in ttdf.iterrows():
        if r.iloc[0] > 0 and r.iloc[1] > 0:
            # non zero hit
            measure['hit_nonzero'] +=1
            measure['hit_diff_error'] +=abs(r.iloc[0]-r.iloc[1])
            hit_diff_error_count += 1
            
        if (r.iloc[0] > 0 and r.iloc[1] == 0)or (r.iloc[0] == 0 and r.iloc[1] > 0):
            measure['miss_nonzero'] +=1
            measure['miss_diff_error'] +=abs(r.iloc[0]-r.iloc[1])
            miss_diff_error_count += 1

        if r.iloc[0] == 0 and r.iloc[1]== 0:
            measure['hit_zero'] +=1

        if r.iloc[0] == 0:
            measure['zero_real'] +=1
        if r.iloc[1] == 0:
            measure['zero_pred'] +=1

    measure['hit_diff_error'] = measure['hit_diff_error']/hit_diff_error_count
    measure['miss_diff_error'] = measure['miss_diff_error']/miss_diff_error_count
    
    pp.pprint(measure)

    return measure



measure(ttdf)


