import decimal
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.dispatch import receiver
from django.db.models.signals import post_save

from django.core.validators import MinValueValidator,MaxValueValidator
# from django.
# Create your models here.
# done
class Faculty(models.Model):
    class Meta:
        verbose_name ="Faculty"
        verbose_name_plural ="Faculties"

    faculty_name = models.CharField(max_length=100)
    faculty_head= models.ForeignKey(User, help_text="Head of the faculty responsible for confirmations",  on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.faculty_name


class Department(models.Model):
    faculty = models.ForeignKey(Faculty, verbose_name='Select the Faculty to which the department Belongs', on_delete=models.CASCADE)
    department_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.department_name


class Profile(models.Model):
    role =  [
        ("u", "User"),
        ("s", "Supervisor"),
        ("h", "Human Resource"),
        ("v", "Vice Chancellor"),
    ]

    sex = [
        ("F", "Female"),
        ("M", "Male"),
    ]

    terms = [
        ("pro", "Probation"),
        ("per", "Permanant"),
        ("cont","Contract")
    ]
    salary =[
        ("m2","M2"),
        ("m3","M3"),
        ("m4","M4"),
        ("m5","M5"),
        ("m6","M6"),
        ("m7","M7"),
        ("m8","M8"),
    ]
    roles = models.CharField(max_length=2, choices=role, default='u')
    job_title = models.CharField(max_length=50, null=True, blank=True)
    salary_scale = models.CharField(max_length=2, choices=salary, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    gender = models.CharField(max_length=2, choices=sex, blank=True, null=True)
    staff_dob = models.DateField(verbose_name='Staff date of birth', blank=True, null=True)
    f_appoi_date = models.DateField(verbose_name='Date of First Appointment', blank=True, null=True)
    s_appoi_date = models.DateField(verbose_name='Date of Latest Appointment', blank=True, null=True)
    terms_of_appoint = models.CharField(max_length=4, choices=terms, blank=True, null=True )
    photo = models.ImageField(upload_to ='staff_uploads', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,editable=False)

    def __str__(self) -> str:
        return self.user.get_full_name()


# class Competence(models.Model):
#     comps = [
#         ("profession_skill", "Professional Knowledge/ Skills"),
#         ("planning", "Planning, organizing and coordinating"),
#         ("leadership","Leadership"),
#         ("decision_making", "Decision making"),
#         ("innovation","Initiative & Innovation"),
#         ("team_work","Team work"),
#         ("human_resource","Human Resource Management:/Mentorship"),
#         ("fin_management","Financial management"),
#         ("o_resource_man","Management of other resources (equipment & facilities)"),
#         ("result_orientation","Result Orientation"),
#         ("client_care","Client Care"),
#         ("communication","Communication skills"),
#         ("integrity","Integrity"),
#         ("time","Time Management"),
#         ("loyalty","Loyalty")
#     ]
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     compentence_type = models.CharField(max_length=200, editable=True, choices=comps)
#     ranking = models.PositiveIntegerField(
#         validators=[MinValueValidator(decimal.Decimal(1)), MaxValueValidator(decimal.Decimal(5))]
#     )
#     current_date = models.DateField(auto_now=True)
#     comment = models.CharField(max_length=255)

#     def __str__(self):
#         return self.user.username


class Competence(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profession_skill = models.PositiveIntegerField(verbose_name="Professional Knowledge/ Skills",
        validators=[MinValueValidator(decimal.Decimal(1)), MaxValueValidator(decimal.Decimal(5))],
        blank=True,null=True
        )
    comment_professional_skill =models.TextField(max_length=400,  blank=True, null=True)
    planning = models.PositiveIntegerField(verbose_name="Planning, organizing and coordinating",
        validators=[MinValueValidator(decimal.Decimal(1)), MaxValueValidator(decimal.Decimal(5))],
        blank=True,null=True
    )
    comment_planning = models.TextField(max_length=400, blank=True,null=True)
    leadership = models.PositiveIntegerField(
        validators=[MinValueValidator(decimal.Decimal(1)), MaxValueValidator(decimal.Decimal(5))],
        blank=True,null=True
    )
    comment_leadership=models.TextField(max_length=400,blank=True,null=True)
    decision_making = models.PositiveIntegerField(
        validators=[MinValueValidator(decimal.Decimal(1)), MaxValueValidator(decimal.Decimal(5))],
        blank=True,null=True
    )
    comment_decision_making=models.TextField(max_length=400,blank=True,null=True)
    innovation = models.PositiveIntegerField(verbose_name="Initiative &Innovation",
        validators=[MinValueValidator(decimal.Decimal(1)), MaxValueValidator(decimal.Decimal(5))],
        blank=True,null=True
    )
    comment_innovation=models.TextField(max_length=400,blank=True,null=True)
    team_work = models.PositiveIntegerField(
        validators=[MinValueValidator(decimal.Decimal(1)), MaxValueValidator(decimal.Decimal(5))],
        blank=True,null=True
    )
    comment_teamwork=models.TextField(max_length=400,blank=True,null=True)
    human_resource = models.PositiveIntegerField(verbose_name="Human Resource Management:/Mentorship",
        validators=[MinValueValidator(decimal.Decimal(1)), MaxValueValidator(decimal.Decimal(5))],blank=True,null=True
    )
    comment_human_resource=models.TextField(max_length=400,blank=True,null=True)
    fin_management = models.PositiveIntegerField(verbose_name="Financial management",
        validators=[MinValueValidator(decimal.Decimal(1)), MaxValueValidator(decimal.Decimal(5))],
        blank=True,null=True
    )
    comment_financial_management=models.TextField(max_length=400,blank=True,null=True)

    o_resource_man = models.PositiveIntegerField(verbose_name="Management of other resources (equipment & facilities)",
        validators=[MinValueValidator(decimal.Decimal(1)), MaxValueValidator(decimal.Decimal(5))],
        blank=True,null=True
    )
    comment_other_resource_mananagement=models.TextField(max_length=400,blank=True,null=True)
    result_orientation = models.PositiveIntegerField(
        validators=[MinValueValidator(decimal.Decimal(1)), MaxValueValidator(decimal.Decimal(5))],
        blank=True,null=True
    )
    comment_result_orientation=models.TextField(max_length=400,blank=True,null=True)
    client_care = models.PositiveIntegerField(
        validators=[MinValueValidator(decimal.Decimal(1)), MaxValueValidator(decimal.Decimal(5))],
        blank=True,null=True
    )
    comment_client_care=models.TextField(max_length=400,blank=True,null=True)
    communication = models.PositiveIntegerField(verbose_name="Communication skills", help_text="This is a sample help text",
        validators=[MinValueValidator(decimal.Decimal(1)), MaxValueValidator(decimal.Decimal(5))],
        blank=True,null=True
    )
    comment_communication=models.TextField(max_length=400,blank=True,null=True)
    integrity = models.PositiveIntegerField(
        validators=[MinValueValidator(decimal.Decimal(1)), MaxValueValidator(decimal.Decimal(5))],
        blank=True,null=True
    )
    comment_integrity=models.TextField(max_length=400,blank=True,null=True)
    time_management = models.PositiveIntegerField(
        validators=[MinValueValidator(decimal.Decimal(1)), MaxValueValidator(decimal.Decimal(5))],
        blank=True,null=True
    )
    comment_time_management=models.TextField(max_length=400,blank=True,null=True)
    loyalty = models.PositiveIntegerField(
        validators=[MinValueValidator(decimal.Decimal(1)), MaxValueValidator(decimal.Decimal(5))],
        blank=True,null=True
    )
    comment_loyalty=models.TextField(max_length=400,blank=True,null=True)
    other_competence = models.TextField(max_length=500,verbose_name="Other Competences (specify)",blank=True, null=True)
    comment_other_competence = models.TextField(max_length=500,blank=True, null=True)

    submitted_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.get_full_name()

class AppraiserAndAppraiseeAgreement(models.Model):
    competence = models.ForeignKey(Competence, on_delete=models.CASCADE, blank=True, null=True)
    key_outputs = models.CharField(max_length=100,  blank=True, null=True)
    performance_indicator = models.CharField(max_length=100,  blank=True, null=True)
    performance_target = models.CharField(max_length=100,  blank=True, null=True)
    self_rating = models.PositiveIntegerField(blank=True, null=True, 
        validators=[MinValueValidator(decimal.Decimal(1)), MaxValueValidator(decimal.Decimal(5))]
    )
    supervisor_rating = models.PositiveIntegerField(blank=True, null=True, 
        validators=[MinValueValidator(decimal.Decimal(1)), MaxValueValidator(decimal.Decimal(5))]
    )
    # super_visor = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Supervisor inspecting this.")
    super_visor = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name="Supervisor inspecting this.")
    comments_on_performance = models.CharField(max_length=100,  blank=True, null=True)

    def __str__(self) -> str:
        return self.competence.user.get_full_name()

    @property
    def agreed_rating(self):
        if self.supervisor_rating:
            return int((self.supervisor_rating+self.self_rating)/2)
        return self.self_rating




class OverallPerformance(models.Model):
    competence = models.ForeignKey(Competence, on_delete=models.CASCADE)
    overall_mark = models.PositiveIntegerField(
        validators=[MinValueValidator(decimal.Decimal(1)), MaxValueValidator(decimal.Decimal(5)),
        ],
    )
    super_visor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.super_visor.get_full_name()

class Performance(models.Model):
    competence = models.ForeignKey(Competence, on_delete=models.CASCADE)
    performance_gap = models.CharField(max_length=250,  blank=True, null=True)
    agreed_action = models.CharField(max_length=250,  blank=True, null=True)
    time_frame = models.PositiveIntegerField(verbose_name="Time duration in days",  blank=True, null=True,
        validators=[MinValueValidator(decimal.Decimal(1)), MaxValueValidator(decimal.Decimal(120))]
    )

    def __str__(self) -> str:
        return self.competence.user.get_full_name()

class AppraiseeComment(models.Model):
    competence = models.OneToOneField(Competence, on_delete=models.CASCADE)
    effectiveness = models.TextField(max_length=500, verbose_name="Describe how effectively you have been utilized by the University.",  blank=True, null=True)
    assistance = models.TextField(max_length=500, verbose_name="How would you like management to assist you in improving your performance?", blank=True, null=True)
    aspiration = models.TextField(max_length=500, verbose_name="What are your aspirations as far as career development is concerned?", blank=True, null=True)
    any_comment = models.TextField(max_length=500, verbose_name="Any other comment?", blank=True, null=True)
    comment_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.competence.user.get_full_name()

class AppraiserComment(models.Model):
    appraisee_comment = models.OneToOneField(AppraiseeComment, on_delete=models.CASCADE)
    comment_justification = models.TextField(max_length=500, verbose_name="COMMENTS OF THE APPRAISER & JUSTIFICATION FOR THE COMMENTS")
    current_date = models.DateTimeField(auto_now=True)
    super_visor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.super_visor.get_full_name()


class VcComment(models.Model):
    appraisee_comment = models.ForeignKey(Competence, on_delete=models.CASCADE)
    vc_comment = models.TextField(verbose_name="COMMENTS OF THE VICE CHANCELLOR /DEPUTY VICE CHANCELLOR (AA) /DEPUTY VICE CHANCELLOR (F&A)**",max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commentdate = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.user.get_full_name()



@receiver(post_save, sender = User)
def post_save_Profile_signal(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user = instance)