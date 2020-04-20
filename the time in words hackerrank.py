import math

if __name__ == '__main__':

    time={
        1:"one",
        2:"two",
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine",
        10:"ten",
        11:"eleven",
        13:"thirteen",
        14:"fourteen",
        16:"sixteen",
        17:"seventeen",
        18:"eighteen",
        19:"nineteen",
        20:"twenty",
        21:"twentyone",
        22:"twenty two",
        23:"twenty three",
        24:"twenty four",
        25:"twenty five",
        26:"twenty six",
        27:"twenty seven",
        28:"twenty eight",
        29:"twenty nine",
        }

    h=int(input())
    m=int(input())


    if m==0:
        print(time[h] + ' o\' clock')
    elif m==1:
        print('one minute past ' + time[h])
    elif(m==15):
        print('quarter past ' + time[h])
    elif(m==30):
        print('half past ' + time[h])
    elif(m==45):
        print('quarter to ' + time[h+1])
    elif(m==59):
        print('one minute to ' + time[h+1])
    elif m<30:
        print(time[m] + ' minutes past ' + time[h])
    else :
        m=60-m
        print(time[m] + ' minutes to ' + time[h+1])
    
    


