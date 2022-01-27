from django.db import models


class BaseModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return {}.format(self.name)

    class Meta:
        abstract = True

class Team(BaseModel):
    city = models.TextField(max_length=128)

class Player(BaseModel):
    goals = models.IntegerField()
    team = models.ForeignKey("teams.Team", on_delete=models.CASCADE)