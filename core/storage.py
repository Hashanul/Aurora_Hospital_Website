import os
from urllib.parse import urljoin
from django.conf import settings
from django.core.files.storage import FileSystemStorage


class NewsStorage(FileSystemStorage):
    """Custom storage that saves files under MEDIA_ROOT/news/ and serves
    them from MEDIA_URL/news/.

    Use by setting `CKEDITOR_5_FILE_STORAGE = 'core.storage.NewsStorage'` in
    your `settings.py`.
    """

    def __init__(self, *args, **kwargs):
        location = kwargs.pop("location", None) or os.path.join(settings.MEDIA_ROOT, "news")
        base_url = kwargs.pop("base_url", None) or urljoin(settings.MEDIA_URL, "news/")
        super().__init__(location=location, base_url=base_url, *args, **kwargs)
