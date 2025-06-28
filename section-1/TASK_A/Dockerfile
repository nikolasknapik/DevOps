FROM alpine:3.20
RUN apk add --no-cache curl unzip bash
RUN curl -LO https://releases.hashicorp.com/terraform/1.8.4/terraform_1.8.4_linux_amd64.zip && \
    unzip terraform_1.8.4_linux_amd64.zip && \
    mv terraform /usr/local/bin/ && \
    rm terraform_1.8.4_linux_amd64.zip
WORKDIR /workspace
CMD ["terraform", "validate"]
