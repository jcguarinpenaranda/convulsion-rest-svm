from flask import Flask, jsonify, request
from sklearn import datasets, svm
from classifier.test import API
from classifier.SVM1 import SVM

app = Flask(__name__)

# Load Dataset from scikit-learn.
digits = datasets.load_digits()

@app.route('/', methods=['GET','POST'])
def main():
  # Get the target url query parameter
  target=request.args.get('target')

  # Return an error if not target sent
  if not target:
    return jsonify({'error': 'Please send "target" query parameter'})
  
  # 0,1 -> [0, 1]
  values = target.split(',')

  # Return an error if target is not in shape x,y
  if len(values) != 4:
    return jsonify({'error': 'Please send "target" query parameter well formed. Example: ?target=0,1,2,3'})    

  # Returns value on get
  if request.method == 'GET':
    instance = SVM()
    res = instance.predict(target = [values[0], values[1], values[2], values[3]])[0]
    return jsonify({'prediction': res})
  else:
    return jsonify({'status': 'ok'})


# host/?target=0,1
@app.route('/test', methods=['GET','POST'])
def hello():
  # Get the target url query parameter
  target=request.args.get('target')

  # Return an error if not target sent
  if not target:
    return jsonify({'error': 'Please send "target" query parameter'})
  
  # 0,1 -> [0, 1]
  values = target.split(',', 1)

  # Return an error if target is not in shape x,y
  if not values[0] or not values[1]:
    return jsonify({'error': 'Please send "target" query parameter well formed. Example: ?target=0,1'})    

  # Returns value on get
  if request.method == 'GET':
    res = API.predict([values[0],values[1]])
    return jsonify({'prediction': res})
  else:
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
  app.run(host='0.0.0.0')
