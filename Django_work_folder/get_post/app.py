from flask import Flask,request,jsonify

app=Flask(__name__)

@app.route('/get-data',methods = ['GET'])
def get_data():
   name = request.args.get('name')
   age = request.args.get('age')
   return jsonify({
    "method":"GET", 
    "name":name,
    "age":age
   })

@app.route('/post-data',methods = ['POST'])
def post_data():
   data = request.get_json()
   name = data.get('name')
   age = data.get('age')
   return jsonify({
    "method":"POST",
    "name":name,
    "age":age
   })   


if __name__=='__main__':
 app.run(debug=True)