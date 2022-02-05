import csv

filename = './test.csv'
header_def = './test_header.csv'
update_date = './update_date.csv'

def get_table():
    with open(header_def, encoding='utf8', newline='') as f:
        csvreader = csv.reader(f, delimiter=",", doublequote=True)
        header = [row for row in csvreader]
        header = header[0]
    with open(filename, encoding='utf8', newline='') as f:
        csvreader = csv.reader(f, delimiter=",", doublequote=True)
        content = [row for row in csvreader]
    return header, content


def get_update_time():
    with open(update_date, encoding='utf8', newline='') as f:
        csvreader = csv.reader(f, delimiter=",", doublequote=True)
        content = [row for row in csvreader]
    return content[0][0]


def select_table(head, contents, fm, to, comp, kwd):
    retstr = ['<table>']
    retstr.append('<tr>')
    for hi in head:
        retstr.append(f'<th>{hi}</th>')
    retstr.append('</tr>')
    for ci in contents:
        retstr.append('<tr>')
        for hi in ci:
            retstr.append(f'<td>{hi}</td>')
        retstr.append('</tr>')
    retstr.append('</table>')
    return '\n'.join(retstr)



if __name__ == '__main__':
    print(get_update_time())