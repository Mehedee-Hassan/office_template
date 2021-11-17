"""
df = pd.DataFrame({'foo': ['one', 'one2', 'one2', 'two', 'two',
                           'two'],
                   'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'baz': [1, 2, 3, 4, 5, 6],
                   'zoo': ['x', 'y', 'z', 'q', 'w', 't']})
df



foo	bar	baz	zoo
0	one	A	1	x
1	one2	B	2	y
2	one2	C	3	z
3	two	A	4	q
4	two	B	5	w
5	two	C	6	t

df.pivot(index='foo', columns='bar', values='baz')


bar	A	B	C
foo			
one	1.0	NaN	NaN
one2	NaN	2.0	3.0
two	4.0	5.0	6.0

## similar index value error

   foo bar  baz
0  one   A    1
1  one   A    2
2  two   B    3
3  two   C    4

df.pivot(index='foo', columns='bar', values='baz')
Traceback (most recent call last):
   ...
ValueError: Index contains duplicate entries, cannot reshape

"""




df3.pivot(index=['store','item'] ,columns='date', values='sales')



"""

	date	2014-08-08	2014-08-09	2014-08-10	2014-08-11	2014-08-12	2014-08-13	
store	item																																																																																	
1	4548779700241	NaN	NaN	NaN	NaN	NaN	NaN	NaN	

"""
