#!/usr/bin/env bash
set -e
py.test --cov-report term-missing --cov=rentomatic
