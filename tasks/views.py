from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
class NewTaskForm(forms.Form):
    input_task= forms.CharField(label="New Task")
    priority=forms.IntegerField(label="Priority",min_value=1,max_value=5)

# list_task=["gmail","spam"]
def index(request):
    if "input_task" not in request.session:
        request.session["input_task"]=[]

    return render(request,"tasks/index.html",
    {"display_task":request.session["input_task"]})

def add(request):
    if request.method=="POST":
#takes all the data from the user while submitting the from and stores in the new form
        new_form=NewTaskForm(request.POST) 
# if the created new form is valid  
        if new_form.is_valid():
            added_task=new_form.cleaned_data["input_task"]
            request.session["input_task"]+=[added_task]
#automatically redirects to task list page
            return HttpResponseRedirect(reverse("task:index"))
    return render(request,"tasks/add.html",{"diya_form":NewTaskForm()})