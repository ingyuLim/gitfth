from django.shortcuts import render
from burgers.models import Burger
def main(request):
    # return HttpResponse("Hello, I'm Pyburger.")
    return render(request, "main.html")

def burger_list(request):
	burgers = Burger.objects.all()
	print("The list of all burgers:",burgers)

	context = {
            "burgers": burgers
	}
	return render(request, "burger_list.html", context)
