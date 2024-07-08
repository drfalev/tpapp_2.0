from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)
# app.config['JSON_AS_ASCII'] = False

L = [
  {
    'a':'alma'
    , 'b':'banán'
    , 'c':'citrom'
    , 'd':'cseresznye'
  }
  , {
    'a':'répa'
    , 'b':'retek'
    , 'c':'tök'
    , 'd':'mogyoró'
  }
]

app.json.ensure_ascii = False # ez kell a magyar (és gonodolom a swiss) karakterekhez...

@app.route("/")
def hello_wolrld():
  # return "Hello World now"  
  return render_template('home.html'
                        , list=L
                        )
@app.route("/api/L")
def api_list_L():
  return jsonify(L)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)








#  print("Hello World!")
