import csv
import datetime
from operator import itemgetter
import os
import re


libpath = os.path.dirname(__file__)
filename = os.path.join(libpath, 'data_informations.csv')
header_def = os.path.join(libpath, 'def_header.csv')
update_date = os.path.join(libpath, 'data_update_date.csv')
comp_url = os.path.join(libpath, 'data_companies.csv')


class ContentsTable:
    def __init__(self) -> None:
        self.header_dict = None
        self.table = None
        self.company_list = None
        self.update_time = None

        with open(header_def, encoding='utf-8-sig', newline='') as f:
            csvreader = csv.reader(f, delimiter=",", doublequote=True)
            header_dict = {head:i for i, head in enumerate([row for row in csvreader][-1])}


        # 会社名の辞書
        # comp_dict = {"xxcomp": (company_no, company_url)}
        company_dict = dict()
        company_list = []
        with open(comp_url, encoding='utf-8-sig', newline='') as f:
            csvreader = csv.reader(f, delimiter=",", doublequote=True)
            for i, row in enumerate(csvreader):
                company_dict[row[0]] = [i, row[1]]
                company_list.append(row[0])

        self.company_list = company_list

        with open(filename, encoding='utf-8-sig', newline='') as f:
            csvreader = csv.reader(f, delimiter=",", doublequote=True)
            table = [row for row in csvreader]

        company_col = header_dict['会社名']
        date_col = header_dict['日付']
        for i, ti in enumerate(table):
            company_no, company_url = company_dict[ti[company_col]]
            table[i] = ti + [company_no, company_url]

        pre_header_dict_len = len(header_dict)
        header_dict['company_no'] = company_no_col = pre_header_dict_len
        header_dict['company_url'] = pre_header_dict_len + 1

        # 会社順
        table.sort(key=itemgetter(date_col), reverse=True)
        table.sort(key=itemgetter(company_no_col))
        table = [ti + [i] for i, ti in enumerate(table)]
        # 日付順
        table.sort(key=itemgetter(date_col), reverse=True)
        table = [ti + [i] for i, ti in enumerate(table)]


        self.table = table

        pre_header_dict_len = len(header_dict)
        header_dict['IdSortByCompany'] = pre_header_dict_len
        header_dict['IdSortByDate'] = pre_header_dict_len + 1

        self.header_dict = header_dict

        with open(update_date, encoding='utf-8-sig', newline='') as f:
            csvreader = csv.reader(f, delimiter=",", doublequote=True)
            update_time = [row[0] for row in csvreader][0]

        self.update_time = update_time


    def select_table(self, comps, days, d_today, kwrds):
        if kwrds: regex = re.compile('|'.join(kwrds))
        ret = []
        for content in self.table:
            if not self._check_comp(content, comps): continue
            if not self._check_day(content, days, d_today): continue
            if kwrds:
                if not self._check_kwd(content, regex): continue
            ret.append(content)
        return ret

    def _check_comp(self, content, company):
        return content[self.header_dict['会社名']] in company

    def _check_day(self, content, days, d_today):
        datestr = content[self.header_dict['日付']]
        for dayid in days:
            if datestr == '---': return dayid == 'M90'
            if dayid[0] == 'Y':
                if int(dayid[1:]) == int(datestr[:4]): return True
            elif dayid[0] == 'B':
                if int(dayid[1:]) >= int(datestr[:4]): return True
            else:
                dt = d_today - datetime.datetime.strptime(datestr, '%Y-%m-%d').date()
                if dt.days <= 90: return True
        return False


    def _check_kwd(self, content, regex):
        if regex.findall(content[self.header_dict['件名']]):
            return True
        else: False


if __name__ == '__main__':
    CT = ContentsTable()
    print(CT.select_table(['日本生命'], 1, ['保険金', '金庫']))
