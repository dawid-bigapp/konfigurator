from django import forms

WYMIARY = [
    (1, '1mb'),
    (2, '2mb'),
    (3, '3mb'),
    (4, '4mb'),
    (5, '5mb'),
]

class wymiaryOdcinek(forms.Form):
    wymiara = forms.CharField(label="Wymiar A:", widget=forms.Select(choices=WYMIARY))
    
class wymiaryL(forms.Form):
    wymiara = forms.CharField(label="Wymiar A:", widget=forms.Select(choices=WYMIARY))
    wymiarb = forms.CharField(label="Wymiar B:", widget=forms.Select(choices=WYMIARY))

class wymiaryU(forms.Form):
    wymiara = forms.CharField(label="Wymiar A:", widget=forms.Select(choices=WYMIARY))
    wymiarb = forms.CharField(label="Wymiar B:", widget=forms.Select(choices=WYMIARY))
    wymiarc = forms.CharField(label="Wymiar C:", widget=forms.Select(choices=WYMIARY))

class wymiaryProstokat(forms.Form):
    wymiara = forms.CharField(label="Wymiar A:", widget=forms.Select(choices=WYMIARY))
    wymiarb = forms.CharField(label="Wymiar B:", widget=forms.Select(choices=WYMIARY))
    wymiarc = forms.CharField(label="Wymiar C:", widget=forms.Select(choices=WYMIARY))
    wymiard = forms.CharField(label="Wymiar D:", widget=forms.Select(choices=WYMIARY))
    

class wymiaryPodwojneL(forms.Form):
    wymiara = forms.CharField(label="Wymiar A:", widget=forms.Select(choices=WYMIARY))
    wymiarb = forms.CharField(label="Wymiar B:", widget=forms.Select(choices=WYMIARY))
    wymiarc = forms.CharField(label="Wymiar C:", widget=forms.Select(choices=WYMIARY))
    wymiard = forms.CharField(label="Wymiar D:", widget=forms.Select(choices=WYMIARY))

class wymiarySufitSciana(forms.Form):
    wymiara = forms.CharField(label="Wymiar A:", widget=forms.Select(choices=WYMIARY))
    wymiarb = forms.CharField(label="Wymiar B:", widget=forms.Select(choices=WYMIARY))
