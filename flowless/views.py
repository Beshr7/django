from django.shortcuts import render
from flowless.models import Pressure_Reading

# Create your views here.


def flowlessPage(request):
    return render(
        request=request,
        template_name="main/home.html",
        context={"flowless": Pressure_Reading.objects.all},
    )
