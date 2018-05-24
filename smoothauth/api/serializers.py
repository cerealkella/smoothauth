from rest_framework import serializers
from api.models import Api, Profile, ConnectLog, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class ApiSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='Api-highlight', format='html')

    class Meta:
        model = Api
        fields = ('url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')

    def create(self, validated_data):
        """
        Create and return a new `Api` instance, given the validated data.
        """
        return Api.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Api` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

class UserSerializer(serializers.HyperlinkedModelSerializer):
    api = serializers.HyperlinkedRelatedField(many=True, view_name='Api-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'api')

class ConnectLogSerializer(serializers.HyperlinkedModelSerializer):
    #api = serializers.PrimaryKeyRelatedField(many=True, queryset=Api.objects.all())
    #user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = ConnectLog
        #fields = ('url', 'id', 'badge', 'user', 'pw', 'desktop')
        fields = ('activity', 'id', 'fqdn', 'ip_addr', 'os', 'user', 'created')

    def create(self, validated_data):
        """
        Create and return a new `Api` instance, given the validated data.
        """
        return ConnectLog.objects.create(**validated_data)

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    #api = serializers.PrimaryKeyRelatedField(many=True, queryset=Api.objects.all())
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Profile
        #fields = ('url', 'id', 'badge', 'user', 'pw', 'desktop')
        fields = ('url', 'id', 'badge', 'user', 'pw', 'desktop', 'modified_date')

    def create(self, validated_data):
        """
        Create and return a new `Api` instance, given the validated data.
        """
        return Profile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Profile` instance, given the validated data.
        """
        instance.badge = validated_data.get('badge', instance.badge)
        instance.pw = validated_data.get('pw', instance.pw)
        instance.desktop = validated_data.get('desktop', instance.desktop)
        instance.save()
        return instance
