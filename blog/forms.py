from django import forms

from .models import Post, Resume, Experience, Comment




class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'image','featured',)
        ordering = ('created_date', 'title')



class ResumeForm(forms.ModelForm):

    class Meta:
        model = Resume
        fields = (
             'job_title', 'email', 'linkedIn',
            'headline', 'technical_skills', 
            'technology_experience', 'other_work_experience', 'volunteering_experience',
            'extracurriculars', 'notable_achievements',
                'references')


class ExperienceForm(forms.ModelForm):
    
    class Meta:
        model = Experience
        fields = ('name', 'start_date', 'end_date','location','role', 'description')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)