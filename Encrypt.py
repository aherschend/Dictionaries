def main():

    dict = {'a' : '[' , 'b': ']', 'c': '{', 'd': '}' ,'e': '=','f': '+','g': ':',
    'h': ';','i': '|', 'j':'!','k':'@', 'l':'%', 'm': '&', 'n':'*', 'o': ')', 'p': '~',
     'q': '-', 'r': '>', 's': '?', 't': '/', 'u': '<', 'v':'(', 'w': '`', 'x': '_',
    'y': '7', 'z': '0'}

    infile = open('info_security.txt', 'r')
    outfile = open('new_info_security.txt', 'w')

    file_contents = infile.read()

    for line in file_contents:
        for ch in line.lower():
            encrypted_txt = ''
            if ch in dict: 
                encrypted_txt += str(dict[ch])
                outfile.write(encrypted_txt)
            else:
                encrypted_txt += ch 
                outfile.write(encrypted_txt)

main()
                

