from django import forms

class TeeTimeBookingForm(forms.Form):
    tee_time = forms.DateTimeField(label='Tee Time')