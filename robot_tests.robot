*** Settings ***
Library    SPM2

*** Test Cases ***
TestHaeLomakkeesta
    [Documentation]    Testaa T-pisteen ja persentiilin hakemista lomakkeesta
    [Tags]    Lomake
    ${t_piste}  ${persentiili}=    SPM2.hae_lomakkeesta    lapsi  kodin lomake  näkö  16
    Should Be Equal As Numbers    ${t_piste}    60
    Should Not Be Empty    ${persentiili}
    Should Be Equal    ${persentiili}    84