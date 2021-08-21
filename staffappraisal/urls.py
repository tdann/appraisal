from django.urls import path

from . import views


app_name = 'staff'
urlpatterns = [
    path('', views.LoginView, name='login'), #localhost:8000 
    path('register', views.RegisterView.as_view(), name='register'), #localhost:8000/register
    path('users', views.ViewUsers.as_view(), name='users'), #localhost:8000/register
    path('list', views.ListCompetenceView.as_view(), name='list'), #localhost:8000/list
    path('comp', views.CompentenceCreateView, name='comp'),
    path('comm/<pk>', views.CommentView.as_view(), name='comm'),
    path('update_compentence/<pk>', views.CompetenceUpdateView.as_view(), name='update_compentence'),
    path('update_com/<pk>', views.AppraiseeCommentUpdate.as_view(), name='update_com'),
    path('update_assessment/<pk>', views.AppraiserAndAppraiseeAgreementView, name='update_assessment'),
    path('update_assess/<pk>', views.UpdateAppraiserAndAppraiseeAgreement, name='update_assess'),
    path('success', views.SuccessView.as_view(), name='success'),
    path('coma', views.CommentappView.as_view(), name='coma'),
    path('comv', views.CommentvcView.as_view(), name='comv'),
    path('prof', views.ProfileView.as_view(), name='prof'),
    path('act/<pk>', views.PerformanceView.as_view(), name='act'),
    path('as/<pk>', views.AssessmentView, name='as'),
    path('both', views.SuperandApprai.as_view(), name='both'),
    # path('profile', views.Profiles.as_view(), name='profile'),
    path('home' , views.IndexView.as_view(), name='index'),
    path('logout', views.LogoutView, name='logout'),
    path('add_user', views.Register, name='add_user'),
    path('detail/<pk>', views.AllDetailViewapp.as_view(), name='detail'),
    path('agreement/<pk>', views.AgreementView.as_view(), name='agreement'),
    path('edit/<pk>', views.EditOutput, name='editing'),
    path('editi/<pk>', views.UpdateOutputall.as_view(), name='editi'),
    

]