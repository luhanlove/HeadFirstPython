#coding:utf-8
from nester import print_lol
import pickle
def fileio(filename):
    K = []
    M = []
    P = []
    try:
        data = open(filename)
        for each_line in data:
            try:
                (role,line) = each_line.split(":",1)
                #print(role,end=' ')
                #注意一个细节问题：我们读取行时，换行符是一并被读取的，所以print需要加''，如果直接print的话，解释器会自动再换一次行。
                #print(line,end='')
                role = role.strip()
                line = line.strip()
                if role == 'K':
                    print(role)
                    K.append(line)
                elif role == 'P':
                    print(role)
                    P.append(line)
                elif role =='M':
                    print(role)
                    M.append(line)
                else:
                    pass
            except ValueError:
                pass
        data.close()
    except IOError:
        print("The file is not exist.")
    try:
        with open('kdata.txt','wb') as kdata:
            pickle.dump(K,kdata)
        with open('mdata.txt','wb') as mdata:
            pickle.dump(M,mdata)
        with open('pdata.txt','wb') as pdata:
            pickle.dump(P,pdata)
            
    except IOError as err:
        print('File error: '+str(err))
    except pickle.PickleError as perr:
        print('Pickling error: '+str(perr))

                
    
