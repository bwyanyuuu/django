from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from project.settings import STATICFILES_DIRS
from django.utils.safestring import *
import pandas as pd
from .models import MyUser
from login.forms import EditProfileForm, PasswordChangeForm
from datetime import datetime

@login_required(login_url='/virtual/accounts/login/')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='/virtual/accounts/login/')
def profile(request):
    user = None
    isSelf = False
    try:
        username = request.GET['username']
        user = MyUser.objects.get(username=username)
    except:
        user = MyUser.objects.get(username=request.user)
        isSelf = True
    context = {
        'user' : user,
        'isSelf' : isSelf
    }
    return render(request, 'profile.html', context)

@login_required(login_url='/virtual/accounts/login/')
def editProfile(request):
    user = MyUser.objects.get(username=request.user)
    form = None
    if user.is_authenticated:
        form = EditProfileForm(initial={'first_name': user.first_name, 'middle_name': user.middle_name, 'last_name': user.last_name, 'affiliation': user.affiliation})
        if request.method == "POST":
            form = EditProfileForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('/virtual/profile/')
                
    context = {
        'form' : form,
        'user' : user
    }
    return render(request, 'editProfile.html', context)

@login_required(login_url='/virtual/accounts/login/')
def changePasswd(request):
    form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/virtual/profile/')

    context = {
        'form' : form
    }
    return render(request, 'changePasswd.html', context)

@login_required(login_url='/virtual/accounts/login/')
def schedule(request):
    # init
    url = STATICFILES_DIRS[0] + '/conference.xlsx'
    # df = pd.read_excel(url, engine='openpyxl')
    df = pd.read_csv(STATICFILES_DIRS[0]+'/session.csv')
    tab = '<ul class="tab-title">'
    inner = ''
    tabDict = []

    # pandas    
    day = []
    for i in range(df.shape[0]):
        if df.iat[i, 3] not in tabDict:
            d = {}
            d['idx'] = str(len(tabDict))
            # d['date'] = str(df.iat[i, 3].strftime(format='%a, %b %d'))
            d['date'] = str(datetime.strptime(df.iat[i, 3], "%m/%d/%Y").strftime('%a, %b %d'))
            d['session'] = []
            day.append(d)
            tabDict.append(df.iat[i, 3])

        s = {}
        s['ssid'] = str(df.iat[i, 1])
        s['topic'] = str(df.iat[i, 2])
        s['date'] = str(datetime.strptime(df.iat[i, 3], "%m/%d/%Y").date())
        s['time'] = str(df.iat[i, 0])
        day[-1]['session'].append(s)

    
    context = {
        'day' : day
    }
    return render(request, 'schedule.html', context)


# @login_required(login_url='/virtual/accounts/login/')
# def session(request):
#     # init
#     id = request.GET['id']
#     url = STATICFILES_DIRS[0] + '/conference.xlsx'
#     inner = ''
#     inner2 = ''

#     # pandas
#     dp = pd.read_csv(STATICFILES_DIRS[0]+'/paper.csv')
#     # dp = pd.read_excel(url, sheet_name='Paper', engine='openpyxl')
#     dp = dp[dp['Session ID'] == id]
#     paper = []
#     for i in range(dp.shape[0]):
#         p = {}
#         p['title'] = str(dp.iat[i, 1])
#         p['author'] = str(dp.iat[i, 2])
#         p['school'] = str(dp.iat[i, 3])
#         p['content'] = str(dp.iat[i, 4])
#         paper.append(p)
        
    
#     df = pd.read_excel(url, usecols="B, C, E, F, G", sheet_name='Session', engine='openpyxl')
#     df = df[df['Session ID'] == id]
#     chair = df.iat[0, 2]
#     img = df.iat[0, 3]
#     link = df.iat[0, 4]
#     title = str(id) + ' | ' + str(df.iat[0, 1])
    
#     context = {
#         'title' : title,
#         'paper' : paper,
#         'chair' : chair,
#         'img' : img,
#         'link' : link

#     }
    
#     return render(request, 'session.html', context)


@login_required(login_url='/virtual/accounts/login/')
def session(request):
    # init
    id = request.GET['id']
    url = STATICFILES_DIRS[0] + '/conference.xlsx'
    inner = ''
    inner2 = ''

    # pandas
    # full = pd.read_excel(url, engine='openpyxl', sheet_name=None)
    
    dp = pd.read_csv(STATICFILES_DIRS[0]+'/paper.csv')
    dp = dp[dp['Session ID'] == id]
    paper = []
    for i in range(dp.shape[0]):
        p = {}
        p['title'] = str(dp.iat[i, 1])
        p['author'] = str(dp.iat[i, 2])
        p['school'] = str(dp.iat[i, 3])
        p['content'] = str(dp.iat[i, 4])
        paper.append(p)
        
    
    # df = pd.read_excel(url, usecols="B, C, E, F, G", sheet_name='Session', engine='openpyxl')
    df = pd.read_csv(STATICFILES_DIRS[0]+'/session.csv')
    df = df[df['Session ID'] == id]
    # chair = df.iat[0, 2]
    # img = df.iat[0, 3]
    link = df.iat[0, 4]
    title = str(id) + ' | ' + str(df.iat[0, 2])
    
    
    dc = pd.read_csv(STATICFILES_DIRS[0]+'/chair.csv')
    dc = dc[dc['Session ID'] == id]
    chair = []
    for i in range(dc.shape[0]):
        c = {}
        c['chair'] = str(dc.iat[i, 1])
        if pd.notna(dc.iat[i, 2]):
            c['img'] = str(dc.iat[i, 2])
        else:
            c['img'] = ''
        c['school'] = str(dc.iat[i, 3])
        chair.append(c)
    
    context = {
        'title' : title,
        'paper' : paper,
        'chair' : chair,
        'link' : link
    }
    
    # context = {
    #     'title' : title,
    #     'paper' : paper,
    #     'chair' : chair,
    #     'img' : img,
    #     'link' : link

    # }
    
    return render(request, 'session.html', context)

