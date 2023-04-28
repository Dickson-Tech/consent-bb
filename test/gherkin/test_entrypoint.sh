#!/bin/bash

set -e

sleep 2s

docker container \
  run \
  --network host \
  --rm \
  docker.io/jwilder/dockerize \
  -wait tcp://localhost:8888 \
  -wait-retry-interval 2s \
  -timeout 20s \

mkdir -p test-data-volume

docker-compose up --build

mkdir -p ./results
cp ./test_data/results.json ./results/example_result.message
