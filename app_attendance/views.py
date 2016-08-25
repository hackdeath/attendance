from django.http      import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms           import UploadFileForm
from .process_file    import *
from datetime         import timedelta

def index(request):
    form = UploadFileForm()
    return render(request, 'app_attendance/index.html', {'form': form})
