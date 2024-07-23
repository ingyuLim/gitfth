from django.shortcuts import render

def main(request):
    return render(request, "main.html")

def burgerlist(request):
    # return HttpResponse("Here is the list of burgers.")
    return render(request, 'burger_list.html')
