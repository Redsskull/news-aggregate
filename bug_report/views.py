from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import BugReportForm
from django.contrib import messages

def submit_bug_report(request):
    """
    View for submitting a bug report. allows user to create a new entry into the database.
    """
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Report submitted successfully. Thank you!')
            return redirect('home_page') 
    else:
        form = BugReportForm()
    return render(request, 'submit_bug_report.html', {'form': form})

# def confirmation(request):
#     messages.success(request, 'Report submitted successfully.')
#     return render(request, 'home_page.html')

