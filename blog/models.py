from django.conf import settings
from django.db import models
from django.utils import timezone
from next_prev import next_in_order, prev_in_order

full_name = "Lauren Alie"
my_uni = "University of Birmingham"
my_degree = "BSc Computer Science with Digital Technology Partnership (PwC)"
my_uni_location = "Birmingham"
my_sixth_form = "Kendrick School"
my_secondary = "Maiden Erlegh School"
my_alevels = "A*A*A in Maths, History, Further Maths (A in AS Physics)"
my_gcses = "11 A*s and 1 A (including English Literature A*, Maths A*, Biology A*, Chemistry A*, Physics A*)"
my_school_location = "Reading"

DEFAULT_ID = 1

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='images/', default='images/default.jpg')
    featured = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#class Section(models.Model):
 #   name = models.CharField(max_length=200, default='')
  #  start_date = models.DateField(default=None)
   # end_date = models.DateField(blank=True, default=None)
    #location = models.CharField(max_length=200, default='')

#    def __str__(self):
 #       return self.name

#    class Meta:
#        abstract = True


class Experience(models.Model):
    name = models.CharField(max_length=200, default='', )
    start_date = models.DateField(default=None)
    end_date = models.DateField(blank=True, default=None)
    location = models.CharField(max_length=200, default='')
    role = models.CharField(max_length=200, blank=True, default='')
    description = models.TextField(default='')
    def __str__(self):
        return self.name


class Resume(models.Model):
    name = models.CharField(max_length=200, default=full_name)
    job_title = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    linkedIn = models.URLField(blank=True)
    headline = models.TextField(blank=True, 
                help_text="Write a few sentences to describe where you are in your career and what you stand for.")
    technical_skills = models.TextField(help_text="Programming languages and technical tools you're competent with.")
    education_experience = models.ManyToManyField(Experience, related_name="employee_education", default=DEFAULT_ID)
    technology_experience = models.ManyToManyField(Experience, related_name="employee_technology_experience", default=DEFAULT_ID)
    other_work_experience = models.ManyToManyField(Experience, related_name="employee_other_experience", default=DEFAULT_ID)
    volunteering_experience = models.ManyToManyField(Experience, related_name="employee_volunteering_experience", default=DEFAULT_ID)
    extracurriculars = models.ManyToManyField(Experience, related_name="employee_extracurriculars", default=DEFAULT_ID)
    notable_achievements = models.ManyToManyField(Experience, help_text="Includes hackathon participation, online courses and certifications.", related_name="employee_achievements", blank=True, default=DEFAULT_ID)
    references = models.TextField(blank=True)
    last_updated_date = models.DateTimeField()


    def __str__(self):
        return self.name + " resume "

    def upload(self):
        last_updated_date = timezone.now()
        self.save()






    


