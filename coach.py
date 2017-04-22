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

class Athlete:
    def __init__(self,a_name,a_dob=None,a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
    def top3(self):
        return sorted(set([sanitize(t) for t in self.times]))[0:3]
    def add_time(self,item):
        self.times.append(item)
    def add_times(self,l):
        self.times.extend(l)


class AthleteList(list):
    def __init__(self,a_name,a_dob=None,a_time=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_time)
    def top3(self):
        return (sorted(set([sanitize(t) for t in self]))[0:3])

def read_coach(file):
    try:
        with open(file) as f:
            data = f.readline()
        data = data.strip().split(',')
        return Athlete(data.pop(0),data.pop(0),data)
    
    except IOError as err:
        print('open file err: '+str(err))
        return(None)

james = read_coach('james.txt')
julie = read_coach('julie.txt')
mikey = read_coach('micky.txt')
sarah = read_coach('sarah.txt')

print(james,julie,mikey,sarah)

james.add_time('2.23')
print(james.top3())


vera = AthleteList('vera iv')
vera.append('1.31')
vera.extend(['1.22','1.33'])
print(vera.top3())



























    
    
