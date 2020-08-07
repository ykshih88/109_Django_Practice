from django.shortcuts import render
from myapp.models import Ratings
from django.http import JsonResponse
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def get_id(request):
    user_id=request.GET.get('user_id')
    movies=Ratings.objects.filter(user_id=user_id)
    userList = []
    for i in movies:
        user_temp={}
        user_temp['id']=i.id
        user_temp['user_id']=i.user_id
        user_temp['movie_id']=i.movie_id
        user_temp['rating']=i.rating
        userList.append(user_temp)
    return JsonResponse({'data': userList})
    # return movies

def insert_id(request):
    user_id=request.GET.get('user_id')
    movie_id=request.GET.get('movie_id')
    rating=request.GET.get('rating')
    data_instance=Ratings.objects.create(user_id=user_id,movie_id=movie_id,rating=rating)
    # data_instance.save()
    
    movies=Ratings.objects.filter(user_id=user_id,movie_id=movie_id,rating=rating)
    userList = []
    for i in movies:
        user_temp={}
        user_temp['id']=i.id
        user_temp['user_id']=i.user_id
        user_temp['movie_id']=i.movie_id
        user_temp['rating']=i.rating
        userList.append(user_temp)
    return JsonResponse({'data': userList})

def delete(request):
    user_id=request.GET.get('user_id')
    movie_id=request.GET.get('movie_id')
    result=Ratings.objects.filter(user_id=user_id,movie_id=movie_id).delete()
    return HttpResponse(result)

def update(request):
    user_id=request.GET.get('user_id')
    movie_id=request.GET.get('movie_id')
    rating=request.GET.get('rating')
    result=Ratings.objects.filter(user_id=user_id,movie_id=movie_id).update(rating=rating)

    #check success or not
    movies=Ratings.objects.filter(user_id=user_id,movie_id=movie_id)
    userList = []
    for i in movies:
        user_temp={}
        user_temp['id']=i.id
        user_temp['user_id']=i.user_id
        user_temp['movie_id']=i.movie_id
        user_temp['rating']=i.rating
        userList.append(user_temp)
    return JsonResponse({'data': userList})

def GUI(request):
    user_id=request.GET.get('user_id')
    movies=Ratings.objects.filter(user_id=user_id)
    userList = []
    for i in movies:
        user_temp={}
        user_temp['id']=i.id
        user_temp['user_id']=i.user_id
        user_temp['movie_id']=i.movie_id
        user_temp['rating']=i.rating
        userList.append(user_temp)
    
    context = {
        'data': userList
    }
    print(context)
    return render(request,"myapp/mytemplate.html",context)