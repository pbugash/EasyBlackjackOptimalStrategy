#!/usr/bin/python3
#
# dealer probability table test for assignment 2
#

import tester
import asst2

total = 10
cutoff = 0.5

_DEALER_CODE = [ '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
    '15', '16', '17', '18', '19', '20', 'AA', 'A2', 'A3', 'A4', 'A5', 'A6' ]

def check_dealer(conn, verbose):
    result, refobj = asst2.load_result('dealer')
    mark = total
    for key in _DEALER_CODE:
        if mark <= 0:
            print("too many errors. exiting.")
            mark = 0
            break
        if key not in result:
            print("missing table for {}".format(key))
            mark -= 1
            continue
        stu = result[key]
        ans = refobj[key]
        sk = tuple(stu.keys())
        ak = tuple(ans.keys())
        if sk != ak:
            print("key set mismatch for table {}: {} vs. {}".format(key, sk, ak))
            mark -= 1
            continue
        for pts in ak:
            if not asst2.isclose(stu[pts], ans[pts]):
                print("probability mismatch for table {}, score {}:" \
                " {} vs. {}".format(key, pts, stu[pts], ans[pts]))
                mark -= 1
                break
    conn.send(int(mark))

def main():
    test = tester.Proc('dealer test', total)
    mark = test.run_process(check_dealer)
    test.add_mark(mark)

if __name__ == '__main__':
    main()
    
