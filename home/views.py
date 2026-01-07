from django.shortcuts import render


def homepage(request):
    apps = [
        {"name": "Quiz App", "url": "/quiz-app/"},
    ]
    return render(request, "home/home.html", {"apps": apps})
