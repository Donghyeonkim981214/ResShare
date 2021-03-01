from django import forms
from . import models as res_model

class RestaurantForm(forms.ModelForm):
    """Form definition for Restaurant."""

    class Meta:
        """Meta definition for Restaurantform."""

        model = res_model.Restaurant
        fields = ('category',
                'restaurant_name',
                'restaurant_link',
                'restaurant_address',
                'restaurant_phone',
                'restaurant_content',
                )
        
        widgets = {
            'category': forms.Select(attrs={'class': "resCategory", 'id': "resCategory", 'name': "resCategory", 'size': "1", "required": 'true', "autofocus": 'true'}),
            'restaurant_name': forms.TextInput(attrs={'id': "resTitle", 'name': "resTitle", 'class': "form-control", 'placeholder': "맛집 이름을 입력해주세요.", 'aria-describedby': "sizing-addon2"}),
            'restaurant_link': forms.TextInput(attrs={'id':"resLink", 'name': "resLink", 'class': "form-control", 'placeholder': "관련 링크를 입력해주세요.", 'aria-describedby': "sizing-addon2"}),
            'restaurant_content': forms.Textarea(attrs={'id': "resContent", 'name': "resContent",  'cols': 90, 'rows': 10, 'placeholder': "상세 내용을 입력해주세요."}),
            'restaurant_address': forms.TextInput(attrs={'id': "resLoc", 'name': "resLoc", 'class': "form-control", 'placeholder': "주소를 입력해주세요.", 'aria-describedby': "sizing-addon2"}),
            'restaurant_phone': forms.TextInput(attrs={'id': "resPhone", 'name': "resLoc", 'class': "form-control", 'placeholder': "전화번호를 입력해주세요.", 'aria-describedby': "sizing-addon2"}),
        }

        labels = {
                'category': "카테고리",
                'restaurant_name': "맛집 이름",
                'restaurant_link': "관련 링크",
                'restaurant_content': "상세 내용",
                'restaurant_address': "주소",
                'restaurant_phone': "전화번호",
        }
        
class CategoryForm(forms.ModelForm):
    """Form definition for Category."""

    class Meta:
        """Meta definition for Categoryform."""

        model = res_model.Category

        fields = ('category_name',)

        widgets = {
            'category_name': forms.TextInput(attrs={'id': "categoryName", 'name': "categoryName", 'class': "form-control", 'placeholder': "추가할 카테고리명을 입력해주세요.", 'style': "width:650px; float:right; border-radius:4px;"}),
        }
        
 