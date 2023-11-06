# Write a Python program to store and read Python object data using pickle module
import pickle
def storeData():
    Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak','age' : 21, 'pay' : 40000}
    Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak','age' : 50, 'pay' : 50000}
    db = {}
    db['Omkar'] = Omkar
    db['Jagdish'] = Jagdish
    dbfile = open('file.dat', 'ab')
    pickle.dump(db, dbfile)
    dbfile.close()
def loadData():
    dbfile = open('file.dat', 'rb')
    db = pickle.load(dbfile)
    for keys in db:
        print(keys, '=>', db[keys])
    dbfile.close()
storeData()
loadData()
