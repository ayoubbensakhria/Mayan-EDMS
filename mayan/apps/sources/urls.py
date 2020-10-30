from django.conf.urls import url

from .api_views import (
    APIStagingSourceFileView, APIStagingSourceFileImageView,
    APIStagingSourceFileUploadView, APIStagingSourceListView,
    APIStagingSourceView
)
from .views.document_file_views import DocumentFileUploadInteractiveView
from .views.document_views import UploadInteractiveView
from .views.source_views import (
    SourceBackendSelectionView, SourceCheckView, SourceCreateView,
    SourceDeleteView, SourceEditView, SourceListView, StagingFileDeleteView
)
from .wizards import DocumentCreateWizard

urlpatterns = [
    url(
        regex=r'^staging_folders/(?P<staging_folder_id>\d+)/files/(?P<encoded_filename>.+)/delete/$',
        name='staging_file_delete', view=StagingFileDeleteView.as_view()
    ),

    # Document create views

    url(
        regex=r'^documents/create/from/local/multiple/$',
        name='document_create_multiple', view=DocumentCreateWizard.as_view()
    ),
    url(
        regex=r'^documents/upload/new/interactive/(?P<source_id>\d+)/$',
        name='document_upload_interactive',
        view=UploadInteractiveView.as_view()
    ),
    url(
        regex=r'^documents/upload/new/interactive/$',
        name='document_upload_interactive',
        view=UploadInteractiveView.as_view()
    ),
    url(
        regex=r'^documents/(?P<document_id>\d+)/files/upload/interactive/(?P<source_id>\d+)/$',
        name='document_file_upload',
        view=DocumentFileUploadInteractiveView.as_view()
    ),
    url(
        regex=r'^documents/(?P<document_id>\d+)/files/upload/interactive/$',
        name='document_file_upload',
        view=DocumentFileUploadInteractiveView.as_view()
    ),

    # Setup views

    url(
        regex=r'^sources/$', name='setup_source_list',
        view=SourceListView.as_view()
    ),
    #url(
    #    regex=r'^sources/create/(?P<source_type_name>\w+)/$',
    #    name='setup_source_create', view=SourceCreateView.as_view()
    #),
    url(
        regex=r'^sources/(?P<backend_path>[a-zA-Z0-9_.]+)/create/$',
        name='source_create', view=SourceCreateView.as_view()
    ),
    url(
        regex=r'^sources/(?P<source_id>\d+)/check/$',
        name='setup_source_check', view=SourceCheckView.as_view()
    ),
    url(
        regex=r'^sources/(?P<source_id>\d+)/delete/$',
        name='setup_source_delete', view=SourceDeleteView.as_view()
    ),
    url(
        regex=r'^sources/(?P<source_id>\d+)/edit/$', name='setup_source_edit',
        view=SourceEditView.as_view()
    ),
    url(
        regex=r'^sources/backend/selection/$',
        name='source_backend_selection',
        view=SourceBackendSelectionView.as_view()
    ),
]

api_urls = [
    url(
        regex=r'^staging_folders/file/(?P<staging_folder_pk>[0-9]+)/(?P<encoded_filename>.+)/image/$',
        name='stagingfolderfile-image',
        view=APIStagingSourceFileImageView.as_view()
    ),
    url(
        regex=r'^staging_folders/file/(?P<staging_folder_pk>[0-9]+)/(?P<encoded_filename>.+)/upload/$',
        name='stagingfolderfile-upload',
        view=APIStagingSourceFileUploadView.as_view()
    ),
    url(
        regex=r'^staging_folders/file/(?P<staging_folder_pk>[0-9]+)/(?P<encoded_filename>.+)/$',
        name='stagingfolderfile-detail',
        view=APIStagingSourceFileView.as_view()
    ),
    url(
        regex=r'^staging_folders/$', name='stagingfolder-list',
        view=APIStagingSourceListView.as_view()
    ),
    url(
        regex=r'^staging_folders/(?P<pk>[0-9]+)/$',
        name='stagingfolder-detail', view=APIStagingSourceView.as_view()
    )
]
