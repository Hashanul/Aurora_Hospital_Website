from rest_framework import serializers
from .models import VisitorPackage, PackageDetail, RoomRent, Equipment, FeedbackBanner, Feedback

class VisitorPackageSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = VisitorPackage
        fields = '__all__'

class PackageDetailSerializer(serializers.ModelSerializer):
        # Write-only field (Accept ID)
    package_title_id = serializers.PrimaryKeyRelatedField(
        queryset=VisitorPackage.objects.all(),
        source='package_title',
        write_only=True,
        allow_null=True,
        required=False
    )

    # Read-only field (Show only title)
    package_title = serializers.CharField(
        source='package_title.title',
        read_only=True
    )
    created_by = serializers.StringRelatedField(read_only=True)


    class Meta:
        model = PackageDetail
        fields = '__all__'


class RoomRentSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = RoomRent
        fields = '__all__'


class EquipmentSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Equipment
        fields = '__all__'

class FeedbackBannerSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = FeedbackBanner
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Feedback
        fields = '__all__'

