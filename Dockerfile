# Base image for processing python tests
FROM python:3.10
# Update "pip" tool
RUN /usr/local/bin/python -m pip install --upgrade pip
# Update "apt-get" package handler and install "jq" for support grid "healthcheck"
RUN apt-get update -y && apt-get install jq -y \
# Install convertor tool from dos related to unix related OS
&& apt-get install dos2unix -y
# Working directory under docker container. Works as start point
WORKDIR /home/ap_test_project_1
# Copy testing preconditions and tools
COPY config.json conftest.py requirements.txt /home/ap_test_project_1
# Copy web pages with methods and locators
COPY pages /home/ap_test_project_1/pages
# Copy selenium tests and features
COPY tests /home/ap_test_project_1/tests
# Copy supporting functionality and tools for reliable test runs
COPY utilities /home/ap_test_project_1/utilities
# Install all required tools: selenium(web communication), pytest(test runs),
# pytest-bdd(BDD), pytest-xdist(parallel runs), allure-pytest(reports)
RUN pip install -r requirements.txt
# Convert to Unix related OS as it was created under Windows 11
RUN dos2unix utilities/selenium_grid_healthcheck/healthcheck.sh
# Perform command right after "docker-compose up" to check selenium grid
CMD sh utilities/selenium_grid_healthcheck/healthcheck.sh