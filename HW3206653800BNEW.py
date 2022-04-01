import re
def longest_words(file):
    try:
        my_file = open(file, "r")
    except FileNotFoundError:
        print('file not found')
        return([])
    else:
        data = my_file.read()
        data_into_list = data.replace('\n', ' ')
        regex = re.compile('[^a-zA-Z]')
        data =re.sub("[^a-zA-Z]+", " ", data_into_list).split(' ')
        max1 = max(data, key=len)
        while max1 in data: data.remove(max1)  
        max2 = max(data, key=len)
        while max2 in data: data.remove(max2)
        max3 = max(data, key=len)
        while max3 in data: data.remove(max3)
        max4 = max(data, key=len)
        while max4 in data: data.remove(max4)
        max5 = max(data, key=len)
        while max5 in data: data.remove(max5) 
        return([max1,max2,max3,max4,max5])       
print(longest_words('ex3_text (1).txt'))
longest_words('ex4_text (1).txt') 
