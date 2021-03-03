from django import forms
from . import models

RATE= [(x,x) for x in range(0, 6)]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = (
            "review",
            "rate",
        )
        widgets = {
            'review': forms.Textarea(attrs={'id': "review", 'name': "review",  'cols': 90, 'rows': 10, 'placeholder': "상세 내용을 입력해주세요."}),
            'rate': forms.Select(choices=RATE, attrs={'class': "rate", 'id': "rate", 'name': "rate", 'size': "1", "required": 'true', "autofocus": 'true'})
        }

    def save(self):
        review = super().save(commit=False)
        return review

    labels = {
                'review': "리뷰",
                'rate': "점수",
        }