from django.db.models import fields
from staffappraisal import models
from staffappraisal.models import AppraiseeComment, AppraiserAndAppraiseeAgreement, Competence, AppraiserComment, Performance, Profile,VcComment
from django import forms

class CompetenceForm(forms.ModelForm):
    class Meta:
        model=Competence
        exclude = ['user']
        widgets ={
            'comment_professional_skill':forms.Textarea(attrs={'cols': 10, 'rows': 3}),
            'comment_planning':forms.Textarea(attrs={'cols': 10, 'rows': 3}),
            'comment_leadership':forms.Textarea(attrs={'cols': 10, 'rows': 3}),
            'comment_decision_making':forms.Textarea(attrs={'cols': 10, 'rows': 3}),
            'comment_innovation':forms.Textarea(attrs={'cols': 10, 'rows': 3}),
            'comment_teamwork':forms.Textarea(attrs={'cols': 10, 'rows': 3}),
            'comment_human_resource':forms.Textarea(attrs={'cols': 10, 'rows': 3}),
            'comment_financial_management':forms.Textarea(attrs={'cols': 10, 'rows': 3}),
            'comment_other_resource_mananagement':forms.Textarea(attrs={'cols': 10, 'rows': 3}),
            'comment_result_orientation':forms.Textarea(attrs={'cols': 10, 'rows': 3}),
            'comment_client_care':forms.Textarea(attrs={'cols': 10, 'rows': 3}),
            'comment_communication':forms.Textarea(attrs={'cols': 10, 'rows': 3}),
            'comment_integrity':forms.Textarea(attrs={'cols': 10, 'rows': 3}),
            'comment_time_management':forms.Textarea(attrs={'cols': 10, 'rows': 3}),
            'comment_loyalty':forms.Textarea(attrs={'cols': 10, 'rows': 3}),
            # 'other_competence':forms.Textarea(attrs={'cols': 10, 'rows': 3}),
            'comment_other_competence':forms.Textarea(attrs={'cols': 10, 'rows': 3}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model= AppraiseeComment
        exclude = ['competence']
        widgets = {
            'effectiveness':forms.Textarea(attrs={'cols': 10, 'rows': 3}),
            'assistance':forms.Textarea(attrs={'cols': 10, 'rows': 3, 'resize':'none'}),
            'aspiration':forms.Textarea(attrs={'cols': 10, 'rows':3}),
            'any_comment':forms.Textarea(attrs={'cols': 10, 'rows':3}),
        }

class AppraiserForm(forms.ModelForm):
    class Meta:
       model = AppraiserComment 
       exclude = ['appraisee_comment','super_visor']

class CommentvcForm(forms.ModelForm):
    class Meta:
       model = VcComment
       exclude = ['appraisee_comment','user']



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['roles']

class PerformanceForm(forms.ModelForm):
    class Meta:
        model = Performance
        exclude = ['competence']

class AssessmentForm(forms.ModelForm):
    class Meta:
        model = AppraiserAndAppraiseeAgreement
        exclude = ['competence', 'supervisor_rating', 'super_visor', 'comments_on_performance']

class AssessmentFormSuper(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(AssessmentFormSuper, self).__init__(*args, **kwargs)
       self.fields['key_outputs'].widget.attrs['readonly'] = True
       self.fields['performance_indicator'].widget.attrs['readonly'] = True
       self.fields['performance_target'].widget.attrs['readonly'] = True
       self.fields['self_rating'].widget.attrs['readonly'] = True
    class Meta:
        model = AppraiserAndAppraiseeAgreement
        exclude = ['competence','super_visor']

        