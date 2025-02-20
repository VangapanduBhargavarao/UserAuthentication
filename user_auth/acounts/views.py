
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from .models import CustomUser
from .forms import SignupForm,LoginForm
# Create your views here.

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST,request.FILES)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form=SignupForm()
    return render(request,'signup.html',{'form':form})

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def login_view(request):
    if request.method=='POST':
        form=LoginForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=CustomUser.objects.filter(username=username).first()
            if not user:
                user = CustomUser.objects.filter(email=username).first()
            if user:
                authenticated_user = authenticate(request, username=user.username, password=password)
                if authenticated_user:
                    login(request,authenticated_user)
                    if authenticated_user.role=='patient':
                        return redirect('patient_dashboard')
                    elif authenticated_user.role=='doctor':
                        return redirect('doctor_dashboard')
                    else:
                        return redirect('login')
            return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password.'})

    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})



@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def patient_dashboard(request):
    if request.user.role!='patient':
        return redirect('login')
    return render(request,'patient_dashboard.html',{'user':request.user})

@login_required
def doctor_dashboard(request):
    if request.user.role!='doctor':
        return redirect('login')
    return render(request,'doctor_dashboard.html',{'user':request.user})
