from django.shortcuts import render
import os
import pickle
import numpy as np
import pandas as pd
# Create your views here.
def index(request):
    res=''
    if request.method=="POST":
        precipitation=float(request.POST['precipitation'])
        temp_max=float(request.POST['temp_max'])
        temp_min=float(request.POST['temp_min'])
        wind=float(request.POST['wind'])
        path=os.path.dirname(__file__)
        model=pickle.load(open(os.path.join(path,'rfp.pkl'),'rb'))       
        x=[precipitation,temp_max,temp_min,wind]
        res=str(model.predict([x])[0])
    return render(request,"index.html",{"res":res})


