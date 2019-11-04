#!/usr/bin/python3
#
# table test for assignment 2
#

import tester
import random

def main():
    test = tester.Core('table test', 5)
    tester.includepath()
    import table
    t = table.Table(int, "abcdefg", range(7))
    
    init = random.randint(0, 99)
    skip = random.randint(1, 9)
    curr = init
    for x in t.xlabels:
        for y in t.ylabels:
            t[y,x] = curr
            curr += skip
    
    curr = init
    for x in t.xlabels:
        for y in t.ylabels:
            if t[y,x] != curr:
                return
            curr += skip
    
    test.add_mark(4)
     
    del t[3,'b']            
    if t[3,'b'] is not None:
        return
        
    test.add_mark(1)
    

if __name__ == '__main__':
    main()
    
