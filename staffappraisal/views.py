# from staffappraisal.models import AppraiseeComment
from django.urls.base import reverse
from django.views.generic.edit import UpdateView
from staffappraisal.models import AppraiseeComment, AppraiserAndAppraiseeAgreement, AppraiserComment, Competence, Performance, Profile, VcComment
from staffappraisal.forms import AssessmentForm, CommentForm, CommentvcForm, CompetenceForm, CommentForm,AppraiserForm, PerformanceForm, ProfileForm
from django.db import reset_queries
from django.forms.forms import Form
from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, DetailView, ListView

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib import messages
import datetime

# Calling the first page
# class LoginView(TemplateView):
#     template_name = "auth/login.html"

def LoginView(request):
    if request.user.is_authenticated:
        return redirect("staff:index")
    else:
         if request.method=="POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("staff:index")
         return render(request, "auth/login.html")

def LogoutView(request):
    auth.logout(request)
    return redirect("staff:login")


class RegisterView(TemplateView):
    template_name = "auth/register.html"


class ViewUsers(TemplateView):
    template_name = "users/users.html"

class ViewList(TemplateView):
    template_name = "supervisor/appraiselist.html"



class Profiles(TemplateView):
    template_name= "alluser/profile.html"

class SuperandApprai(TemplateView):
    template_name= "users/bothforhr.html"

    def get_context_data(self, **kwargs):
        context = super(SuperandApprai, self).get_context_data(**kwargs)
        context['lists-selected']=Competence.objects.filter(user=self.request.user)
        return context

class IndexView(TemplateView):
    template_name = "users/index.html"


