from django import forms
from .models import Status


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['user', 'content', 'image']

    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data['content']

        if len(content) < 2:
            raise forms.ValidationError('Content is too short')

        if len(content) > 240:
            raise forms.ValidationError('Content is too long')
        return content

    def clean(self, *args, **kwargs):
        data = self.cleaned_data

        content = data.get('content', None)
        if content == '':
            content = None

        image = data.get('image', None)
        if image == '':
            image = None

        if content is None and image is None:
            raise forms.ValidationError('Content or Image is required!')

        return super().clean(*args, **kwargs)
