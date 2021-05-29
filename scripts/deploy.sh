#!/bin/bash

kubectl delete configmap scripts-config
kubectl delete deployment hello

kubectl apply -f deploy.yaml