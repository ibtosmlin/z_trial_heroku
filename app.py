import datetime
from flask import Flask, render_template, request, url_for
from numpy import maximum
from flask_paginate import Pagination, get_page_parameter
import os

from data import readcsv

app = Flask(__name__)

CT = readcsv.ContentsTable()
per_page = 50
companies = []
for c in CT.companies_ordered:
    sc = c.replace('株式会社', '').replace('相互会社', '').replace('生命保険', '生命')
    companies.append((c, sc))

# for si-pc
years = []
for y in list(CT.years):
    yf = y[0]
    yy = int(y[1:])
    if yf == '<':
        yy -= 1
        yy = f'{yy}年度以前'
    else:
        yy = f'{yy}年度'
    years.append((y, yy))



# for si-pc



@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        page = request.args.get(get_page_parameter(), type=int, default=1)
        tbl_all = CT.df_articles_init
        tbl = tbl_all[(page-1)*per_page: page*per_page]
        total = len(tbl_all)
        pagination = Pagination(page=page, total=total, per_page=per_page, css_framework='foundation')



        return render_template('./index.html',
                update_time=CT.update_date,
                n = len(tbl),
                years = years,
                companies = companies,
                tbl_company_name = list(tbl.company_name),
                tbl_company_url = list(tbl.company_url),
                tbl_article_date = list(tbl.article_date),
                tbl_article_type = list(tbl.article_type),
                tbl_article_title = list(tbl.article_title),
                tbl_article_url = list(tbl.article_url),
                pagination = pagination,
                si_comp = list(tbl.company_name),
                si_comp_all = True,
                si_years = years,
                si_years_all = True,
                si_kwrds = (None, None)
                )


"""
    elif request.method == 'POST':
    tbl = CT.select_table([], CT.years[0:2], '')
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
