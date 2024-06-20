from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import Item
from .serializers import ItemRequestSerializer, ItemResponseSerializer
from rest_framework.response import Response


@extend_schema_view(
    get=extend_schema(
        tags=["Inventory"], responses={200: ItemResponseSerializer(many=True)}
    ),
    post=extend_schema(
        tags=["Inventory"],
        request=ItemRequestSerializer,
        responses={201: ItemResponseSerializer},
    ),
)
class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.filter(is_deleted=False)
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return ItemResponseSerializer

    def perform_create(self, serializer):
        serializer.save()


@extend_schema_view(
    get=extend_schema(tags=["Inventory"], responses={200: ItemResponseSerializer}),
    put=extend_schema(
        tags=["Inventory"],
        request=ItemRequestSerializer,
        responses={200: ItemResponseSerializer},
    ),
    patch=extend_schema(
        tags=["Inventory"],
        request=ItemRequestSerializer,
        responses={200: ItemResponseSerializer},
    ),
    delete=extend_schema(
        tags=["Inventory"], responses={200: "Success", 400: "Bad Request"}
    ),
)
class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.filter(is_deleted=False)
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return ItemResponseSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response(
            {
                "response": "Item successfully deleted!",
                "item": ItemResponseSerializer(instance).data,
            },
            status=status.HTTP_200_OK,
        )
