#coding:utf-8
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins+'.'+secs)

def read_coach(file):
    try:
        with open(file) as f:
            data = f.readline()
        data = data.strip().split(',')
        dic = {}
        dic['Name'] = data.pop(0)
        dic['Birth'] = data.pop(0)
        dic['times'] = sorted(set([sanitize(t) for t in data]))[0:3]
        return dic
    except IOError as err:
        print('open file err: '+str(err))
        return(None)

james = read_coach('james.txt')
julie = read_coach('julie.txt')
mikey = read_coach('micky.txt')
sarah = read_coach('sarah.txt')

print(james,julie,mikey,sarah)
































    
    
