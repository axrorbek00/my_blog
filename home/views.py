from django.shortcuts import render, redirect
from .forms import PostCreateForm
from .models import PostModel
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin


def post_detail_views(request, id):
    post = PostModel.objects.get(id=id)

    hit_count = get_hitcount_model().objects.get_for_object(post)
    # hits = hit_count.hits
    hit_count_response = HitCountMixin.hit_count(request, hit_count)

    return render(request, 'main/detail.html', context={
        'post_id': post,
        'hit_count_object': hit_count_response
    })


def my_home_view(request):
    posts = PostModel.objects.all()
    return render(request, 'main/home.html', context={
        'posts': posts
    })


# Create your views here.

def creat_post_view(request):
    form = PostCreateForm()
    if request.method == 'POST':
        form = PostCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_psot = PostModel.objects.create(
                title=form.cleaned_data['title'],
                body=form.cleaned_data['body'],
                img=form.cleaned_data['img'],
                user=request.user
            )
            new_psot.save()
            return redirect('blog:my_home')
    return render(request, 'main/post_craet.html', context={
        'create_form': form
    })
