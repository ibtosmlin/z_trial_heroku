from flask import Flask, render_template, request
import os
import readcsv

app = Flask(__name__)

# 更新日時
update_time =  readcsv.get_update_time()
header, contents = readcsv.get_table()

@app.route("/", methods=['GET', 'POST'])
def script():

    if request.method == 'GET':
        return render_template('./index.html',
                update_time=update_time, header=header)
    elif request.method == 'POST':
        datefrom = request.form['datefrom']
        dateto = request.form['dateto']
        company = request.form['company']
        kwrds = request.form['company']
        tabledata = readcsv.select_table(header, contents, datefrom, dateto, company, kwrds)
        return render_template('./index.html',
                update_time=update_time, header=header,
                tabledata=tabledata)


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
