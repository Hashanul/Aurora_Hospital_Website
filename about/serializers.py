from rest_framework import serializers
from .models import BOD, ChairmanMessage, MDMessage, AboutBanner


class AboutBannerSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = AboutBanner
        fields = "__all__"



    # created_by = serializers.StringRelatedField(read_only=True)
class BODSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    # Doctor related read-only fields
    doctor_name = serializers.CharField(source="bod_drName.drName", read_only=True)
    doctor_drCode = serializers.CharField(source="bod_drName.drCode", read_only=True)
    doctor_designation = serializers.CharField(source="bod_drName.designation", read_only=True)
    doctor_description = serializers.CharField(source="bod_drName.description", read_only=True)
    doctor_richtext = serializers.CharField(source="bod_drName.richtext", read_only=True)
    doctor_image = serializers.ImageField(source="bod_drName.image", read_only=True)
    doctor_department = serializers.CharField(source="bod_drName.department.name", read_only=True)
    doctor_email = serializers.CharField(source="bod_drName.email", read_only=True)
    doctor_phone = serializers.CharField(source="bod_drName.phone", read_only=True)

    class Meta:
        model = BOD
        fields = "__all__"

    def validate(self, data):
        bod_drName = data.get("bod_drName")  # doctor selected or not

        # CASE 1: doctor selected
        if bod_drName is not None:
            # bod_designation must be required
            if not data.get("bod_designation"):
                raise serializers.ValidationError({
                    "bod_designation": "Doctor select করলে bod_designation অবশ্যই দিতে হবে।"
                })

            # These fields should be ignored if doctor selected
            data["bod_name"] = None
            data["bod_image"] = None
            data["richtext"] = None

        # CASE 2: doctor NOT selected
        else:
            # User must manually fill own BOD data
            if not data.get("bod_name"):
                raise serializers.ValidationError({
                    "bod_name": "Doctor না দিলে bod_name দিতে হবে।"
                })

        return data
    
    def create(self, validated_data):
        validated_data.pop('richtext', None)
        return super().create(validated_data)





class ChairmanMessageSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = ChairmanMessage
        fields = "__all__"


class MDMessageSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = MDMessage
        fields = "__all__"

