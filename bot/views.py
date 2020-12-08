from django.shortcuts import render, redirect
from bot.models import userInfo, contactForm

def getIndex(request):
  return render(request,'index.html')

def getForm(request):
  return render(request,'input.html')

def getAbout(request):
  return render(request, 'about.html')

def getContact(request):
  return render(request, 'contact.html')

def acceptContact(request):
  contact = contactForm()

def runBot(request):
  print(request.GET)
  user = userInfo(first_name = request.GET["first_name"],
                  last_name = request.GET["last_name"],
                  email = request.GET["email"],
                  addr = request.GET["addr"],
                  city = request.GET["city"],
                  state = request.GET["state"],
                  zip_code = request.GET["zip_code"],
                  card_number = request.GET["card_number"],
                  exp_date = request.GET["exp_date"],
                  ccv = request.GET["ccv"],
                  product_id = "newProduct",
                  shoe_size = request.GET["shoe_size"])
  user.save()
  return redirect("index")