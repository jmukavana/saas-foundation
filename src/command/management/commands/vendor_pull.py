from typing import Any

from django.conf import settings
from django.core.management import BaseCommand

import helpers

STATICFILES_VENDORS_DIR = getattr(settings, 'STATICFILES_VENDORS_DIR')

VENDOR_STATICFILES = {
    "flowbite.min.js": "https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.js",
    "flowbite.min.css": "https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.css"
}


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        self.stdout.write("Downloading vendor static files...")
        completed_urls = []
        for name, url in VENDOR_STATICFILES.items():
            out_path = STATICFILES_VENDORS_DIR / name
            dl_success = helpers.downloader.download_to_local(url, out_path)
            if dl_success:
                completed_urls.append(url)
            else:
                self.stdout.write(self.style.ERROR(f"Failed to download {url}"))
        if set(completed_urls) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(self.style.SUCCESS("All vendor static files updated successfully"))
        else:
            self.stdout.write(self.style.WARNING("Failed to update all vendor static files"))
