#!/bin/sh

docker login \
    exx1lion-cr.kr.ncr.ntruss.com \
    -u "ED133FDB54933308D17E" \
    -p "DC7B1102A6106231FABA048B34FDC9F42E2D2FD5"
docker pull exx1lion-cr.kr.ncr.ntruss.com/lion-app:latest

docker run -p 8000:8000 -d \
    --name lion-app \
    -v ~/.aws:/root/.aws:ro \
    --env-file .env \
    exx1lion-cr.kr.ncr.ntruss.com/lion-app:latest