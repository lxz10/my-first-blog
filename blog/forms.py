from django import forms

from .models import Post, Resume, Experience

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'image','featured',)
        ordering = ('created_date', 'title')

    #add education_experience
    class Meta:
        model = Resume
        fields = (
            'name', 'job_title', 'email', 'linkedIn',
            'headline', 'technical_skills', 
            'education_experience','technology_experience', 'other_work_experience', 'volunteering_experience',
            'extracurriculars', 'notable_achievements',
             'references')

    class Meta:
        model = Experience
        fields = ('name', 'start_date', 'end_date','location','role', 'description')
