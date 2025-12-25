from flask import Flask,request,jsonify

app=Flask(__name__)

@app.route('/get-data',methods = ['GET'])
def get_data():
   name = request.args.get('name')
   return jsonify({"message":"This is GET REQUEST"})


@app.route('/post-data', methods=['POST'])
def post_data():
   data = request.json
   return jsonify({
      "message":"POST request recieved",
      "data":data
   })

if __name__=='__main__':
 app.run(debug=True)