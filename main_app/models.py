from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


LEVELS = (
    (1, 'Fundamental Awareness'),
    (2, 'Novice'),
    (3, 'Intermediate'),
    (4, 'Advanced'),
    (5, 'Expert')
)

class Skill(models.Model):
    description = models.TextField(max_length=250)
    skill_level = models.IntegerField(choices=LEVELS, default=LEVELS[0][0])
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Curent skill level is {self.get_skill_level_display()}'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'skill_id': self.id})


