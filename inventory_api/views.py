from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import Item
from .serializers import ItemRequestSerializer, ItemResponseSerializer

@extend_schema_view(
    tags=["Inventory"],
    get=extend_schema(tags=["Inventory"],responses=ItemResponseSerializer),
    post=extend_schema(tags=["Inventory"],request=ItemRequestSerializer, responses=ItemResponseSerializer)
)
class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.filter(is_deleted=False)
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ItemRequestSerializer
        return ItemResponseSerializer

@extend_schema_view(
    tags=["Inventory"],
    get=extend_schema(tags=["Inventory"],responses=ItemResponseSerializer),
    put=extend_schema(tags=["Inventory"],request=ItemRequestSerializer, responses=ItemResponseSerializer),
    patch=extend_schema(tags=["Inventory"],request=ItemRequestSerializer, responses=ItemResponseSerializer),
    delete=extend_schema(tags=["Inventory"],responses=None)
)
class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.filter(is_deleted=False)
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return ItemRequestSerializer
        return ItemResponseSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
