from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('submit/', views.userlogin, name='userlogin' ),
    path('profile/', views.profilehandle, name='profilehanlde'),
    path('post/',views.posthandler, name='posthandler'),
    path('likes/<int:post_id>', views.likeshandler, name='likeshandler'),
    path('takeusername/',views.takeusername,name='takeusername'),
    path('follow/<int:user_id>',views.followhandle, name='followhandle'),
    path('sorthandler/',views.sorthandler, name='sorthandler'),
    path('You/',views.You, name='You'),
    path('deletepost/<int:post_id>', views.deletepost, name='deletepost'),
    path('sortedwithdistrict/',views.sortedwithdistrict, name='sortedwithdistrict')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)