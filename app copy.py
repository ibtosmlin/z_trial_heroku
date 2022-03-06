import datetime
from flask import Flask, render_template, request, url_for
import os
import re

from data import readcsv

app = Flask(__name__)

CT = readcsv.ContentsTable()
d_today = datetime.date.today()
d_today_str = str(d_today)
header_list = ['日付', '会社名', '分類', '件名']
days_list = [('D90', '90日以内')]
_year = int(d_today_str[:4])
for i in range(3):
    days_list.append((f'Y{_year-i}', f'{_year-i}年'))
days_list.append((f'B{_year-3}', f'{_year-3}年以前'))


@app.route("/", methods=['GET', 'POST'])
def index():
    global date_fm, date_to
    if request.method == 'GET':
        days_selected = [u for u, _v in days_list]
        return render_template('./index.html',
                update_time=CT.update_time,
                header=header_list,
                header_dict=CT.header_dict,
                companies=CT.company_list,
                days=days_list,
                tabledata=CT.table,
                days_selected=days_selected,
                companies_selected = CT.company_list,
                kwrds = ""
                )

    elif request.method == 'POST':
        days = request.form.getlist('select-days')
        comps = request.form.getlist('select-company')
        kwrds = request.form.get('keywords')
        kwrds = search_string_to_list(kwrds)
        return render_template('./index.html',
                update_time=CT.update_time,
                header=header_list,
                header_dict=CT.header_dict,
                companies=CT.company_list,
                days=days_list,
                tabledata=CT.select_table(comps, days, d_today, kwrds),
                companies_selected = comps,
                days_selected = days,
                kwrds = " ".join(kwrds)
                )


def search_string_to_list(tgt: str)-> list:
    tgts = re.split('\s+', tgt)
    tgts = [tgt for tgt in tgts if len(tgt)!=0]
    return tgts


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)