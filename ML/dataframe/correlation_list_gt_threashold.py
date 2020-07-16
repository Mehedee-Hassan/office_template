
len(df.index)

df.head()
df.columns

df.corr('pearson')

df_product_sale.iloc[:,2:].values

df.head()
df_product_sale = df.copy()


df.columns


listofindex =dict(df.corr('pearson')['count'])
listofindexto_consider =[]
for key,val in listofindex.items():
    print(key,val)
    
    if val > 0.1:
        listofindexto_consider.append(str(key))
        
listofindexto_consider = [i for a in listofindexto_consider ]
print(listofindexto_consider)
