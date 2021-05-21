from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Llst, item
from .forms import CreateNewList

# Create your views here.


def z(response, id):
    ls = Llst.objects.get(id=id)
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "chicked":
                    item.cmpl = True
                else:
                    item.cmpl = False

                item.save()
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")

            if len(txt) > 2:
                ls.item_set.create(text=txt, cmpl=False)
            else:
                print("invalid")

    return render(response, "b/3.html", {"ls": ls})


def home(response):
    return render(response, "b/2.html", {})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = Llst(name=n)
            t.save()
        return HttpResponseRedirect("/%i" % t.id)
    else:
        form = CreateNewList()
    return render(response, "b/4create.html", {"form":  form})
