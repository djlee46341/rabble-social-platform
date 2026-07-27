from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rabble.models import Subrabbles, Posts
from .serializers import SubrabblesSerializer, PostsSerializer

@api_view(['GET'])
def subrabble_list(request):
    subrabbles = Subrabbles.objects.all()
    serializer = SubrabblesSerializer(subrabbles, many=True)  
    return Response(serializer.data)
@api_view(['GET'])
def subrabble_detail(request, identifier):
    subrabble = Subrabbles.objects.get(identifier=identifier)
    serializer = SubrabblesSerializer(subrabble)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def subrabble_posts(request, identifier):
    subrabble = Subrabbles.objects.get(identifier=identifier)

    if request.method == 'GET':
        posts = Posts.objects.filter(subrabble=subrabble)
        serializer = PostsSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(subrabble=subrabble)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def post_detail(request, identifier, pk):
    post = Posts.objects.get(pk=pk, subrabble__identifier=identifier)

    if request.method == 'GET':
        serializer = PostsSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = PostsSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
