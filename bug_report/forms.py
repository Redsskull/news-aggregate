from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import BugReport


class BugReportForm(forms.ModelForm):
    # form based on the bug report model
    class Meta:
        model = BugReport
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit Report'))
