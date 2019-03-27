from flask import Flask,render_template
import myutil
app = Flask(__name__)

Plist = []
@app.route("/listParking.do")
def listParking():
    global Plist
    Plist = myutil.getParking()
    print('가져온 주차장 데이터의 수 : ',len(Plist))
    return render_template('listParking.html',Plist=Plist)

@app.route("/parkingMap/<idx>")
def mapParking(idx):
    i = int(idx) -1
    print(Plist[i])
    item = Plist[i]

    return render_template('parkingMap.html',item=item)


if __name__ == '__main__':
    app.run(host='203.236.209.96',debug=True)