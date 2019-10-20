from django.shortcuts import render
from .forms import UserRegisterForm
# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Your account is created ! You are now able to login'
            messages.success(request, msg)
            return redirect("/")
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)
