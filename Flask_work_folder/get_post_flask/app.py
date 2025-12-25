from flask import Flask,request,jsonify

app=Flask(__name__)

@app.route('/get-data',methods = ['GET'])
def get_data():
   name = request.args.get('name')
   age = request.args.get('age')
   return jsonify({
    "name":name,
    "age":age
   })


if __name__=='__main__':
 app.run(debug=True)