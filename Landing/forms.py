from django import forms
from .models import Space
from django.utils import timezone
from django.core.exceptions import ValidationError
from django import forms
from django.forms import TextInput, Select, FileInput
from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm, TextInput, EmailInput, Textarea
from blog.models.comment_models import Comment




def validate_date(date):
    if date < timezone.now():
        raise ValidationError("Date cannot be in the past.")

def validate_date_after(date):
    if date > timezone.now():
        raise ValidationError("Date cannot be in the future.")

class DateTimeLocalInput(forms.DateTimeInput):
    input_type = "datetime-local"
 
class DateTimeLocalField(forms.DateTimeField):
    input_formats = [
        "%Y-%m-%dT%H:%M:%S", 
        "%Y-%m-%dT%H:%M:%S.%f", 
        "%Y-%m-%dT%H:%M"
    ]
    widget = DateTimeLocalInput(format="%Y-%m-%dT%H:%M")


class ArticleCreateForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.filter(
                                      approved=True),
                                      empty_label="Select Category",
                                      widget=forms.Select(attrs=
                                                          {
                                                              "class": "form-control selectpicker",
                                                              "type": "text",
                                                              "name": "article-category",
                                                              "id": "articleCategory",
                                                              "data-live-search": "true"
                                                          }
                                      )
                                    )

    class Meta:

        # Article status constants
        DRAFTED = "DRAFTED"
        PUBLISHED = "PUBLISHED"

        # CHOICES
        STATUS_CHOICES = (
            (DRAFTED, 'Draft'),
            (PUBLISHED, 'Publish'),
        )

        model = Article
        fields = ["title", "category", "image", "image_credit", "body", "tags", "status"]
        widgets = {
            'title': TextInput(attrs={
                                     'name': "article-title",
                                     'class': "form-control",
                                     'placeholder': "Enter Article Title",
                                     'id': "articleTitle"
                                     }),

            'image': FileInput(attrs={
                                        "class": "form-control clearablefileinput",
                                        "type": "file",
                                        "id": "articleImage",
                                        "name": "article-image"
                                      }

                               ),

            'image_credit': TextInput(attrs={
                'name': "image_credit",
                'class': "form-control",
                'placeholder': "Example: made4dev.com (Premium Programming T-shirts)",
                'id': "image_credit"
            }),

            'body': forms.CharField(widget=CKEditorWidget(config_name="default", attrs={
                       "rows": 5, "cols": 20,
                       'id': 'content',
                       'name': "article_content",
                       'class': "form-control",
                       })),

            'tags': TextInput(attrs={
                                     'name': "tags",
                                     'class': "form-control",
                                     'placeholder': "Example: sports, game, politics",
                                     'id': "tags",
                                     'data-role': "tagsinput"
                                     }),

            'status': Select(choices=STATUS_CHOICES,
                             attrs=
                             {
                                 "class": "form-control selectpicker",
                                 "name": "status", "type": "text",
                                 "id": "articleStatus",
                                 "data-live-search": "true",
                                 "title": "Select Status"
                             }
                             ),
        }


class ArticleUpdateForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.filter(
                                      approved=True),
                                      empty_label="Select Category",
                                      widget=forms.Select(attrs=
                                                          {
                                                              "class": "form-control selectpicker",
                                                              "type": "text",
                                                              "name": "article-category",
                                                              "id": "articleCategory",
                                                              "data-live-search": "true"
                                                          }
                                      )
                                    )

    class Meta:
        # Article status constants
        DRAFTED = "DRAFTED"
        PUBLISHED = "PUBLISHED"

        # CHOICES
        STATUS_CHOICES = (
            (DRAFTED, 'Draft'),
            (PUBLISHED, 'Publish'),
        )

        model = Article
        fields = ["title", "category", "image", "image_credit", "body", "tags", "status"]
        widgets = {
            'title': TextInput(attrs={
                'name': "article-title",
                'class': "form-control",
                'placeholder': "Enter Article Title",
                'id': "articleTitle"
            }),

            'image_credit': TextInput(attrs={
                'name': "image_credit",
                'class': "form-control",
                'placeholder': "Example: made4dev.com (Premium Programming T-shirts)",
                'id': "image_credit"
            }),

            'status': Select(choices=STATUS_CHOICES,
                             attrs=
                             {
                                 "class": "form-control selectpicker",
                                 "name": "status", "type": "text",
                                 "id": "articleStatus",
                                 "data-live-search": "true",
                                 "title": "Select Status"
                             }
                             ),
            'body': forms.CharField(widget=CKEditorWidget(config_name="default", attrs={
                       "rows": 5, "cols": 20,
                       'id': 'content',
                       'name': "article_content",
                       'class': "form-control",
                       })),

            'image': FileInput(attrs={
                "class": "form-control clearablefileinput",
                "type": "file",
                "id": "articleImage",
                "name": "article-image",
            }

            ),

        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment', ]
        widgets = {
            'name': TextInput(attrs={'aria-required': "true",
                                     'name': "contact-form-name",
                                     'class': "form-control",
                                     'placeholder': "Enter your name",
                                     'aria-invalid': "true"
                                     }),

            'email': EmailInput(attrs={'aria-required': "true",
                                       'name': "contact-form-email",
                                       'class': "form-control",
                                       'placeholder': "Enter your email",
                                       'aria-invalid': "true",
                                       }),

            'comment': Textarea(attrs={'name': "contact-form-message",
                                       'rows': "2",
                                       'class': "text-area-messge form-control",
                                       'placeholder': "Enter your comment",
                                       'aria - required': "true",
                                       'aria - invalid': "false"
                                       }),
        }