def LoginSystem(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        return redirect("staff:index")
    else:
        return render(request, "auth/login.html")


def Register(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        user=User(
                first_name=firstname,
                last_name=lastname,
                email=email,
                username=username,
                )
        if password1 == password:
            user.set_password(password)

            a = user.save()
            return redirect("staff:login")
    return render(request, "auth/register.html")


class CompetenceUpdateView(UpdateView):
    model = Competence
    form_class=CompetenceForm
    template_name = "users/competence_update_form.html"
    success_url='/'

# def AppraiseeCommentUpdateView(request, pk):
#     obj = AppraiseeComment.objects.filter(competence__id =pk)
#     # model = AppraiseeComment
#     form=CommentForm()
#     return render(request, "users/comment_update_form.html", {'objects':obj, 'form':form})

# def UpdateAppraiseeComment(request, pk):
#     if request.method == 'POST':
#         app =AppraiseeComment.objects.get(pk=pk)
#         form = CommentForm(request.POST, instance=app)
#         if form.is_valid():
#             form.save()
#         return redirect('/')

class AppraiseeCommentUpdate(UpdateView):
    model = AppraiseeComment
    form_class=CommentForm
    template_name = "users/comment_update_form.html"
    success_url='/'


# class AppraiserAndAppraiseeAgreementView(UpdateView):
#     model = AppraiserAndAppraiseeAgreement
#     form_class=AssessmentForm
#     template_name = "users/assessment_update_form.html"

#     success_url='/'


def AppraiserAndAppraiseeAgreementView(request, pk):
    my_objects = AppraiserAndAppraiseeAgreement.objects.filter(competence__id =pk)
    form = AssessmentForm()
    return render(request, "users/assessment_update_form.html",  {'objects':my_objects, 'form':form})


def UpdateAppraiserAndAppraiseeAgreement(request, pk):
    my_objects = AppraiserAndAppraiseeAgreement.objects.get(pk =pk)
    if request.method == 'POST':
        app =AppraiserAndAppraiseeAgreement.objects.get(pk=pk)
        form = AssessmentForm(request.POST, instance=app)
        if form.is_valid():
            fm = form.save()
    return redirect('/update_assessment/'+str(my_objects.competence.pk))

# class ActionUpdate(UpdateView):
#     model = Performance
#     form_class=PerformanceForm
#     template_name = "users/action.html"
#     success_url='/'

from django.db.models.functions import Extract
def CompentenceCreateView(request):
    form = CompetenceForm()
    dat = datetime.datetime.now()
    month = dat.month
    print(month)
    # compent_check_1 = Competence.objects.filter(user=request.user, submitted_on__month=month)
    compent_check_1 = Competence.objects.annotate(start_year=Extract('submitted_on', 'month')).filter(user=request.user)
    print(compent_check_1)
    if compent_check_1.count() > 0:
        return redirect('update_compentence/'+str(compent_check_1[0].pk))
    if request.method == 'POST':
        form = CompetenceForm(request.POST)
        if form.is_valid():
            fm = form.save(commit = False)
            fm.user = request.user
            fm.save()
            return redirect('/as/'+str(fm.pk)) #localhost/as/7

    return render(request, 'users/competence.html', {'form':form})

class SuccessView(TemplateView):
    template_name='users/success.html'


class CommentView(CreateView):
    model = AppraiseeComment
    form_class = CommentForm
    template_name= 'users/comments.html'
    success_url="/success"
    
    def form_valid(self, form):
        compentence =get_object_or_404(Competence, pk = self.kwargs.get('pk'))
        form.instance.competence=compentence
        return super().form_valid(form)

class CommentappView(CreateView):
    model = AppraiserComment
    form_class = AppraiserForm
    template_name = 'supervisor/commentsuper.html'
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class CommentvcView(CreateView):
    model = VcComment
    form_class = CommentvcForm
    template_name = 'vc/commentvc.html'
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class ProfileView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'alluser/profile.html'
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class PerformanceView(CreateView):
    model = Performance
    form_class = PerformanceForm
    template_name = 'users/action.html'
    def get_success_url(self):
        # pk = self.kwargs['pk']
        return reverse("staff:act", kwargs = {'pk':self.kwargs['pk']}) 

    def form_valid(self, form):
        compentence =get_object_or_404(Competence, pk = self.kwargs.get('pk'))
        form.instance.competence=compentence
        # form.instance.user=self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['performances'] = Performance.objects.filter(competence__id=self.kwargs.get('pk'))
        return context
        
def AssessmentView(request, pk):
    competence =  get_object_or_404(Competence, pk=pk)
    asses = AppraiserAndAppraiseeAgreement.objects.filter(competence=competence).count()
    form = AssessmentForm()
    if request.method == 'POST':
        form = AssessmentForm(request.POST)
        if form.is_valid():
            fm = form.save(commit = False)
            fm.competence = competence
            fm.save()
            return redirect('/as/'+str(competence.pk)) #localhost/as/7
    return render(request, 'supervisor/assessment.html', {'form':form, 'competence':competence, 'assess':asses})

# AssessmentView(request)
# class AssessmentView(CreateView):
#     model = AppraiserAndAppraiseeAgreement
#     form_class = AssessmentForm
#     template_name = 'supervisor/assessment.html'
#     def form_valid(self, form):
#         form.instance.user=self.request.user
#         return super().form_valid(form)

class ListCompetenceView(ListView):
    model = Competence
    context_object_name = 'competences'
    template_name='supervisor/appraiselist.html'
    
    def get_queryset(self):
        """
            Return only the compentences where the currently logged in user is the head
        """
        queryset = Competence.objects.filter(user__profile__department__faculty__faculty_head=self.request.user)
        return queryset

"""
    Fetching details using the DetailView
"""
class AllDetailView(DetailView):
    model = Competence
    template_name='supervisor/detail.html'

    def form_valid(self, form):
        comp = get_object_or_404(Competence,pk = self.kwargs.get('pk'))
        return comp

class AllDetailViewapp(DetailView):
    model = Competence
    # form_class=CompetenceForm
    context_object_name="details"
    template_name = "supervisor/detail.html"

    