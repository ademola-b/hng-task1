from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime


# Create your views here.
class Task(APIView):
    def get(self, request):
        slack_name = request.GET.get('slack_name')
        track = request.GET.get('track')
        current_time = datetime.datetime.now(datetime.timezone.utc)
        curr = current_time.replace(microsecond=0)
        day = current_time.strftime("%A")
        route = {
            "slack_name": slack_name,
            "current_day": day,
            "utc_time": curr,
            "track": track,
            "github_file_url": "https://github.com/ademola-b/hng-task1/blob/main/task/views.py",
            "github_repo_url": "https://github.com/ademola-b/hng-task1",
            "status_code":200
        }
        return Response(route)

