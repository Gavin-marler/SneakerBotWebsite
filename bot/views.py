from django.shortcuts import render, redirect

def getIndex(request):
  return render(request,'index.html')

def getForm(request):
  return render(request,'input.html')

def runBot(request):
  print(request.GET)
  return redirect("index")