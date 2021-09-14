# from staffappraisal.models import AppraiseeComment
from django.http.response import HttpResponse
from django.urls.base import reverse, reverse_lazy
from staffappraisal.models import AppraiseeComment, AppraiserAndAppraiseeAgreement, AppraiserComment, Competence, Performance, Profile, VcComment
from staffappraisal.forms import AssessmentForm, AssessmentFormSuper, CommentForm, CommentvcForm, CompetenceForm, CommentForm,AppraiserForm, PerformanceForm, ProfileForm
from django.db import reset_queries
from django.forms.forms import Form
from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.db.models.functions import Extract
from django.db import IntegrityError


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

class AppraiseeCommentUpdate(UpdateView):
    model = AppraiseeComment
    form_class=CommentForm
    template_name = "users/comment_update_form.html"
    success_url='/'

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
    template_name = 'supervisor/action.html'
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


class ListCompetenceView(ListView):
    model = Competence
    context_object_name = 'competences'
    template_name='supervisor/appraiselist.html'
    
    def get_queryset(self):
        """
            Return only the competences where the currently logged in user is the head
        """
        queryset = Competence.objects.filter(user__profile__department__faculty__faculty_head=self.request.user,appraiseecomment__appraisercomment__comment_justification__isnull=True)
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

class CommentappView(CreateView):
    model = AppraiserComment
    form_class = AppraiserForm
    template_name = 'supervisor/commentsuper.html'
    success_url='/success'
    
    def form_valid(self, form):
        comm1 = AppraiseeComment.objects.get(competence__id = self.kwargs['pk'])
        form.instance.appraisee_comment=comm1
       
        try:
             form.instance.super_visor=self.request.user
             return super().form_valid(form)
    # code that produces error
        except IntegrityError as e:
            # return render("auth/register.html", {"message": e.message})
            return HttpResponse("ERROR: Comment already exists!")

class AgreementView(CreateView):
    model = AppraiserAndAppraiseeAgreement
    form_class = AssessmentFormSuper
    template_name = 'supervisor/last.html'
    def get_success_url(self):
        return reverse("staff:agreement", kwargs = {'pk':self.kwargs['pk']}) 

    def form_valid(self, form):
        assess =get_object_or_404(AppraiserAndAppraiseeAgreement, pk = self.kwargs.get('pk'))
        form.instance.appraiserandappraiseeagreement=assess
        # form.instance.super_visor=self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['agreements'] = AppraiserAndAppraiseeAgreement.objects.filter(competence__id=self.kwargs.get('pk'))
        return context
def EditOutput(request,pk):
    disp = AppraiserAndAppraiseeAgreement.objects.get(pk=pk)
    return render(request,"supervisor/editlast.html",{"outputing":disp})
class UpdateOutputall(UpdateView):
    model = AppraiserAndAppraiseeAgreement
    form_class = AssessmentFormSuper
    template_name = "supervisor/editlast.html"

    def form_valid(self, form):
        form.instance.super_visor = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        comp_id = self.object.competence.pk
        return reverse_lazy("staff:agreement", kwargs = {'pk':comp_id})

class ListCompetenceVCView(ListView):
    model = Competence
    context_object_name = 'competences'
    template_name='vc/appraiserlist.html'
    
    def get_queryset(self):
        """
            Return all the competences where signed by the supervisor
        """
        queryset = Competence.objects.filter(appraiseecomment__appraisercomment__comment_justification__isnull=False)
        # queryset = Competence.objects.filter(appraiseecomment__appraisercomment__comment_justification__isnull=False, appraiseecomment__appraisercomment__vccomment__vc_comment__isnull=True)
        return queryset

class AllDetailViewVC(DetailView):
    model = Competence
    # form_class=CompetenceForm
    context_object_name="details"
    template_name = "vc/details.html"

class CommentvcView(CreateView):
    model = VcComment
    form_class = CommentvcForm
    template_name = 'vc/commentvc.html'
    success_url='/success'

    def form_valid(self, form):
        comvc = Competence.objects.get(id=self.kwargs['pk'])
        form.instance.appraiser_comment=comvc
        try:
             form.instance.user=self.request.user
             return super().form_valid(form)
    # code that produces error
        except IntegrityError as e:
            # return render("auth/register.html", {"message": e.message})
            return HttpResponse("ERROR: Comment already exists!")