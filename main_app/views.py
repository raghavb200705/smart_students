from django.shortcuts import render, redirect

ALLOWED_ROLL_NUMBERS = ['S001', 'S002', 'A001', 'A002']  # Add more later

def splash_screen(request):
    return render(request, 'main_app/splash.html')

def login_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        rollno = request.POST.get('rollno')

        if rollno in ALLOWED_ROLL_NUMBERS:
            request.session['name'] = name
            request.session['rollno'] = rollno
            return redirect('home')
        else:
            return render(request, 'main_app/splash.html', {'error': 'Invalid Roll Number'})

    return redirect('splash')


