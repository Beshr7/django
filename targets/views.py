from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from targets.models import Target_model


def homepage(request):
    return render(
        request=request,
        template_name="main/home.html",
        context={"targets": Target_model.objects.all},
    )
