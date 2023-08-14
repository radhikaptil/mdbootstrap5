from django.shortcuts import render

# Create your views here.
def mdb5(request):
    return render(request,'mdb5.html')
def index(request):
    return render(request,'index.html')
def image(request):
    return render(request,'image.html')
def card(request):
    return render(request,'card.html')
def button(request):
    return render(request,'button.html')
def card1(request):
    return render(request,'card1.html')
def button_group(request):
    return render(request,'button_group.html')
def dropdown(request):
    return render(request,'dropdown.html')
def tooltips(request):
    return render(request,'tooltips.html')


