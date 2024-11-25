from django.shortcuts import render,redirect
from item.models import Category ,Item
from.forms import SignupForm
from django.contrib.auth import logout



# Create your views here.
def index(request):
    items=Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all()
    context={
        'categories': categories,
        'items': items,
    }
    
    return render(request, 'core/index.html',context )

def Contact(request):
    return render (request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

def user_logout(request):
    # Log the user out
    logout(request)
    # Redirect to the main page (index)
    return redirect('core:index')