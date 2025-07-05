from django.apps import apps
from django.db.models.fields import  (
    IntegerField, CharField, TextField,
    DateField
)

from rest_framework import serializers, viewsets, permissions, routers

FIELD_TYPES = (IntegerField, CharField, TextField, DateField)

router = routers.DefaultRouter()

for M in apps.get_models():
    
    class S(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = M 
            fields = [ F.name for F in M._meta.get_fields() 
                        if issubclass(type(F), FIELD_TYPES) ]
    
    class V(viewsets.ModelViewSet):
        queryset = M.objects.all()
        serializer_class = S
        permission_classes = [ permissions.DjangoModelPermissions ]

    router.register(M._meta.verbose_name_plural, V)
