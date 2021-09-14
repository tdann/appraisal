# Generated by Django 3.2.5 on 2021-09-14 13:48

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppraiseeComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effectiveness', models.TextField(blank=True, max_length=500, null=True, verbose_name='Describe how effectively you have been utilized by the University.')),
                ('assistance', models.TextField(blank=True, max_length=500, null=True, verbose_name='How would you like management to assist you in improving your performance?')),
                ('aspiration', models.TextField(blank=True, max_length=500, null=True, verbose_name='What are your aspirations as far as career development is concerned?')),
                ('any_comment', models.TextField(blank=True, max_length=500, null=True, verbose_name='Any other comment?')),
                ('comment_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Competence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession_skill', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(Decimal('1')), django.core.validators.MaxValueValidator(Decimal('5'))], verbose_name='Professional Knowledge/ Skills')),
                ('comment_professional_skill', models.TextField(blank=True, max_length=400, null=True)),
                ('planning', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(Decimal('1')), django.core.validators.MaxValueValidator(Decimal('5'))], verbose_name='Planning, organizing and coordinating')),
                ('comment_planning', models.TextField(blank=True, max_length=400, null=True)),
                ('leadership', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(Decimal('1')), django.core.validators.MaxValueValidator(Decimal('5'))])),
                ('comment_leadership', models.TextField(blank=True, max_length=400, null=True)),
                ('decision_making', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(Decimal('1')), django.core.validators.MaxValueValidator(Decimal('5'))])),
                ('comment_decision_making', models.TextField(blank=True, max_length=400, null=True)),
                ('innovation', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(Decimal('1')), django.core.validators.MaxValueValidator(Decimal('5'))], verbose_name='Initiative &Innovation')),
                ('comment_innovation', models.TextField(blank=True, max_length=400, null=True)),
                ('team_work', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(Decimal('1')), django.core.validators.MaxValueValidator(Decimal('5'))])),
                ('comment_teamwork', models.TextField(blank=True, max_length=400, null=True)),
                ('human_resource', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(Decimal('1')), django.core.validators.MaxValueValidator(Decimal('5'))], verbose_name='Human Resource Management:/Mentorship')),
                ('comment_human_resource', models.TextField(blank=True, max_length=400, null=True)),
                ('fin_management', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(Decimal('1')), django.core.validators.MaxValueValidator(Decimal('5'))], verbose_name='Financial management')),
                ('comment_financial_management', models.TextField(blank=True, max_length=400, null=True)),
                ('o_resource_man', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(Decimal('1')), django.core.validators.MaxValueValidator(Decimal('5'))], verbose_name='Management of other resources (equipment & facilities)')),
                ('comment_other_resource_mananagement', models.TextField(blank=True, max_length=400, null=True)),
                ('result_orientation', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(Decimal('1')), django.core.validators.MaxValueValidator(Decimal('5'))])),
                ('comment_result_orientation', models.TextField(blank=True, max_length=400, null=True)),
                ('client_care', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(Decimal('1')), django.core.validators.MaxValueValidator(Decimal('5'))])),
                ('comment_client_care', models.TextField(blank=True, max_length=400, null=True)),
                ('communication', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(Decimal('1')), django.core.validators.MaxValueValidator(Decimal('5'))], verbose_name='Communication skills')),
                ('comment_communication', models.TextField(blank=True, max_length=400, null=True)),
                ('integrity', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(Decimal('1')), django.core.validators.MaxValueValidator(Decimal('5'))])),
                ('comment_integrity', models.TextField(blank=True, max_length=400, null=True)),
                ('time_management', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(Decimal('1')), django.core.validators.MaxValueValidator(Decimal('5'))])),
                ('comment_time_management', models.TextField(blank=True, max_length=400, null=True)),
                ('loyalty', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(Decimal('1')), django.core.validators.MaxValueValidator(Decimal('5'))])),
                ('comment_loyalty', models.TextField(blank=True, max_length=400, null=True)),
                ('other_competence', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(Decimal('1')), django.core.validators.MaxValueValidator(Decimal('5'))], verbose_name='Other Competences (specify in the Comment)')),
                ('comment_other_competence', models.TextField(blank=True, max_length=500, null=True)),
                ('submitted_on', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VcComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vc_comment', models.TextField(max_length=500, verbose_name='COMMENTS OF THE VICE CHANCELLOR /DEPUTY VICE CHANCELLOR (AA) /DEPUTY VICE CHANCELLOR (F&A)**')),
                ('commentdate', models.DateField(auto_now=True)),
                ('appraiser_comment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='staffappraisal.competence')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roles', models.CharField(choices=[('u', 'User'), ('s', 'Supervisor'), ('h', 'Human Resource'), ('v', 'Vice Chancellor')], default='u', max_length=2)),
                ('job_title', models.CharField(blank=True, max_length=50, null=True)),
                ('salary_scale', models.CharField(blank=True, choices=[('m2', 'M2'), ('m3', 'M3'), ('m4', 'M4'), ('m5', 'M5'), ('m6', 'M6'), ('m7', 'M7'), ('m8', 'M8')], max_length=2, null=True)),
                ('gender', models.CharField(blank=True, choices=[('F', 'Female'), ('M', 'Male')], max_length=2, null=True)),
                ('staff_dob', models.DateField(blank=True, null=True, verbose_name='Staff date of birth')),
                ('f_appoi_date', models.DateField(blank=True, null=True, verbose_name='Date of First Appointment')),
                ('s_appoi_date', models.DateField(blank=True, null=True, verbose_name='Date of Latest Appointment')),
                ('terms_of_appoint', models.CharField(blank=True, choices=[('pro', 'Probation'), ('per', 'Permanant'), ('cont', 'Contract')], max_length=4, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='staff_uploads')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staffappraisal.department')),
                ('user', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('performance_gap', models.CharField(blank=True, max_length=250, null=True)),
                ('agreed_action', models.CharField(blank=True, max_length=250, null=True)),
                ('time_frame', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(Decimal('1')), django.core.validators.MaxValueValidator(Decimal('120'))], verbose_name='Time duration in days')),
                ('competence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staffappraisal.competence')),
            ],
        ),
        migrations.CreateModel(
            name='OverallPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overall_mark', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(Decimal('1')), django.core.validators.MaxValueValidator(Decimal('5'))])),
                ('competence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staffappraisal.competence')),
                ('super_visor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=100)),
                ('faculty_head', models.ForeignKey(help_text='Head of the faculty responsible for confirmations', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Faculty',
                'verbose_name_plural': 'Faculties',
            },
        ),
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staffappraisal.faculty', verbose_name='Select the Faculty to which the department Belongs'),
        ),
        migrations.CreateModel(
            name='AppraiserComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_justification', models.TextField(max_length=500, verbose_name='COMMENTS OF THE APPRAISER & JUSTIFICATION FOR THE COMMENTS')),
                ('current_date', models.DateTimeField(auto_now=True)),
                ('appraisee_comment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='staffappraisal.appraiseecomment')),
                ('super_visor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AppraiserAndAppraiseeAgreement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_outputs', models.CharField(blank=True, max_length=100, null=True)),
                ('performance_indicator', models.CharField(blank=True, max_length=100, null=True)),
                ('performance_target', models.CharField(blank=True, max_length=100, null=True)),
                ('self_rating', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(Decimal('1')), django.core.validators.MaxValueValidator(Decimal('5'))])),
                ('supervisor_rating', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(Decimal('1')), django.core.validators.MaxValueValidator(Decimal('5'))])),
                ('comments_on_performance', models.CharField(blank=True, max_length=100, null=True)),
                ('competence', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staffappraisal.competence')),
                ('super_visor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Supervisor inspecting this.')),
            ],
        ),
        migrations.AddField(
            model_name='appraiseecomment',
            name='competence',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='staffappraisal.competence'),
        ),
    ]
