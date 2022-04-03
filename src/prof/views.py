from django.shortcuts import render
from django.views.generic import ListView, CreateView
from  .models import compte, CV_Text
import PyPDF2
import textract


class CompteList(ListView):
    model = compte
    context_object_name = "compte"
    template_name = "prof/prof_list.html"

class CompteCreate(CreateView, ListView):
    context = []
    model = compte
    template_name = "prof/Compte_Add.html"
    fields = ['nom', 'prenom', 'age', 'profile', 'lettre_de_motivation', 'CV']

    def get_context_data(self, **kwargs):
        kwargs['comptes'] = compte.objects.all()
        return super(CompteCreate, self).get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        pdfReader = PyPDF2.PdfFileReader(request.FILES['CV'])
        num_pages = pdfReader.numPages
        count = 0
        text = ""
        # The while loop will read each page.
        while count < num_pages:
            pageObj = pdfReader.getPage(count)
            count += 1
            text += pageObj.extractText()
        if text != "":
            text = text
        CV_Text.objects.create(TextCV=text)
        return super(CompteCreate, self).post(self, request, *args, **kwargs)




