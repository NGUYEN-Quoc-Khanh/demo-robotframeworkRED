*** Settings *** 
Library    ../../../apps/web_apps/web_functions.py       WITH NAME    browser_01

Test Teardown    browser_01.Close Browser
*** Variables ***
${url}    http://11.11.7.10/login
${url1}    http://10.128.220.229:81/

*** Test Cases ***
ATDA001 Account page - Verify create a new account with invalid information - WIN1
    browser_01.Open Browser     ${url1}
    Sleep    5s
    #browser_01.Close Browser