#!/bin/bash

# Open browser
open http://localhost:8000/ventureinsight/home

# Run Docker container
# docker run -v $(pwd):/venture-insight -p 8000:8000 --name ventureinsight ventureinsight
docker run -v $(pwd):/venture-insight -p 8000:8000 --name venture-insight ventureinsight.azurecr.io/venture-insight
# -v tag allows sync upon save between folder in local machine to a folder in docker container
# $(pwd) Mac/Linux, %cd% Windows command shell, ${pwd} Windows PowerShell