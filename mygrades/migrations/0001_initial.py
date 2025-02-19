# Generated by Django 2.2 on 2019-10-29 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('status', models.CharField(choices=[('Not Assigned', 'Not Assigned'), ('Assigned', 'Assigned'), ('Incomplete', 'Incomplete'), ('Exempt', 'Exempt')], max_length=30)),
                ('type_of', models.CharField(choices=[('Repeating Weekly', 'Repeating Weekly'), ('From Pacing List', 'From Pacing List')], max_length=30)),
                ('active', models.BooleanField(default=False)),
                ('late', models.BooleanField(default=0)),
                ('registered_datetime', models.DateTimeField(auto_now=True)),
                ('submission_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('subject', models.CharField(choices=[('Math', 'Math'), ('ELA', 'ELA'), ('Science', 'Science'), ('History', 'History'), ('Other', 'Other')], max_length=30)),
                ('grade_level', models.CharField(choices=[('P', 'Pre-K'), ('K', 'Kinder'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('All', 'All'), ('High School', 'High School')], max_length=20)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='ScrapyItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(max_length=100, null=True)),
                ('data', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_level', models.CharField(choices=[('PK', 'Pre-K'), ('K', 'Kindergarten'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('PA', 'PA'), ('HS', 'HS'), ('9', '9'), ('A1', 'A1'), ('10', '10'), ('A2', 'A2'), ('11', '11'), ('G', 'G'), ('12', '12')], max_length=20)),
                ('standard_number', models.CharField(max_length=2)),
                ('standard_description', models.CharField(max_length=300)),
                ('strand_code', models.CharField(max_length=2)),
                ('strand', models.CharField(max_length=50, null=True)),
                ('strand_description', models.CharField(max_length=300, null=True)),
                ('objective_number', models.CharField(max_length=2)),
                ('objective_description', models.CharField(max_length=300)),
                ('standard_code', models.CharField(max_length=10)),
                ('subject', models.CharField(choices=[('Math', 'Math'), ('ELA', 'ELA'), ('Science', 'Science'), ('History', 'History'), ('Other', 'Other')], max_length=30)),
                ('PDF_link', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=75)),
                ('last_name', models.CharField(max_length=75)),
                ('email', models.CharField(max_length=75)),
            ],
            options={
                'unique_together': {('first_name', 'last_name', 'email')},
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epicenter_id', models.CharField(max_length=10, unique=True)),
                ('last_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=120)),
                ('phone_number', models.CharField(max_length=50)),
                ('additional_email', models.EmailField(max_length=120, null=True)),
                ('additional_phone_number', models.CharField(max_length=20, null=True)),
                ('grade', models.CharField(choices=[('P', 'Pre-K'), ('K', 'Kinder'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], max_length=20)),
                ('teacher_email', models.CharField(max_length=75)),
                ('curriculum', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mygrades.Curriculum')),
            ],
        ),
        migrations.CreateModel(
            name='ExemptAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignments', models.ManyToManyField(blank=True, null=True, to='mygrades.Assignment')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mygrades.Student')),
            ],
            options={
                'verbose_name_plural': 'Exempt Assignments',
            },
        ),
        migrations.AddField(
            model_name='assignment',
            name='curriculum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curriculum_assignment', to='mygrades.Curriculum'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='standard',
            field=models.ManyToManyField(to='mygrades.Standard'),
        ),
        migrations.CreateModel(
            name='GradeBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complete', models.CharField(default='true', max_length=20)),
                ('required', models.CharField(default='true', max_length=20)),
                ('quarter', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=1)),
                ('week', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18')], max_length=2)),
                ('grade', models.IntegerField()),
                ('semester', models.CharField(choices=[('1', '1'), ('2', '2')], max_length=1)),
                ('curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curriculum_grade', to='mygrades.Curriculum')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gradebook_student', to='mygrades.Student')),
            ],
            options={
                'unique_together': {('student', 'curriculum', 'week', 'quarter')},
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curriculum_enrollment', to='mygrades.Curriculum')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_enrollment', to='mygrades.Student')),
            ],
            options={
                'unique_together': {('curriculum', 'student')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='assignment',
            unique_together={('name', 'curriculum', 'description')},
        ),
    ]
