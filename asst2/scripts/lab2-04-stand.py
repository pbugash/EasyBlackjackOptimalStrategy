#!/usr/bin/python3
#
# stand ev table test for assignment 2
#

import tester
import asst2
import math

total = 10
cutoff = 0.5

def check_stand(conn, verbose):    
    result, refobj = asst2.load_result('stand')
    val = asst2.similarity(result, refobj, verbose)
    if val >= cutoff:
        conn.send(math.sqrt(val)*total)
    else:
        conn.send(0)
    

def main():
    test = tester.Proc('stand test', total)
    mark = test.run_process(check_stand)
    test.add_mark(mark)

if __name__ == '__main__':
    main()

    
