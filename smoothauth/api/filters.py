from .models import Profile
import django_filters


class ProfileFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['user', 'badge', ]
