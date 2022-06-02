from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from Users import views as user_views

from .views import ( 
    ArticleListView,
    ArticleDetailView,
    ArticleSearchListView,
    TagArticlesListView,
    CategoryArticlesListView,
    CategoriesListView,
    CategoryCreateView,
    CategoryUpdateCreateView,
    AuthorArticlesListView,
    AuthorsListView,
    CommentCreateView,
    ArticleCommentList,
    DashboardHomeView,
    ArticleWriteView,
    ArticleUpdateView,
    ArticleDeleteView,
    DashboardArticleDetailView,
    ArticlePublishView,
    AuthorWrittenArticlesView,
    AuthorPublishedArticlesView,
    AuthorDraftedArticlesView,
    AuthorDeletedArticlesView,


    
)

urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),
    path('@<str:username>/<str:slug>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/search/', ArticleSearchListView.as_view(), name='article_search_list_view'),
    path('tag/<str:tag_name>/articles', TagArticlesListView.as_view(), name="tag_articles"),
    path('authors/list/', AuthorsListView.as_view(),name='authors_list'),
    path('author/<str:username>/articles', AuthorArticlesListView.as_view(), name='author_articles'),
    path('category/<str:slug>/articles', CategoryArticlesListView.as_view(), name='category_articles'),
    path('categories/list/', CategoriesListView.as_view(),name='categories_list'),
    path('category/create/',CategoryCreateView.as_view(), name="category_create"),
    path('category/<str:slug>/update/', CategoryUpdateCreateView.as_view(),name="category_update"),
    path('comment/new/<str:slug>/', CommentCreateView.as_view(), name="comment_create"),
    path('<str:slug>/comments/', ArticleCommentList.as_view(),name="article_comments"),
    path("author/dashboard/home/", DashboardHomeView.as_view(),name="dashboard_home"),
    path("author/dashboard/home/", DashboardHomeView.as_view(), name="dashboard_home"),
    path('me/article/write/', ArticleWriteView.as_view(),name="article_write"),
    path('me/article/<str:slug>/update/', ArticleUpdateView.as_view(),name="article_update"),
    path('me/article/<str:slug>/delete/', ArticleDeleteView.as_view(), name="article_delete"),
    path("article/<str:slug>/publish/", ArticlePublishView.as_view(),name="publish_article"),
    path("me/articles/written/", AuthorWrittenArticlesView.as_view(),name="written_articles"),
    path("me/articles/published/", AuthorPublishedArticlesView.as_view(), name="published_articles"),
    path("me/articles/drafts/", AuthorDraftedArticlesView.as_view(),name="drafted_articles"),
    path("me/articles/deleted/", AuthorDeletedArticlesView.as_view(), name="deleted_articles"),
    path("me/<str:slug>/",DashboardArticleDetailView.as_view(),name='dashboard_article_detail'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()


