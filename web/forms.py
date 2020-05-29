from django import forms


class Contact(forms.Form):
    Nombre = forms.CharField(required=True, max_length=50,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '... ', }))
    Email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email@...', }))
    Telefono = forms.CharField(required=True, max_length=20,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '04141234567...', }))
    Mensaje = forms.CharField(required=True, max_length=150,
                                widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': '... ', }))

    def clean(self):
        Nombre = self.cleaned_data.get("Nombre")
        Email = self.cleaned_data.get("Email")
        Telefono = self.cleaned_data.get("Telefono")
        Mensaje = self.cleaned_data.get("Mensaje")

        return super(Contact, self).clean()
