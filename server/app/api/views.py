from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
import json
from web3 import Web3
from .serializers import *
from .models import *
from .web3_connection_view import connection_to_web3
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.

class getallmusic(APIView):
    def get(self, request):
        try:
            total_tracks = connection_to_web3().functions.getTotalTracks().call()
            tracks = []
            for trackId in range(1, total_tracks + 1):
                track = connection_to_web3().functions.getMusicTrack(trackId).call()
                name, artist, song = track
                tracks.append({
                    'trackId' : trackId,
                    'name' : name,
                    'artist' : artist,
                    'song' : song
                })
            return Response({'stauts': status.HTTP_200_OK,'data':tracks})
        
        except Exception as e:
            return Response({'status':status.HTTP_204_NO_CONTENT,'message':e})
        

class uploadmusic(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        serializer =  SongSerializer(data=request.data)
        if serializer.is_valid():
            jsondata = json.loads(request.data)
            tx_hash = connection_to_web3().functions.uploadTrack(jsondata['name'], jsondata['artist'], jsondata['song']).transact()
            serializer.save()
            print('saved')
            return Response({'status':status.HTTP_201_CREATED,'data':serializer.data, 'tx_hash':tx_hash})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class delivermusic(APIView):
    def get(self, request, id):
        try:
            song_obj = Song.objects.get(id=id)
            serializer = SongSerializer(song_obj)
            return Response({'status':status.HTTP_202_ACCEPTED, 'data':serializer.data})
        
        except Exception as e:
            return Response({'status':status.HTTP_204_NO_CONTENT,'message':e})