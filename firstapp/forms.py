from django import forms
PHOTOS = (
    ('front', 'Общий вид'),
    ('1floor', '1 этаж'),
    ('2floor', '2 этаж'),
)

class UserForm(forms.Form):
    name = forms.CharField(label="Имя")
    surname = forms.CharField(label="Фамилия")
    email = forms.EmailField(label="Email адрес")
    check1 = forms.BooleanField(label="Прикрепить к документу права и обязанности сторон", required=False)
    check2 = forms.BooleanField(label="Прикрепить к документу ТЗ", required=False)
    photos = forms.MultipleChoiceField(label = "Прикрепить фото", required=False, widget=forms.CheckboxSelectMultiple, choices=PHOTOS)
