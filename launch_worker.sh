#!/bin/bash

. env/bin/activate
cd src
celery -A dummy worker -l info
