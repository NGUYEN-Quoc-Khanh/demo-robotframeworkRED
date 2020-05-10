*** Settings *** 
Library    ../../../apps/web_apps/web_functions.py       WITH NAME    browser_01

Test Teardown    browser_01.Close Browser
*** Variables ***
${url}    http://11.11.7.10/login
${url1}    http://10.128.220.229:81/
${message}    project with this name already exists.

*** Test Cases ***
ADA014 Project Page_Edit project with existed name in the newly created project
    Log To Console    Start Login user
    Log To Console    1. Lauch browser and go to url http://10.128.220.229:81/        
    browser_01.Open Browser     ${url1}
    #Sleep    5s
    Log To Console    2. Verify Login page
    browser_01.Verify Login Page
    Log To Console    3. Login user        
    browser_01.Input Username Password Login Page    nqkhanh    1234
    #Sleep    3s
    browser_01.Click Login Button
    #sSleep    5s
    Log To Console    4. Verify user login
    browser_01.Verify Dash Board Page       
    Sleep    2s
    browser_01.Click New Project
    Sleep    1s
    browser_01.Input Project    ADA014    ABC
    Sleep    1s
    browser_01.Click Create Edit Project
    Sleep    1s    
    browser_01.Click New Project
    Sleep    1s
    browser_01.Input Project    ADA014NEW    ABC
    Sleep    1s
    browser_01.Click Create Edit Project
    Sleep    1s
    browser_01.Click Project To Edit    ADA014NEW
    Sleep    1s
    browser_01.Input Project    ADA014    Description of ADA014 new
    Sleep    1s 
    browser_01.Click Create Edit Project
    Sleep    1s
    browser_01.Verify Message Project Name    ${message}
    Sleep    1s
    browser_01.User Log Out 