*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kaisa  kaisa123
    Output Should Contain  New user registered
    
Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  Username already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kaisu123
    Output Should Contain  Username must be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  123  kaisu123
    Output Should Contain  Username must consist of only a-z characters

Register With Valid Username And Too Short Password
    Input Credentials  kaisu  ka
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kaisu  kaisukaisu
    Output Should Contain  Password must contain at least one number

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command