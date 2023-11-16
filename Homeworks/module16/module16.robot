*** Settings ***
Library    SeleniumLibrary
Library    Helpers.py

*** Variables ***
${BROWSER}    chrome
${URL}        https://www.demoblaze.com/
${USERNAME}   notabot
${PASSWORD}   1234

*** Test Cases ***
Login Test
    [Setup]    Setup
    Click Element    id=login2  #step1
    Wait Until Element Is Visible   id=loginusername
    Page Should Contain Element   id=loginusername  #step1 expected result
    Page Should Contain Element   id=loginpassword  #step1 expected result
    Input Text    id=loginusername    ${USERNAME}
    Input Password    id=loginpassword    ${PASSWORD}
    Click Button    xpath=//button[@onclick='logIn()']  #step2
    Wait Until Element Is Visible   id=logout2
    Page Should Contain Element   id=logout2    #step2 expected result
    Page Should Contain    Welcome ${USERNAME}  #step2 expected result
    [Teardown]      Teardown

Cart Test
    [Setup]     Login
    ${price_elems}=     Get Element Count   xpath=//h5
    Click Element    xpath=//a[@onclick="byCat('monitor')"]  #step1
    Wait Until Page Does Not Contain    Iphone
    ${price_filtered}=  Get Element Count   xpath=//h5
    Should Be True    ${price_filtered}<${price_elems}
    ${prices}=  Get WebElements    xpath=//h5
    ${highest}=     find_max_price      ${prices}
    ${title}=   Get Text    xpath=//h5[text()='${highest}']/preceding-sibling::h4/a
    Click Element    xpath=//h5[text()='${highest}']/preceding-sibling::h4/a    #step2
    Wait Until Element Is Visible   xpath=//a[@onclick='addToCart(10)']
    Page Should Contain     ${title}    #step2 expected result
    Page Should Contain     ${highest}  #step2 expected result
    Click Element    xpath=//a[@onclick='addToCart(10)']    #step3
    Click Element    id=cartur  #step4
    Wait Until Element Is Visible   xpath=//td[text()='${title}']
    Page Should Contain     ${title}    #step4 expected result
    Page Should Contain     ${highest}[1:]    #step4 expected result
    [Teardown]      Teardown

*** Keywords ***
Setup
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Login
    Setup
    Click Element    id=login2  #step1
    Wait Until Element Is Visible   id=loginusername
    Input Text    id=loginusername    ${USERNAME}
    Input Password    id=loginpassword    ${PASSWORD}
    Click Button    xpath=//button[@onclick='logIn()']
    Wait Until Element Is Visible   id=logout2

Teardown
    Close Browser

