from flask import Flask, request

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
#    ConsoleSpanExporter,
    SimpleSpanProcessor,
)
from opentelemetry.exporter.zipkin.json import ZipkinExporter
#from opentelemetry.exporter.jaeger.proto.grpc import JaegerExporter
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
PORT = 8000
MESSAGE = "Hello, world!\n"

app = Flask(__name__)

# create a ZipkinExporter
# zipkin_exporter = ZipkinExporter(
# )
#jaeger_exporter = JaegerExporter(
#)
otlp_exporter = OTLPSpanExporter()

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
   SimpleSpanProcessor(otlp_exporter)
)
#trace.get_tracer_provider().add_span_processor(
#    SimpleSpanProcessor(jaeger_exporter)
#)

FlaskInstrumentor().instrument_app(app)
#RequestsInstrumentor().instrument()



@app.route("/")
def root():
    result = MESSAGE.encode("utf-8")
    return result


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
