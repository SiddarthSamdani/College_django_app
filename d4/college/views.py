from django.shortcuts import render
from .models import Notice, Profile, Question
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def home(req):
    return render(req, 'index.html')


@method_decorator(login_required, name='dispatch')
class NoticeListView(ListView):
    model = Notice

    def get_queryset(self):
        si = self.request.GET.get('si')
        if si == None:
            si = ""
        if self.request.user.is_superuser:
            return Notice.objects.filter(Q(subject__icontains = si) | Q(msg__icontains = si)).order_by("-id")
        else:
            return Notice.objects.filter(Q(branch=self.request.user.profile.branch)|Q(branch__isnull=True))\
                .filter(Q(subject__icontains = si) | Q(msg__icontains = si)).order_by("-id")


@method_decorator(login_required, name='dispatch')
class NoticeDetailView(DetailView):
    model = Notice


@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ["branch", "sem", "marks_10", "marks_12", "marks_aggr", "myimg", "myresume", "skills", "rn"]


@method_decorator(login_required, name='dispatch')
class QuestionCreate(CreateView):
    model = Question
    fields = ["subject", "msg"]