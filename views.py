from django.http import HttpResponse
from pathlib import Path
from telemetry.adapter import emit_event, emit_metric

PLUGIN_NAME = "demo_plugin"
PLUGIN_DIR = Path(__file__).resolve().parents[0]

def hello_view(request):
    # event
    emit_event(
        "demo.hello_shown", "INFO", "Hello page rendered",
        labels={"endpoint": "/demo"},
        plugin_name=PLUGIN_NAME, plugin_dir=PLUGIN_DIR,
    )
    # metrika
    emit_metric(
        "demo_requests_total", 1, mtype="counter",
        labels={"endpoint": "/demo"},
        plugin_name=PLUGIN_NAME, plugin_dir=PLUGIN_DIR,
    )
    return HttpResponse("Hello from demo_plugin!")