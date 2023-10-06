from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from pasco import PASCOBLEDevice

from .models import  Asset
from .serializers import AssetSerializer

def connect_to_pasco(model):
    device = PASCOBLEDevice()
    try:
        print("Device",device.scan())
        device.connect_by_id(model)
        is_connected = device.is_connected
    except Exception as e:
        print(f"Failed to connect: {e}")
        return False 
    finally:
        device.disconnect()
    return is_connected

    

# Create your views here.
class Labassets(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    def create(self, request):
        serializer = AssetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve_by_model(self, request, model_name):
        try:
            assets = Asset.objects.filter(model=model_name)
            serializer = AssetSerializer(assets, many=True)
            return Response(serializer.data)
        except Asset.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    
    def partial_update(self, request, pk=None):
        asset = self.get_object()
        serializer = AssetSerializer(asset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        asset = self.get_object()
        asset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def startservicepasco(self, request, model_name):
        if not model_name:
            return Response({"error": "Invalid model_name provided"}, status=status.HTTP_400_BAD_REQUEST)
        is_connected = connect_to_pasco(model_name)
        return Response({"is_connected": is_connected}, status=status.HTTP_200_OK)
