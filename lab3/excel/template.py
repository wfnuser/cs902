#!/usr/bin/env python
# encoding: utf-8

import sys
import xlwt
import xlrd

Weight = [0.1, 0.1, 0.1, 0.7]

def save(workbook, filename):
    if (not isinstance(workbook, xlwt.Workbook)) and (not isinstance(filename, str)):
        print "type error in save"
        sys.exit(0)
    """
    FIXME
    """

def add_sheet(workbook, sheet_name):
    if (not isinstance(workbook, xlwt.Workbook)) and (not isinstance(sheet_name, str)):
        print "type error in write_cell"
        sys.exit(0)
    """
    FIXME
    """

def write_cell(sheet, x, y, value):
    if (not isinstance(sheet, xlwt.Worksheet)):
        print "type error in write_cell"
        sys.exit(0)
    """
    FIXME
    """

def read_cell(sheet, x, y):
    if (not isinstance(sheet, xlrd.sheet.Sheet)):
        print "type error in read_cell"
        sys.exit(0)
    """
    FIXME
    """

def grade_calculator(grades):
    global Weight
    """
    FIXME
    """

def init_colume_name(orig_sheet, new_sheet):
    columes = orig_sheet.ncols

    # init colume name
    for i in xrange(columes):
        colume_name = read_cell(orig_sheet, 0, i)
        write_cell(new_sheet, 0, i, colume_name)
    write_cell(new_sheet, 0, columes, "Grade")

def process_grade(orig_sheet, new_sheet):
    rows = orig_sheet.nrows
    columes = orig_sheet.ncols

    # copy and calculation
    for i in xrange(1, rows):
        grades = []
        for j in xrange(columes):
            value = read_cell(orig_sheet, i, j)
            if j >= 1:
                grades.append(value)
            write_cell(new_sheet, i, j, value)
        final = grade_calculator(grades)
        write_cell(new_sheet, i, columes, final)

def main():
    write_workbook = xlwt.Workbook(encoding = 'ascii')
    new_sheet = write_workbook.add_sheet("Grade")

    read_workbook = xlrd.open_workbook("test.xls")
    orig_sheet = read_workbook.sheets()[0]

    nrows = orig_sheet.nrows
    ncols = orig_sheet.ncols

    new_sheet.write(0,0,'Name')
    new_sheet.write(0,1,'Lab0')
    new_sheet.write(0,2,'Lab1')
    new_sheet.write(0,3,'Lab2')
    new_sheet.write(0,4,'FinalExam')
    new_sheet.write(0,5,'Grade')

    rownum = 1

    for test in range(nrows):
        avg = 0.0
        if(test == 0): 
            continue
        testarray = orig_sheet.row_values(test)
        #print testarray
        index = 0
        for each in testarray:
            new_sheet.write(rownum,index,"%s"%str(each))
            if(index == 0):
                index = index + 1
                continue
            else:
                avg = avg + int(each)*Weight[index-1]
            index = index + 1

        new_sheet.write(rownum,index,avg)
        rownum = rownum + 1

    write_workbook.save('Grade.xls')

    #init_colume_name(orig_sheet, new_sheet)
    #process_grade(orig_sheet, new_sheet)

    #save(write_workbook, "grade.xls")


if __name__ == "__main__":
    main()
