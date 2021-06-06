tarray = np.array([[[[1],[2],[3]]]])
print(type(tarray))
tempyhat = tarray


if type(tarray) == type(np.array([])):
    tempyhat=tarray.tolist()[0]

if len(tempyhat) ==1:
    while len(tempyhat) == 1:
      tempyhat = tempyhat[0]
      
    if type(tempyhat[0])==type([]):
      tt=[]
      for a in tempyhat:
          tt.append(a[0])
      tempyhat=tt
    print(tempyhat)
    if type(tempyhat) == type([]):
        pass
    else:
        temppyhat = yhat.tolist()
