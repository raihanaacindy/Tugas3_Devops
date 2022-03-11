import sys
import os
#membuat perulangan dengan variable _arg di sys argv 1
for _arg in sys.argv[1:]:
  try:
    #membuat fungsi file io 
    with open(_arg, 'r') as _file:
      for _line in iter((_file.readline),""):
        print(_line),
    #tetapi jika kita salah menginput argumen maka akan muncul pesan oops, something went wrong
  except IOError as e:
        print ('Opps, something went wrong.')
        print (e)