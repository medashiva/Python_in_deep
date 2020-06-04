import pickle

'''
dump will write your data to file, if you didn't give the file object it will give error
dumps will store the data to variable as string in binary format.
below example for pickle data to file
'''

list1 = [1,2,3]
file_1 = open('./random.txt','wb') # writes to file in binary format
pickle.dump(list1,file_1)
file_1.close()

b = pickle.dumps(list1)
print(b,"string pickle")

'''
below example to unpickle the pickled data
'''

file_2 = open('./random.txt','rb')
a = pickle.load(file_2)
file_2.close()
print(a)
print(pickle.loads(b))
