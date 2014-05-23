import numpy as np
def CharToNum(Char):
    Char=Char.split()
    Char=''.join(Char)
    nparray=np.array([(map(ord, Char))])-ord('0')
    return ''.join(map(str,list(flatten(nparray))))

from collections import Iterable
def flatten(lis):
     for item in lis:
         if isinstance(item, Iterable) and not isinstance(item, basestring):
             for x in flatten(item):
                 yield x
         else:        
             yield item

