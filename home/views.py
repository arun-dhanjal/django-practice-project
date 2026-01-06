from django.shortcuts import render


def homepage(request):
    apps = [
        {"name": "Blog", "url": "/blog/"},
        {"name": "Shop", "url": "/shop/"},
        {"name": "Tasks", "url": "/tasks/"},
    ]
    return render(request, "home/home.html", {"apps": apps})
