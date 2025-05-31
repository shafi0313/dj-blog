from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "author", "image", "is_published"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "শিরোনাম লিখুন",
                    "id": "title",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "বিস্তারিত লিখুন",
                    "rows": 5,
                    "id": "content",
                }
            ),
            "author": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "লেখকের নাম লিখুন",
                    "id": "author",
                }
            ),
            "image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "id": "image",
                }
            ),
            "is_published": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                    "id": "is_published",
                }
            ),
        }
        labels = {
            "title": "শিরোনাম",
            "content": "বিস্তারিত",
            "author": "লেখক",
            "image": "ছবি (ঐচ্ছিক)",
            "is_published": "প্রকাশিত",
        }
        # labels = {
        #     "title": "শিরোনাম",
        #     "content": "বিস্তারিত",
        #     "author": "লেখক",
        #     "image": "ছবি (ঐচ্ছিক)",
        #     "is_published": "প্রকাশিত",
        # }
        # help_texts = {
        #     "title": "শিরোনামটি কমপক্ষে ৫ অক্ষরের হতে হবে।",
        #     "content": "আপনার পোস্টের বিস্তারিত লিখুন।",
        #     "author": "লেখকের নাম লিখুন।",
        #     "image": "ছবি আপলোড করুন (ঐচ্ছিক)।",
        # }
