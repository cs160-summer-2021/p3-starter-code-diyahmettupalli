from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def demo(request):
    return render(request, 'coloring/demo.html')

def new_interaction(request):
    return render(request, 'coloring/new_interaction.html')

def e(request):
    return render(request, 'coloring/e.html')

def f(request):
    return render(request, 'coloring/f.html')

def g(request):
    return render(request, 'coloring/g.html')

def h(request):
    return render(request, 'coloring/h.html')

def i(request):
    return render(request, 'coloring/i.html')

def j(request):
    return render(request, 'coloring/j.html')

def k(request):
    return render(request, 'coloring/k.html')
