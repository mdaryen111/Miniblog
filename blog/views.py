from django.shortcuts import render , redirect
from .models import*
# Create your views here.
def home(request):
    home = Home.objects.all()

    context = {'home':home}

    return render(request, 'blog/index.html',context)

def blog(request):
    home = Home.objects.all()
    context = {'home':home}

    return render(request,'blog/blog.html',context)

def contact(request):
    home = Home.objects.all()
    context = {'home':home}

    if request.method == "POST":
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        #email  = request.POST['email']
        #subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(first_name=firstname,last_name=lastname,message=message)
        contact.save()

        return redirect('/contact')
    return render(request,'blog/contact.html',context)

def category(request):
    home = Home.objects.all()

    context = {'home':home}
    return render(request,'blog/category.html',context)

def single(request):
    home = Home.objects.all()

    context = {'home':home}
    return render(request,'blog/single.html',context)