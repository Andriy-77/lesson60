from django.db.models import F
from django.utils import timezone

from .models import PageView


class PageViewMiddleware:
    """
    Stores aggregated page view counters in DB (PageView).
    Keeps logic simple for a learning portfolio project.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        try:
            path = request.path or "/"

            # Skip admin and asset paths
            if (
                path.startswith("/admin/")
                or path.startswith("/static/")
                or path.startswith("/media/")
            ):
                return response

            obj, created = PageView.objects.get_or_create(page_path=path)
            if created:
                obj.views = 1
                obj.last_viewed = timezone.now()
                obj.save(update_fields=["views", "last_viewed"])
            else:
                PageView.objects.filter(pk=obj.pk).update(
                    views=F("views") + 1,
                    last_viewed=timezone.now(),
                )
        except Exception:
            # Analytics should never break page rendering
            pass

        return response
