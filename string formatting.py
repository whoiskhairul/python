def print_formatted(number):
    w = bin(number).replace('0b','')
    w = len(w)
    for i in range(1,number+1) :
        b = bin(i).replace('0b','').rjust(w, ' ')
        o = oct(i).replace('0o', '').rjust(w, ' ')
        h = hex(i).replace('0x','').rjust(w, ' ').upper()
        d = str(i).rjust(w, ' ')

        print(d,o,h,b)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)