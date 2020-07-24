from django.shortcuts import render
from myapp.models import Ratings
from django.http import JsonResponse
from django.http import HttpResponse

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