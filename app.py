import datetime
from flask import Flask, render_template, request, url_for
import os
import re

from data import readcsv

app = Flask(__name__)

CT = readcsv.ContentsTable()


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        tbl = CT.select_table([], CT.years[0:2], '')
        return render_template('./index.html',
                update_time=CT.update_date,
                n = len(tbl),
                tbl_company_name = list(tbl.company_name),
                tbl_company_url = list(tbl.company_url),
                tbl_article_date = list(tbl.article_date),
                tbl_article_type = list(tbl.article_type),
                tbl_article_title = list(tbl.article_title),
                tbl_article_url = list(tbl.article_url),
                )
"""
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
"""



if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
