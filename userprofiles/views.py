
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import UserProfile

def profile_view(request):
    users=UserProfile.objects.all()
    if request.method == 'POST':
        uname = request.POST.get('uname')
        bio = request.POST.get('bio')
        skills = request.POST.get('skills')
        cnum = request.POST.get('cnum')
        u=UserProfile(user =uname,bio=bio,skills=skills,contact_number=cnum)
        u.save()
    return render(request, 'profile.html',{'users':users})
def listuser(request):
    users=UserProfile.objects.all()
    return render(request, 'listuser.html',{'users':users})
def detailsview(request,user_id):
    user=UserProfile.objects.get(id=user_id)
    return render(request, 'detailview.html', {'user': user})
def updateuser(request,user_id):
    user = UserProfile.objects.get(id=user_id)
    if request.method == 'POST':
        uname = request.POST.get('uname')
        bio = request.POST.get('bio')
        skills = request.POST.get('skills')
        cnum = request.POST.get('cnum')
        user.user=uname
        user.bio = bio
        user.skills =skills
        user.contact_number = cnum
        user.save()
    return render(request, 'updateview.html',{'user':user})
