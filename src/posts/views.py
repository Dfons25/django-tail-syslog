from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, StreamingHttpResponse
from celery.result import AsyncResult
from django.shortcuts import render
from .models import Pub
from time import sleep
from django.views.decorators.http import condition
from .tasks import debug_task
import json
# Create your views here.
# CRUD

#list all posts
def post_list_view(request):
    if request.method == "POST":
        print('post')
    if request.method == "GET":
        print('get')
    post_objects = Pub.objects.all()
    # print(request.POST.get(''))
    print('post_list_view')
    context = {
        'post_objects': post_objects
    }

    return render(request, "posts/index.html", context)

def hacky_get(request):
    if request.method == "GET":
        job = debug_task.apply_async()
        return JsonResponse({'job_id': job.id})
    if request.method == "POST":
        json_data = json.loads(request.body)
        job_id = json_data['job_id']
        print(job_id)
        job = AsyncResult(job_id)
        print(job)
        data = job.result or job.state
        context = {
            'data': data,
            'task_id': job_id,
        }
        print(context)
        return JsonResponse(context)

    return JsonResponse({'hacky_endpoint': 'post callback'})
