'''
1. List given containing 0,1 etc. Ex: [0, 1, 1, 1,,0,0,1,1] .0 means absent, 1 means present.Find total absentees and presentees.
INPUT:  status(S)                                        [0, 1, 0, 0, 1, 0, 1]
OUTPUT: result(R)                                        3 3
INPUT:  status(S)                                        [1, 1, 0, 1, 0]
OUTPUT: result(R)                                        3 2
'''
status = [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]
print(status.count(1), status.count(0))