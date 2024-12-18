from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ["id", "user", "amount", "payment_date", "status"]
        read_only_fields = ["user", "payment_date", "status"]

    def create(self, validated_data: dict) -> Payment:
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
