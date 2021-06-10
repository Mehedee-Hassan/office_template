seq[0] = np.array(seq[0])
seq[1] = np.array(seq[1])
seq[2] = np.array(seq[2])
seq[3] =np.array(seq[3])


seq[0] = np.reshape(seq[0],(seq[0].shape[0],1))
seq[1] = np.reshape(seq[1],(seq[1].shape[0],1))
seq[2] = np.reshape(seq[2],(seq[2].shape[0],1))
seq[3] = np.reshape(seq[3],(seq[3].shape[0],1))

seq[0]= np.insert(seq[0], [1], np.array(list(oh["pid_4901033630034"])), axis=1)
seq[1]= np.insert(seq[1], [1], np.array(list(oh["pid_4908837324190"])), axis=1)
seq[2]= np.insert(seq[2], [1], np.array(list(oh["pid_4901033630904"])), axis=1)
seq[3]= np.insert(seq[3], [1], np.array(list(oh["pid_4901033630034"])), axis=1)
