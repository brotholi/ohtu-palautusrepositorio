*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go to Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kaarina
    Set Password  kaarina123
    Set Password Confirmation  kaarina123
    Submit Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kaija123
    Submit Register Credentials
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Invalid Password
    Set Username  kaija
    Set Password  ka
    Submit Register Credentials
    Register Should Fail With Message  Password must be at least 8 characters long and contain numbers

Register With Nonmatching Password And Password Confirmation
    Set Username  kaija
    Set Password  kaija123
    Set Password Confirmation  kaisa12
    Submit Register Credentials
    Register Should Fail With Message  Password and password confirmation do not match

Login After Successful Registration
    Set Username  katri
    Set Password  katri123
    Set Password Confirmation  katri123
    Submit Register Credentials
    Register Should Succeed
    Logout
    Set Username  katri
    Set Password  katri123
    Submit Credentials
    Login Should Succeed
    
Login After Failed Registration
    Set Username  kaapo
    Set Password  kaapoonparas
    Set Password Confirmation  kaapoonparas
    Submit Register Credentials
    Register Should Fail With Message  Password must be at least 8 characters long and contain numbers
    Go To Login Page
    Set Username  kaapo
    Set Password  kaapoonparas
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Register Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}
