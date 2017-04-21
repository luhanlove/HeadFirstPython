#coding:utf-8
def fileio(filename):
    try:
        data = open(filename)
        for each_line in data:
            try:
                (role,line) = each_line.split(":",1)
                print(role,end=' ')
                #注意一个细节问题：我们读取行时，换行符是一并被读取的，所以print需要加''，如果直接print的话，解释器会自动再换一次行。
                print(line,end='')
            except ValueError:
                pass
        data.close()
    except IOError:
        print("The file is not exist.")
                
    
