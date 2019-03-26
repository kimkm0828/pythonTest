from flask import Flask,request,render_template
import myutil

app = Flask(__name__)

#약국 검색결과 지도
@app.route("/searchPharmacy.do")
def searchPharmacy():

    return render_template('map.html')

@app.route("/pharm/<idx>")
def pharmacy(idx):
    i = int(idx)-1
    item = list[i]
    return render_template("map.html",item=item)



@app.route("/listPharmacy.do")
def listPharmacy():
    global list
    list = myutil.getPharmacy()

    return render_template('listPharmacy.html',list=list)


if __name__ == '__main__':
    app.run(host='203.236.209.96',debug=True)