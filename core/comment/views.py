from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponseForbidden

from .forms import CommentForm
from .models import Comment

# Create your views here.


class CommentFormView(SingleObjectMixin, FormView):

    template_name = 'blog/post_detail.html'
    form_class = CommentForm
    success_url = "#"
    model = Comment
    def post(self, request, *args, **kwargs):
        """
        Posts the comment only if the user is logged in.
        """
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
