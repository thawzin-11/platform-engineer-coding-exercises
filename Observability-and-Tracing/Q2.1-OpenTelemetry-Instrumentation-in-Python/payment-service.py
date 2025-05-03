from opentelemetry import trace, baggage
from opentelemetry.trace import TracerProvider
from opentelemetry.sdk.trace import SpanProcessor, BatchSpanProcessor
from opentelemetry.sdk.trace.export import OTLPSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.context import attach, detach, set_value

# Setup tracer provider with resource attributes
resource = Resource(attributes={
    SERVICE_NAME: "payment-service"
})
trace.set_tracer_provider(TracerProvider(resource=resource))

# Create OTLP exporter for a locally running OTEL Collector
otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)

# Add the exporter to the tracer provider
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

# Get a tracer
tracer = trace.get_tracer(__name__)

def process_payment(user_id: str):
    # Add baggage (context propagation)
    context = set_value("user_id", user_id)
    token = attach(context)

    # Create span
    with tracer.start_as_current_span("process_payment") as span:
        # Add custom attribute
        span.set_attribute("payment_method", "credit_card")
        
        # Add user_id from baggage as an attribute (for visibility in trace)
        span.set_attribute("user_id", user_id)

        # Simulate processing
        print(f"Processing payment for user {user_id}")

    # Detach the context to clean up
    detach(token)

# Example usage
if __name__ == "__main__":
    process_payment("user-123")
