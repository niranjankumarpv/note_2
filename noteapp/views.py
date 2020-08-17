from django.shortcuts import render
from noteapp.models import Note,Note_Detail
# Create your views here.

def index(request):
    notes_list = Note.objects.all()
    return render(request, "noteapp/index.html", {'notes_list': notes_list})

def detail(request, note_id):
    # if request.method == "POST":
    #     detail_id = int(request.POST.get("note_detail"))
    note = Note.objects.get(id=note_id)
    return render(request, "noteapp/detail.html", {'note': note})

def edit(request, note_id):
    if request.method == "POST":
        if request.POST.get('des'):

            content = Note_Detail()
            content.id = Note.objects.get(id=2)
            # content.note_id = Note_Detail.objects.get(id=note_id)
            content.description= request.POST.get('des')
            print(content.description)
            content.save()
            note = Note.objects.get(id=note_id)
            return render(request, "noteapp/edit.html", {'note': note})
    else:
        note = Note.objects.get(id=note_id)
        return render(request, "noteapp/edit.html", {'note': note})
    # return render(request, "noteapp/edit.html")