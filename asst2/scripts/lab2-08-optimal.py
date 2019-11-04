#!/usr/bin/python3
#
# optimal ev table test for assignment 2
#

import tester
import asst2
import math

total = 5
cutoff = 0.5

def check_optimal(conn, verbose):    
    result, refobj = asst2.load_result('optimal')
    val = asst2.similarity(result, refobj, verbose)
    if val >= cutoff:
        conn.send(math.sqrt(val)*total)
    else:
        conn.send(0)
    

def main():
    test = tester.Proc('optimal test', total)
    mark = test.run_process(check_optimal)
    test.add_mark(mark)

if __name__ == '__main__':
    main()

