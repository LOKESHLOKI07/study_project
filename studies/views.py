# studies/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Study
from .forms import StudyForm
import logging

logger = logging.getLogger(__name__)

def study_list(request):
    studies = Study.objects.all()
    return render(request, 'study_list.html', {'studies': studies})

def study_add(request):
    if request.method == 'POST':
        form = StudyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('study_list')
    else:
        form = StudyForm()
    return render(request, 'study_form.html', {'form': form})

def study_view(request, pk):
    study = get_object_or_404(Study, pk=pk)
    return render(request, 'study_view.html', {'study': study})

def study_edit(request, pk):
    study = get_object_or_404(Study, pk=pk)
    if request.method == 'POST':
        form = StudyForm(request.POST, instance=study)
        if form.is_valid():
            form.save()
            return redirect('study_list')
    else:
        form = StudyForm(instance=study)
    return render(request, 'study_form.html', {'form': form})

def study_delete(request, pk):
    study = get_object_or_404(Study, pk=pk)
    study.delete()
    return redirect('study_list')
