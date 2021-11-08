
import pickle
from flask import Flask, request , jsonify , render_template
from flask_cors import CORS, cross_origin

file = open("duration_model.sav",'rb')
model = pickle.load(file)
file.close()

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/predict',methods=['POST'])
@cross_origin()
def predict():
    
    dataList = request.get_json()
    predList = []
    for data in dataList:
        month = float(data['month'])/12
        day = float(data['day'])/6
        week = float(data['week'])/5
        cabin = float(data['cabin'])
        trip = float(data['trip'])/2
        origin_lat = float(data['origin_lat'])/90
        origin_lon = float(data['origin_lon'])/180
        dest_lat = float(data['dest_lat'])/90
        dest_lon = float(data['dest_lon'])/180
        pred = model.predict([[month,day,week,trip,cabin,origin_lon,origin_lat,dest_lon,dest_lat]])
        pred = int(pred[0])
        predList.append({'pred':pred,'month':data['month'],'day':data['day'],'week':data['week']})
    return jsonify(predList)

@app.route('/travel')
@cross_origin()
def home():
    return render_template('index.html')


if __name__ == '__main__':
     app.run()