from django.urls import path, include
from .views import *

urlpatterns = [
    path('add/', new_ccos_view, name='new_ccos_page'),
    path('remarks/<int:remark_id>', remark_view, name='remark_page'),
    path('remarks/add/', new_remark_view, name='new_remark_page'),
    path('remarks/add/<int:element_id>', new_remark_view, name='new_remark_shortcut_page'),
    path('<int:id>/', include([
        path('', ccos_view, name='ccos_page'),
        path('add/<int:element_id>', add_element_view, name='add_element_api'),
        path('remarks/', include([
            path('list/', remarks_list_view, name='remarks_list_page'),
            path('list/<int:element_id>', remarks_list_view, name='remarks_list_filter_page'),
        ])),
        path('export/', export_view, name='export_to_excel')
    ])),
    path('', ccos_list_view, name='ccos_list_page'),
]
