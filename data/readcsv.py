import csv
import os
import re


libpath = os.path.dirname(__file__)
filename = os.path.join(libpath, 'test.csv')
header_def = os.path.join(libpath, 'test_header.csv')
update_date = os.path.join(libpath, 'update_date.csv')
comp_url = os.path.join(libpath, 'list_li_utf8.csv')


with open(comp_url, encoding='utf-8-sig', newline='') as f:
    csvreader = csv.reader(f, delimiter=",", doublequote=True)
    comp_url_dict = {row[0]: row[1] for row in csvreader}


def get_table():
    with open(header_def, encoding='utf-8-sig', newline='') as f:
        csvreader = csv.reader(f, delimiter=",", doublequote=True)
        header = [row for row in csvreader]
        header = header[0]
    with open(filename, encoding='utf-8-sig', newline='') as f:
        csvreader = csv.reader(f, delimiter=",", doublequote=True)
        content = [row + [comp_url_dict[row[0]]] for row in csvreader]
    return header, content


def get_update_time():
    with open(update_date, encoding='utf-8-sig', newline='') as f:
        csvreader = csv.reader(f, delimiter=",", doublequote=True)
        content = [row for row in csvreader]
    return content[0][0]


def select_table(head, contents, fm, to, comp, kwd):
    ret = []
    for con in contents:
#        if comp == con[0]:
        ret.append(con)
    return ret



if __name__ == '__main__':
    print(get_update_time())