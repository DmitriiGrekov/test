from django.shortcuts import render
from django.http import HttpResponse


def hello_view(request):
    """Выводит сообщение Hello {name}! {message}"""
    name = request.GET.get("name")
    message = request.GET.get("message")
    return render(request, "core/hello.html", {"name": name,
                                               "message": message})



