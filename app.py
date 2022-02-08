from flask import Flask, render_template, request, url_for
import os
from data import readcsv
import datetime


app = Flask(__name__)

# 更新日時
update_time =  readcsv.get_update_time()
header, contents = readcsv.get_table()
d_today = str(datetime.date.today())
date_fm = "2000-04-01"
date_to = d_today

@app.route("/", methods=['GET', 'POST'])
def script():
    global date_fm, date_to
    if request.method == 'GET':
        return render_template('./index.html',
                update_time=update_time, header=header,
                datefrom = date_fm, dateto = date_to
                )

    elif request.method == 'POST':
        date_fm = request.form['datefrom']
        date_to = request.form['dateto']
        company = request.form['company']
        kwrds = request.form['company']
        tabledata = readcsv.select_table(header, contents, date_fm, date_to, company, kwrds)
        return render_template('./index.html',
                update_time=update_time, header=header,
                datefrom = date_fm, dateto = date_to,
                tabledata=tabledata
                )

#def links(url)


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
