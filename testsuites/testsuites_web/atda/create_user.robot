*** Settings *** 
Library    ../../../apps/web_apps/web_functions.py       WITH NAME    browser_01

Test Teardown    browser_01.Close Browser
*** Variables ***
${url}    http://11.11.7.10/login
${url1}    http://10.128.220.229:81/

*** Test Cases ***
LOGIN USER
    Log To Console    Start Login user
    Log To Console    1. Lauch browser and go to url http://10.128.220.229:81/        
    browser_01.Open Browser     ${url}
    #Sleep    5s
    Log To Console    2. Navigate to Register page to create new user
    browser_01.Nav To Register Page
    Log To Console    3. Verify Register page
    browser_01.Verify Loading Register Page
    Log To Console    4. Input User value to register            
    browser_01.Input Username Psd Create Account Page    nqkhanh    nqkhanh@tma.com.vn    Quoc-Khanh Nguyen    1234
    Sleep    3s
    Log To Console    5. Start Creating user    
    browser_01.Click Register Button
    Sleep    10s    