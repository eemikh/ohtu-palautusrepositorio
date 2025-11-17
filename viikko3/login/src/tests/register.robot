*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
     Set Username  kalle
     Set Password  kalle123
     Set Password Confirmation  kalle123
     Click Button  Register
     Register Should Succeed

Register With Too Short Username And Valid Password
     Set Username  k
     Set Password  kalle123
     Set Password Confirmation  kalle123
     Click Button  Register
     Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
     Set Username  kalle
     Set Password  k
     Set Password Confirmation  k
     Click Button  Register
     Register Should Fail With Message  Password too short

Register With Valid Username And Invalid Password
     Set Username  kalle
     Set Password  kkkkkkkkkkkkkkk
     Set Password Confirmation  kkkkkkkkkkkkkkk
     Click Button  Register
     Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
     Set Username  kalle
     Set Password  kalle123
     Set Password Confirmation  321ellak
     Click Button  Register
     Register Should Fail With Message  Password and password confirmation do not match

Register With Username That Is Already In Use
     Set Username  kalle
     Set Password  kalle123
     Set Password Confirmation  kalle123
     Click Button  Register
     Go To Register Page
     Set Username  kalle
     Set Password  kalle123
     Set Password Confirmation  kalle123
     Click Button  Register
     Register Should Fail With Message  Username already in use

*** Keywords ***
Reset Application And Go To Register Page
    Reset Application
    Go To Register Page

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}
