from rest_framework import serializers
from .models import Hero, HeroBadge, About_us, Badge, Facilities, Banner, Contact



class HeroSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Hero
        fields = '__all__'

class HeroBadgeSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = HeroBadge
        fields = '__all__'




class AboutSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = About_us
        fields = '__all__'

class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = '__all__'


class FacilitiesSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    points_list = serializers.SerializerMethodField()
    open_hour_list = serializers.SerializerMethodField()



    class Meta:
        model = Facilities
        fields = ['id','title', 'description', 'image', 'points_list', 'open_hour_list', 'created_by']

    def get_points_list(self, obj):
        return obj.get_points_list()

    def get_open_hour_list(self, obj):
        return obj.get_open_hours_list()



class BannerSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Banner
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

