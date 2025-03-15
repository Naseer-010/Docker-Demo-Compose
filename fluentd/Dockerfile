# Use the official Fluentd image as the base
FROM fluent/fluentd:v1.15-debian-1

# Switch to root user for installing dependencies
USER root

# Install necessary system dependencies
RUN apt-get update && apt-get install -y build-essential ruby-dev

# Install required Fluentd plugins
RUN gem install \
    fluent-plugin-parser \
    fluent-plugin-rewrite-tag-filter \
    fluent-plugin-prometheus 

# Copy the custom Fluentd configuration file
COPY fluentd.conf /fluentd/etc/fluentd.conf

# Ensure correct permissions for Fluentd directories
RUN mkdir -p /fluentd/log && \
    chown -R fluent:fluent /fluentd /fluentd/etc /fluentd/log

# Switch back to the default Fluentd user


# Start Fluentd
CMD ["fluentd", "-c", "/fluentd/etc/fluentd.conf"]
