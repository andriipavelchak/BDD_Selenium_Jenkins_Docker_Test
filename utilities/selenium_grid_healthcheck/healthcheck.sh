#!/bin/bash
while [ "$( curl -s http://selenium-hub:4444/wd/hub/status | jq -r .value.ready )" != "true" ]
do
	sleep 1
done
# Run tests
python -m pytest --alluredir=/home/ap_test_project_1/reports/allure-results