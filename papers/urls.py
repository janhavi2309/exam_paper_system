from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_paper, name='upload_paper'),
    path('moderator/', views.moderator_dashboard, name='moderator_dashboard'),
    path('request_decryption/<int:paper_id>/', views.request_decryption, name='request_decryption'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('approve/<int:request_id>/', views.approve_decryption, name='approve_decryption'),
    path('reject/<int:request_id>/', views.reject_decryption, name='reject_decryption'),
    path('view/<int:paper_id>/', views.view_decrypted_paper, name='view_decrypted_paper'),
    path('review/<int:paper_id>/', views.review_paper, name='review_paper'),
    path('final_selection/', views.final_selection, name='final_selection'),
]
