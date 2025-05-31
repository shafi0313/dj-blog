from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm


# from django.http import HttpResponseRedirect
# from django.urls import reverse
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
# def create_post(request):
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("post_list")  # আপনার ইউআরএল অনুযায়ী ঠিক করুন
#     else:
#         form = PostForm()
#     return render(request, "post_form.html", {"form": form})


class PostListView(ListView):
    model = Post
    template_name = "posts/list.html"
    context_object_name = 'posts'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts/create.html"
    success_url = reverse_lazy("posts:list")
