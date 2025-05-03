Task: Write a Python snippet that:

    - Uses OpenTelemetry SDK to manually create a span inside a function process_payment(user_id).
    - Adds baggage (user_id) and a custom attribute (payment_method).
    - Sends trace data to a locally running OTEL Collector via OTLP.

Focus: OpenTelemetry SDK, span creation, baggage, OTLP exporter setup.

-------

Requirements:

- Make sure you have the required packages installed:

    pip install opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp

- Running python app

    python payment-service.py

Note:

- The OTLP exporter defaults to gRPC at port 4317.

- You must have a locally running OTEL Collector configured to receive OTLP data on localhost:4317.

- Baggage is not automatically added as span attributes; you can extract it and manually add it as needed.