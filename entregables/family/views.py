from django.shortcuts import render
from django.http import HttpResponse

from family.models import Family

def add_family_member(request):
    new_family_member = Family.objects.create(name="Magali", last_name="Rios", age=30, is_adult=True)
    print(new_family_member)
    return HttpResponse("Se agrego el familiar")

def list_family(request):
    all_members = Family.objects.all
    context = {
        "family_member":all_members
    }
    return render(request, "family_list.html", context=context)