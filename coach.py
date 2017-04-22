#coding:utf-8
def read_coach(file):
    try:
        with open(file) as f:
            data = f.readline()
        return data.strip().split(',')
    except IOError as err:
        print('open file err: '+str(err))
        return(None)

james = read_coach('james.txt')
julie = read_coach('julie.txt')
mikey = read_coach('micky.txt')
sarah = read_coach('sarah.txt')

print(james,julie,mikey,sarah)

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins+'.'+secs)

(james_name,james_birth) = james.pop(0),james.pop(0)
(julie_name,julie_birth) = julie.pop(0),julie.pop(0)
(mikey_name,mikey_birth) = mikey.pop(0),mikey.pop(0)
(sarah_name,sarah_birth) = sarah.pop(0),sarah.pop(0)
print(james_name, james_birth)

print(sorted([sanitize(t) for t in james]))
print(sorted([sanitize(t) for t in julie]))
print(sorted([sanitize(t) for t in mikey]))
print(sorted([sanitize(t) for t in sarah]))

#使用set集合
print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])






























    
    
