from django.shortcuts import render
from burgers.models import Burger
def main(request):
    print("requset = ",request)
    # return HttpResponse("Hello, I'm Pyburger.")
    return render(request, "main.html")


def burger_list(request):
	print("requset = ",request)
	burgers = Burger.objects.all()
	print("The list of all burgers:",burgers)

	context = {
            "burgers": burgers
	}
	return render(request, "burger_list.html", context)

def burger_search(request):
	print("requset = ",request)
	print("requset.GET = ",request.GET)
	keyword = request.GET.get("keyword")
	print("keyword = ",keyword)

	if keyword is not None:
		burgers = Burger.objects.filter(name__contains=keyword)
	else:
		burgers = Burger.objects.none()

	print("burgers = ",burgers)
	context = {
            "burgers": burgers
	}
	return render(request, "burger_search.html", context)
