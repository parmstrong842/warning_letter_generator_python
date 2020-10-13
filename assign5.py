#!/usr/bin/env python3

import os
import sys
import glob

if not os.path.isdir(sys.argv[1]):
    print(sys.argv[1] + " is not a directory")
    sys.exit(1)
crs_files = glob.glob(sys.argv[1] + "/*.crs")
date = sys.argv[3]
if len(sys.argv) == 7:
    lChar = sys.argv[5]
    rChar = sys.argv[6]
else:
    lChar = '[['
    rChar = ']]'
for crs_file in crs_files:
    f = open(crs_file, 'r')
    tokens = f.readline().split()
    dept_code = tokens[0]
    dept_name = tokens[1]
    course_name = f.readline().rstrip()
    tokens = f.readline().split()
    course_start = tokens[1]
    course_end = tokens[2]
    credit_hours = f.readline().rstrip()
    num_students = f.readline().rstrip()
    course_num = crs_file[len(crs_file)-8:len(crs_file)-4]
    if int(num_students) > 50:
        warn = []
        temp = open(sys.argv[2], 'r')
        for line in temp:
            line = line.replace(lChar + "dept_code" + rChar, dept_code)
            line = line.replace(lChar + "dept_name" + rChar, dept_name)
            line = line.replace(lChar + "course_name" + rChar, course_name)
            line = line.replace(lChar + "course_start" + rChar, course_start)
            line = line.replace(lChar + "course_end" + rChar, course_end)
            line = line.replace(lChar + "credit_hours" + rChar, credit_hours)
            line = line.replace(lChar + "num_students" + rChar, num_students)
            line = line.replace(lChar + "course_num" + rChar, course_num)
            line = line.replace(lChar + "date" + rChar, date)
            warn.append(line)
        temp.close()
        if not os.path.isdir(sys.argv[4]):
            os.mkdir(sys.argv[4])
        os.mknod(sys.argv[4] + "/" + dept_code + course_num + ".warn")
        warn_file = open(sys.argv[4] + "/" + dept_code + course_num + ".warn", 'w')
        for line in warn:
            warn_file.write(line)
        warn_file.close()
    f.close()
