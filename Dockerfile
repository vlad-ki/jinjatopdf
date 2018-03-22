FROM python:3.6-alpine3.6

RUN apk add --update libstdc++ glib libxrender libssl1.0 libxext freetype fontconfig && \
    rm -rf /var/cache/apk/*

ADD http://media.ticketscloud.s3.amazonaws.com/__deploy__/wkhtmltopdf /usr/local/bin/wkhtmltopdf
RUN chmod +x /usr/local/bin/wkhtmltopdf

COPY . /srv/src
RUN pip install --no-cache -U pip && \
    pip install --no-cache /srv/src

ENTRYPOINT ["/usr/bin/env", "jinjatopdf"]