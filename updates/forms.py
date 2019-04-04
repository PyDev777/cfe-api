from django import forms
from updates.models import Update as UpdateModel


class UpdateModelForm(forms.ModelForm):
    class Meta:
        model = UpdateModel
        fields = ['user', 'content', 'image']

    def clean(self, *args, **kwargs):

        data = self.cleaned_data
        print()
        print('self.cleaned_data =', data)
        print()
        content = data.get('content', None)
        image = data.get('image', None)
        if not content and not image:
            raise forms.ValidationError('Warning: Content or Image is required!')
        return super().clean(*args, **kwargs)
