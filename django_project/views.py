from django.shortcuts import render
import requests


def index(request):
  r1 = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
  res1 = r1.json()
  fact = res1["text"]

  
  r2 = requests.get('https://www.boredapi.com/api/activity')
  res2 = r2.json()
  activity = res2["activity"]

  r3 = requests.get('https://dog.ceo/api/breeds/image/random')
  res3 = r3.json()
  dog = res3["message"]

  if request.method == 'POST':
    photo = request.POST['photo']
  else:
    photo = None
  
  return render(request, 'templates/index.html', {'fact': fact, 'activity': activity, 'dog': dog, 'photo':photo} )