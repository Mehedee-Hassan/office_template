forpie = corr1.groupby(by="C",as_index=False).count()

"""


	C	Unnamed: 0	pid	corr_count_customer	corr_count_shop_customer
0	'-0.5,-1'	0	0	0	0
1	'-0.4,-0.5'	0	0	0	0
2	'-0.3,-0.4'	0	0	0	0
3	'-0.2,-0.3'	0	0	0	0
4	'-0.1,-0.2'	20	20	20	20
5	'-0.0,-0.1'	708	708	708	708
6	'0.0'	2125	2125	2125	2125
7	'0,0.1'	900	900	900	900
8	'0.1,0.2'	209	209	209	209
9	'0.2,0.3'	24	24	24	24
10	'0.3,0.4'	9	9	9	9
11	'0.4,0.5'	5	5	5	5
12	'0.5,0.6'	0	0	0	0
"""


import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = list(forpie['C'].values)
sizes = list(forpie['pid'].values)
explode = (0, 0, 0,0, 1, 0,2, 0, 0,0, 0, 0) 

fig1, ax1 = plt.subplots(figsize=(20,15))
ax1.pie(sizes, 
        #explode=explode, 
        labels=labels,
        #, autopct='%1.1f%%',
        #colors=["orange","blue","lime"],
        shadow=True, startangle=90)
ax1.axis('equal') 
plt.show()



import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = np.array(forpie['C'].values)
size= np.array(forpie['pid'].values)
explode = (0, 0, 0,0, 1, 0,2, 0, 0,0, 0, 0) 

# fig1, ax1 = plt.subplots(figsize=(20,15))
# ax1.pie(sizes, 
#         #explode=explode, 
#         labels=labels,
#         #, autopct='%1.1f%%',
#         #colors=["orange","blue","lime"],
#         shadow=True, startangle=90)
# ax1.axis('equal') 
# plt.show()

porcent = 100.*size/size.sum()
fig1, ax1 = plt.subplots(figsize=(10,15))

patches, texts = ax1.pie(size,  startangle=90, radius=1.2)
labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(labels, porcent)]

sort_legend = True
if sort_legend:
    patches, labels, dummy =  zip(*sorted(zip(patches, labels, size),
                                          key=lambda x: x[2],
                                          reverse=True))

ax1.legend(patches, labels, loc='left center', bbox_to_anchor=(-0.1, 1.),
           fontsize=20)

plt.savefig('piechart.png', bbox_inches='tight')




# result pi graph


import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'NN', 'PI', 'TOKEI'
sizes = [a,b,c]
explode = (0.05, 0.05, 0.05) 

fig1, ax1 = plt.subplots(figsize=(10,15))
ax1.pie(sizes, explode=explode, labels=labels, autopct='%2.1f%%',colors=["orange","blue","lime"],
        shadow=False, startangle=180)
ax1.axis('equal') 
plt.title="BEFORE TEMPO CUSTOMER COUNT"
plt.show()



