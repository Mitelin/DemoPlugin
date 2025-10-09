from django.shortcuts import render
from pathlib import Path
from telemetry.adapter import emit_event, emit_metric

PLUGIN_NAME = "demo_plugin"
PLUGIN_DIR = Path(__file__).resolve().parent

def index(request):
    emit_event(
        "demo.hello_shown",
        "INFO",
        "Demo template rendered",
        labels={"endpoint": "/demo"},
        plugin_name=PLUGIN_NAME,
        plugin_dir=PLUGIN_DIR,
    )
    emit_metric(
        "demo_requests_total",
        1,
        mtype="counter",
        labels={"endpoint": "/demo"},
        plugin_name=PLUGIN_NAME,
        plugin_dir=PLUGIN_DIR,
    )
    return render(request, "demo_plugin/index.html")
