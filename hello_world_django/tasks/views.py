from django.shortcuts import render

tasks = ["eat","sleep","play"]


def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    return render(request, "tasks/add.html")