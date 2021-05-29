#!/bin/bash


export FLASK_APP=./server.py

while test $# -gt 0
do
    case "$1" in
        --none)
            echo "option none"
            python3 -m flask run --host=0.0.0.0 --port=8000

            ;;
        --debug)
            echo "option debug"
            pip3 install --user debugpy
            export PATH=$HOME/.local/bin:$PATH

            python3 -m debugpy --listen 0.0.0.0:5678 -m flask run --host=0.0.0.0 --port=8000
            ;;
        --trace)
            echo "option trace"
            pip3 install --user opentelemetry-api==1.2.0 opentelemetry-sdk==1.2.0 opentelemetry-instrumentation==0.21b0 opentelemetry-distro==0.21b0  opentelemetry-exporter-otlp==1.2.0
            pip3 install --user opentelemetry-instrumentation-flask==0.21b0 opentelemetry-instrumentation-grpc==0.21b0 opentelemetry-instrumentation-jinja2==0.21b0 opentelemetry-instrumentation-requests==0.21b0 opentelemetry-instrumentation-sqlite3==0.21b0 opentelemetry-instrumentation-urllib==0.21b0
            export PATH=$HOME/.local/bin:$PATH

            #exec opentelemetry-bootstrap
            #exec opentelemetry-bootstrap --action=install


            opentelemetry-instrument python3 -m flask run --no-reload --host=0.0.0.0 --port=8000
            ;;
        --*)
            echo "bad option $1"
            ;;
        *) echo "argument $1"
            ;;
    esac
    shift
done


exit 0