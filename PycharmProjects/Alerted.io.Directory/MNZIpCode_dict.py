import pickle

l = [i for i in range(55001, 56763,1)]

with open ("zipcodes.txt", "wb") as fp:
    pickle.dump(l, fp)

with open("zipcodes.txt", 'rb') as fp:
    b = pickle.load(fp)

print(b)
