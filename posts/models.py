from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError


# কাস্টম ম্যানেজার: শুধুমাত্র প্রকাশিত পোস্ট ফেরত দেয়
class PostManager(models.Manager):
    def published(self):
        return self.filter(is_published=True)


class Post(models.Model):
    # পোস্টের শিরোনাম: এটি একটি আবশ্যিক (required) ফিল্ড এবং সর্বোচ্চ দৈর্ঘ্য ২০০ অক্ষর
    title = models.CharField(blank=False, null=False, max_length=200)

    # SEO এবং URL বান্ধব ইউনিক স্লাগ; যদি না দেওয়া হয় তাহলে শিরোনাম থেকে স্বয়ংক্রিয়ভাবে তৈরি হবে
    slug = models.SlugField(unique=True, blank=True)

    # পোস্টের বিষয়বস্তু সংরক্ষণের জন্য ব্যবহৃত টেক্সট ফিল্ড
    content = models.TextField()

    # লেখকের নাম: সর্বোচ্চ ১০০ অক্ষর; এটি একটি আবশ্যিক ফিল্ড
    author = models.CharField(max_length=100)

    # ঐচ্ছিক ছবি সংযুক্ত করার জন্য ফিল্ড; ছবি না থাকলেও চলবে
    image = models.ImageField(upload_to="images/", blank=True, null=True)

    # পোস্ট তৈরি হওয়ার তারিখ ও সময়; স্বয়ংক্রিয়ভাবে সেট হয়
    created_at = models.DateTimeField(auto_now_add=True)

    # সর্বশেষ হালনাগাদের সময়; প্রতিবার সংরক্ষণের সময় স্বয়ংক্রিয়ভাবে আপডেট হয়
    updated_at = models.DateTimeField(auto_now=True)

    # পোস্টটি প্রকাশিত হয়েছে কিনা তা বোঝাতে ব্যবহৃত বুলিয়ান ফিল্ড
    is_published = models.BooleanField(default=True)

    # কাস্টম ম্যানেজার যুক্ত করা হয়েছে
    objects = PostManager()

    # ডেটা ভ্যালিডেশন: শিরোনাম ৫ অক্ষরের কম হলে এরর প্রদর্শন করবে
    def clean(self):
        if len(self.title) < 5:
            raise ValidationError({"title": "শিরোনাম কমপক্ষে ৫ অক্ষরের হতে হবে।"})

    # মডেল অবজেক্টকে স্ট্রিং হিসেবে রূপান্তর করলে শিরোনাম দেখাবে
    def __str__(self):
        return self.title

    # সেভ করার আগে slug ফিল্ডটি যদি না থাকে তাহলে শিরোনাম থেকে তৈরি করা হবে

    def save(self, *args, **kwargs):
        # title থেকে slug বানানো হচ্ছে (URL-সুরক্ষিত ফর্মে)
        base_slug = slugify(self.title)
        slug = base_slug
        counter = 1

        # যদি slug আগেই থাকে, তাহলে শেষে -1, -2, ... যোগ করে ইউনিক করা হচ্ছে
        while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        # ইউনিক slug ফিল্ডে সেট করা হচ্ছে
        self.slug = slug

        # মডেল সেভ করার জন্য প্যারেন্ট মেথড কল করা হচ্ছে
        super().save(*args, **kwargs)
