from sklearn import svm

class API():
  @staticmethod
  def predict(target):
    x = [[0,0], [1,1]]
    y = [0,1]

    classifier = svm.SVC()
    classifier.fit(x, y)    
    return classifier.predict(target)[0]
