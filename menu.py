from django.urls import reverse

def get_menu():
    return {
        "title": "Demo",
        "url": "/demo/",  # kořen pluginu (prefix)
        "items": [
            {"title": "Úvod", "url": reverse("demo_plugin_index")},
            # {"title": "Další stránka", "url": reverse("demo_plugin_something")},
        ],
    }
