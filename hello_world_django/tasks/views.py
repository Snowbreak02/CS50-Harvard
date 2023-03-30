from django.shortcuts import render

tasks = ["yes","no","hi"]


def index(request):
    return render(request, "tasks/index.html", {
    "tasks": tasks
    })