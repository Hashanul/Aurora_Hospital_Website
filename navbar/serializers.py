# from rest_framework import serializers
# from .models import MenuItem, MenuContent, PopUp



# class PopUpSerializer(serializers.ModelSerializer):
#     created_by = serializers.StringRelatedField(read_only=True)
    
#     class Meta:
#         model = PopUp
#         fields = '__all__'

# class MenuContentSerializer(serializers.ModelSerializer):
#     # menu = serializers.StringRelatedField()
#     class Meta:
#         model = MenuContent
#         fields = ["id", "menu", "title", "to"]
#         extra_kwargs ={
#             'menu' : {'write_only': True},
#         }


# class MenuItemSerializer(serializers.ModelSerializer):
#     content = MenuContentSerializer(many=True, read_only=True)

#     class Meta:
#         model = MenuItem
#         fields = ["id", "title", "to", "classChange", "content"]