#!/usr/bin/python3
#
# split ev table test for assignment 2
#

import tester
import asst2
import math

total = 25
cutoff = 0.5

def check_split(conn, verbose):    
    result, refobj = asst2.load_result('split')
    val = asst2.similarity(result, refobj, verbose)
    if val >= cutoff:
        conn.send(math.sqrt(val)*total)
    else:
        conn.send(0)
    

def main():
    test = tester.Proc('split test', total)
    mark = test.run_process(check_split)
    test.add_mark(mark)

if __name__ == '__main__':
    main()

    
