from django.shortcuts import render
import joblib
import numpy as np
from .models import Users

def predict(ls):
    model = joblib.load('prediction/model/pneumonia_detection_model.joblib')
    result = model.predict([ls])
    return result

# Create your views here.
def index(request):
    return render(request, 'prediction/index.html', {'title': "Pneumonia Detection" })


def my_view(request):
    if request.method == 'POST':
        test = []
        if ((request.POST.get('gender')) == "Male"):
            test.append(1)
        else:
            test.append(0)
        test.append(request.POST.get('age'))
        test.append(request.POST.get('fever'))
        test.append(request.POST.get('cough'))
        test.append(request.POST.get('breathing_difficulty'))
        test.append(request.POST.get('weight_loss'))  
        test.append(request.POST.get('headache'))
        test.append(request.POST.get('fainting'))
        test.append(request.POST.get('bronchitis_infection'))
        test.append(request.POST.get('chest_pain'))
        test.append(request.POST.get('tuberculosis_history'))
   
        
        
        
        
        test = [int(x) for x in test]
        
        # array = np.asarray(test, dtype=np.int32)
        prediction = predict(test)
        if (prediction == 1):
            user = Users(age= int(test[1]),gender = request.POST.get('gender') , test = "Positive")
            message = "Positive"
            user.save()
            text = "You have Pneumonia please consult a doctor  and take a chest x-ray"
            return render(request, 'prediction/home.html', {'text': text, 'result': message })
        else:
            user = Users(age= int(test[1]),gender = test[0], test = "Negative")
            user.save()
            message = "Negative"
            text ="You don't have Pneumonia but please consult a doctor if you have any symptoms and take a chest x-ray"
            return render(request, 'prediction/home.html', {'result': message, 'text': text, 'title': "Pneumonia Detection" })
        # do something with the values
        
    else:
        # handle GET request
        pass
        error = "Error"
        return render(request, 'prediction/home.html',  {'result': error })
    
def about(request):
    return render(request, 'prediction/about.html', {'title': "About" })
