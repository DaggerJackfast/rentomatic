#!/usr/bin/env bash
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
DOCKER_IMAGE_TAG = $DOCKER_USERNAME/rentomatic:beta.$TRAVIS_BUILD_NUMBER
docker build -t $DOCKER_IMAGE_TAG .
docker push DOCKER_IMAGE_TAG
