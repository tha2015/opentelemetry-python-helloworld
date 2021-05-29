#!/bin/bash

kubectl delete configmap scripts-config
kubectl delete deployment hello

cat deploy.yaml | sed -e 's/--trace/--debug/' | kubectl apply -f -