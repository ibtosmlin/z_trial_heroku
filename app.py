import datetime
from flask import Flask, render_template, request, url_for
from numpy import maximum
from flask_paginate import Pagination, get_page_parameter
import os

from data import readcsv

app = Flask(__name__)

CT = readcsv.ContentsTable()
page = 1
per_page_init = 50
per_page_new = ((CT.newcount + 10 - 1) // 10 ) * 10
per_page = max(per_page_init, per_page_new)

si_ym = ""
si_comp_all = True
si_comp = [c0 for c0, _c1 in CT.companies_ordered]
kyrd_inc = ""
kyrd_exc = ""
si_kwrds = ("", "")
tbl_all = CT.df_articles

@app.route("/", methods=['GET', 'POST'])
def index():
    global si_ym, si_comp_all, si_comp, per_page
    global kyrd_inc, kyrd_exc, si_kwrds, tbl_all, page

    if request.method == 'POST':
        post_type = request.form.get('post-type')

        if post_type == 'menu-sp':
            si_ym = request.form.getlist('select-years')[0]
            si_comp = request.form.getlist('select-companies')
            if si_comp[0] != 'all': si_comp_all = False
            kyrd_inc = request.form.get('keywords-inc')
            kyrd_exc = request.form.get('keywords-exc')
            si_kwrds = (kyrd_inc, kyrd_exc)
            per_page = per_page_init
        else:
            pass
    rpage = request.args.get(get_page_parameter(), type=int, default=1)

    if rpage == page:
        tbl_all = CT.df_articles_selected(si_comp, si_ym, si_kwrds)
        page = 1
    else:
        page = rpage

    tbl = tbl_all[(page-1)*per_page: page*per_page]
    total = len(tbl_all)
    pagination = Pagination(page=page, total=total,
                            per_page=per_page,
                            display_msg='<b>{start} - {end} / {total}</b>',
                            css_framework='foundation')

    return render_template('./index.html',
            update_time=CT.update_date,
            news = CT.news,
            n = len(tbl),
            companies = CT.companies_ordered,
            tbl_company_name = list(tbl.company_name_s),
            tbl_company_url = list(tbl.company_url),
            tbl_article_date = list(tbl.article_date),
            tbl_article_type = list(tbl.article_type),
            tbl_article_title = list(tbl.article_title),
            tbl_article_url = list(tbl.article_url),
            tbl_is_new = list(tbl.is_new),
            pagination = pagination,
            si_ym = si_ym,
            si_comp = si_comp,
            si_comp_all = si_comp_all,
            si_kwrds = si_kwrds,
            )


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
