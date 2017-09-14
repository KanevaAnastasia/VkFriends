from django.shortcuts import render
import requests
import json
# Create your views here.
from django.http import HttpResponse



def index(request):
    return render(request, 'friends/index.html')
def main(request, user_id):
    user = "https://api.vk.com/method/users.get?user_id=" + str(user_id)+"&lang=0&fields=photo_200"
    friends_id_list = 'https://api.vk.com/method/friends.get?user_id=' + str(user_id)+"&count=5&order='random'"
    user_vk = requests.get(user).json()['response'][0]
    friends_id_list = requests.get(friends_id_list).json()['response']
    friends = []
    for i in friends_id_list:
        url = "https://api.vk.com/method/users.get?user_id=" + str(i)+"&lang=0&fields=photo_100"
        friend_json = requests.get(url)
        friend = friend_json.json()['response'][0]
        friends.append(friend)
    context = {'user_vk': user_vk, 'friends': friends, 'url_id': user_id}
    return render(request, 'friends/main.html', context)