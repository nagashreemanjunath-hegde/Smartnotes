from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Notes 
from django.views.generic import ListView,DetailView

# Create your views here from function based--
# def list(request):
#     all_notes=Notes.objects.all()
#     return render(request,'notes/notes_list.html',{'notes':all_notes})

# def detail(request, pmk):
#     try:
#         note=Notes.objects.get(pk=pmk)
        
#     except Notes.DoesNotExist:
#         raise Http404("Notes doesn't exist")
    
#     return render(request,'notes/notes_detail.html',{'notes':note})

class NotesListView(ListView):
    model = Notes
    content_object_name = "notes"
    template_name = "notes/notes_list.html"


class NotesDetailView(DetailView):
    model = Notes
    context_object_name ="notes"
    template_name = "notes/notes_detail.html"