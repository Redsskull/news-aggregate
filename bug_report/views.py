from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import BugReportForm

def submit_bug_report(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bug_report:confirmation') 
    else:
        form = BugReportForm()

    return render(request, 'submit_bug_report.html', {'form': form})

def confirmation(request):
    return render(request, 'confirmation.html')

