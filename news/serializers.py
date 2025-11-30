from rest_framework import serializers
from .models import NewsCategories, News, NewsBanner



class NewsBannerSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = NewsBanner
        fields = '__all__'


class NewsCategoriesSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = NewsCategories
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    category_name = serializers.CharField(write_only = True, required=False, allow_blank=True)
    category_description = serializers.CharField(write_only = True, required=False, allow_blank=True)
    category = serializers.StringRelatedField(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset = NewsCategories.objects.all(),
        source = 'category',
        write_only = True,
        required = False,
        allow_null = True
    )

    class Meta:
        model = News
        fields = ['id', 'title', 'richtext', 'image', 'created_by',
                'category', 'category_id', 'category_name', 'category_description', 'created_at' ]


    def create(self, validated_data):
        category_name = validated_data.pop('category_name', None)
        category_description = validated_data.pop('category_description', None)
        if category_name:
            category, created = NewsCategories.objects.get_or_create(name=category_name)
            validated_data['category'] = category
        if category_description and category_name:
            category.description = category_description 
            category.save()
        news = News.objects.create(**validated_data)
        return news