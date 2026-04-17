from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import Serializer
from rest_framework.decorators import APIView
from api.models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from .serializers import Profileserializer
from .models import Profilemodel
import os 
from rest_framework.parsers import MultiPartParser
from .serializers import Postserializer
from .models import Post, Likes, User, Follow


@api_view(['POST'])
def userlogin(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()

        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh_token': str(refresh),
            'access_token': str(refresh.access_token),
        })

    return Response(serializer.errors)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def profilehandle(request):
    
    old = Profilemodel.objects.filter(user=request.user).first()

    serializer = Profileserializer(data=request.data)  

    if serializer.is_valid():
        serializer.save(user=request.user)

        if old:
            if os.path.isfile(old.profile.path):
                os.remove(old.profile.path)
            old.delete()

        return Response({
            'profile': serializer.data['profile']
        })

    return Response(serializer.errors)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def posthandler(request):

    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = Postserializer(posts, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = Postserializer(data=request.data)

        if serializer.is_valid():
            post = serializer.save(user=request.user)

            return Response({
                'id': post.id,
                'title': post.title,
                'post': post.post.url,
                'user_id': post.user.id
            })

        return Response(serializer.errors)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def likeshandler(request, post_id):
    user = request.user
    post = get_object_or_404(Post, id=post_id)

    like = Likes.objects.filter(user=user, post=post)

    if like.exists():
        like.delete()
    else:
        Likes.objects.create(user=user, post=post)

    likes = Likes.objects.filter(post=post).count()
    likedusers = Likes.objects.filter(post=post).values_list('user__username', flat=True)

    return Response({
        'likes': likes,
        'likedusers': likedusers
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def takeusername(request):
    return Response({
        'username': request.user.username
    })


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def followhandle(request, user_id):

    user = request.user
    target_user = User.objects.get(id=user_id)

    model = Follow.objects.filter(follower=user, following=target_user)

    if model.exists():
        model.delete()
    else:
        Follow.objects.create(follower=user, following=target_user)

    counts = Follow.objects.filter(following=target_user).count()
    following = Follow.objects.filter(following=target_user).values_list('follower__username', flat=True)

    return Response({
        'count': counts,
        'following': following
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def sorthandler(request):
    user = request.user

    username = user.username
    following = Follow.objects.filter(following=user).count()
    district = user.district

    profile = Profilemodel.objects.filter(user=user).first()

    posts = Post.objects.filter(user=user)

    data = []
    for i in posts:
        data.append({
            "title": i.title,
            "post": i.post.url
        })

    return Response({
        "username": username,
        "following": following,
        "district": district,
        "profile": profile.profile.url if profile else None,
        "posts": data
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def You(request):
    user = request.user
    username = user.username
    following = Follow.objects.filter(following=user).count()

    profile = Profilemodel.objects.filter(user=user).first()

    post = Post.objects.filter(user=user)

    data = []
    for i in post:
        data.append(i.post.url)

    return Response({
        "username": username,
        "following": following,
        "profile": profile.profile.url if profile else None,
        "posts": data 
    })


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deletepost(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    post.delete()

    return Response({
        "message": "Post deleted successfully"
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def sortedwithdistrict(request):
    user = request.user

    username = user.username
    following = Follow.objects.filter(following=user).count()
    district = user.district

    profile = Profilemodel.objects.filter(user=user).first()

    posts = Post.objects.filter(user=user)

    data = []
    for i in posts:
        data.append({
            "title": i.title,
            "post": i.post.url
        })

    return Response({
        "username": username,
        "following": following,
        "district": district,
        "profile": profile.profile.url if profile else None,
        "posts": data
    })
