from rest_framework import viewsets, permissions
from .models import Payment
from .serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all().order_by("-payment_date")
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer: PaymentSerializer) -> None:
        serializer.save(user=self.request.user)
