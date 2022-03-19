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
        yy = f'{yy}年以前'
    else:
        yy = f'{yy}年'
    years.append((y, yy))


    si_years_all = True
    si_years = [y0 for y0, _y1 in years]
    si_comp_all = True
    si_comp = [c0 for c0, _c1 in companies]
    kyrd_inc = ""
    kyrd_exc = ""
    si_kwrds = ("", "")
    tbl_all = CT.df_articles_init


@app.route("/", methods=['GET', 'POST'])
def index():
    global si_years_all, si_years, si_comp_all, si_comp
    global kyrd_inc, kyrd_exc, si_kwrds, tbl_all

    if request.method == 'POST':
        media_type = request.form.get('media-type')
        if media_type == 'menu-pc':
            si_years_all = request.form.get('select-years-all')
            si_years = request.form.getlist('select-years')
            si_comp_all = request.form.get('select-companies-all')
            si_comp = request.form.getlist('select-companies')
            kyrd_inc = request.form.get('keywords-inc')
            kyrd_exc = request.form.get('keywords-exc')
            si_kwrds = (kyrd_inc, kyrd_exc)

        else:
            si_years_all = True
            si_years = request.form.getlist('select-years')
            si_comp = request.form.getlist('select-companies')
            if si_comp[0] != 'all': si_comp_all = False
            kyrd_inc = request.form.get('keywords-inc')
            kyrd_exc = request.form.get('keywords-exc')
            si_kwrds = (kyrd_inc, kyrd_exc)

        tbl_all = CT.df_articles_selected(si_comp, si_years, si_kwrds)

    page = request.args.get(get_page_parameter(), type=int, default=1)
    tbl = tbl_all[(page-1)*per_page: page*per_page]
    total = len(tbl_all)
    pagination = Pagination(page=page, total=total,
                            per_page=per_page,
                            display_msg='<b>{start} - {end} / {total}</b>',
                            css_framework='foundation')

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
            si_comp = si_comp,
            si_comp_all = si_comp_all,
            si_years = si_years,
            si_years_all = si_years_all,
            si_kwrds = si_kwrds,

            )


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
