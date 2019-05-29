import zipfile
import sys
import os
import pyfiglet

limpar = 'clear'


count = 1

try:

    file1= sys.argv[1]

    file2 = sys.argv[2]
except:

    os.system(limpar)

    ascii_banner = pyfiglet.figlet_format("ZIP FILE CRACKING ")
    print(ascii_banner)

    print("[+] how to use: python  zipfile_cracking.py <file.zip> <Wordlist.txt>")
    print("[+] script developed by Gabriel Brandao")


    sys.exit()

os.system(limpar)

ascii_banner = pyfiglet.figlet_format("ZIP FILE CRACKING ")
print(ascii_banner)
print("[+] script developed by Gabriel Brandao")





with open(file2,'rb') as text:
    for entry in text.readlines():
        password = entry.strip()
        try:
            with zipfile.ZipFile(file1,'r') as zf:
                zf.extractall(pwd=password)

                data = zf.namelist()[0]

                data_size = zf.getinfo(data).file_size
                     
                print('''******************************\n[+]password found - %s\n[+]file: %s\n[+]size: %s\n******************************'''
                    % (password.decode('utf8'), data, data_size))
                break

        except:
            number = count
            print('[%s] [-] password not found! - %s' % (number,password.decode('utf8')))
            count += 1
            pass

ascii_banner = pyfiglet.figlet_format("ZIPFILE CRACKING ")
print(ascii_banner)
print("[+] script developed by Gabriel Brandao")
