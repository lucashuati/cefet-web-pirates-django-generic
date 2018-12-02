from django.contrib import admin
from django.urls import path
from pirates import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.ListarTesouros.as_view(),name="lista_tesouros"),
    path('inserir',views.InserirTesouro.as_view(),name="inserir"),
    path('editar/<int:pk>/',views.AtualizarTesouro.as_view(),name="editar"),
    path('remover/<int:pk>/',views.RemoverTesouro.as_view(),name="excluir"),
    path('login',LoginView.as_view(template_name="login.html"),name="login"),
    path('logout',LogoutView.as_view(next_page='/login'),name="login"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
