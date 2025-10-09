from django.shortcuts import render
from telemetry.adapter import emit_event, emit_metric

def index(request):
    emit_event(
        source="demo_plugin:DemoPlugin@0.1.0",
        environment="dev",
        event="demo.hello_shown",
        level="INFO",
        message="Demo template rendered",
        labels={"endpoint": "/demo"},
    )
    emit_metric(
        source="demo_plugin:DemoPlugin@0.1.0",
        environment="dev",
        metric="demo_requests_total",
        mtype="counter",
        value=1,
        labels={"endpoint": "/demo"},
    )
    return render(request, "demo_plugin/index.html")
