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

def getConfirm(request):
  return render(request, 'confirm.html')

def acceptContact(request):
  print(request.GET)
  contact = contactForm(name = request.GET["user_name"],
                        email = request.GET["user_email"],
                        message = request.GET["user_message"])
  contact.save()
  return redirect("input")

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
                  product_id = request.GET["sneaker"],
                  shoe_size = request.GET["shoe_size"])
  user.save()
  return redirect("confirm")