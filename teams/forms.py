from django.forms import FileField, CharField, ModelForm
from teams.models import Team


class CreateTeamForm(ModelForm):

    class Meta:
        model = Team
        fields = ['name', 'defender', 'midfielder1', 'midfielder2', 'striker1', 'striker2']

    def save(self, commit=True):
        instance = super(CreateTeamForm, self).save(commit=False)

        if commit:
            instance.save()

        return instance





