from django.shortcuts import render
from . import a_model

def home(request):
    return render(request, 'index.html')

def result(request):
    pclass = round(int(request.GET["pclass"]))
    sex = int(request.GET["sex"])
    age = int(request.GET["age"])
    sibsp = int(request.GET["sibsp"])
    parch = int(request.GET["parch"])
    fare = int(request.GET["fare"])
    embarked = int(request.GET["embarked"])
    title = int(request.GET["title"])

    prediction = a_model.predict(pclass,sex,age,sibsp,parch,fare,embarked,title)
    return render(request, 'result.html', {"prediction": prediction})
