from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Ism",
        help_text="Ismingizni kiriting.",
        widget=forms.TextInput(attrs={
            'placeholder': 'Ismingiz',
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
        })
    )
    email = forms.EmailField(
        label="Email",
        help_text="Email manzilingizni kiriting.",
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email',
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
        })
    )
    comment = forms.CharField(
        label="Izoh",
        help_text="Kamida 10 ta harf va 3 ta so‘z bo‘lishi kerak.",
        widget=forms.Textarea(attrs={
            'placeholder': 'Izohingizni kiriting...',
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            'rows': 4,
        })
    )

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.strip():
            raise forms.ValidationError("Ism bo‘sh bo‘lishi mumkin emas.")
        return name

    def clean_comment(self):
        comment = self.cleaned_data.get('comment')
        if len(comment) <= 10:
            raise forms.ValidationError("Izoh kamida 10 ta harfdan iborat bo‘lishi kerak.")
        if len(comment.split()) < 3:
            raise forms.ValidationError("Izoh kamida 3 ta so‘z bo‘lishi kerak.")
        return comment
