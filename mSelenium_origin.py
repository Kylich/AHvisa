# Generated by Selenium IDE
# import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

# class TestUntitled():
#   def setup_method(self, method):
driver = webdriver.Firefox()
actions = ActionChains(driver) 

driver.get(r"https://www.vfsvisaservicesrussia.com/onlinevaf-finland?Country=NhRR5Ee0CQYQchCJG6L+TmyspNLVu6Jjk/QOcheOSo9pDuGGZHwtmEl7tuos+PHK&Culture=ru-RU")

# try:
    # driver.get("https://www.vfsvisaservicesrussia.com/OnlineVAF-Finland/Applicant/Page1")
    # select = Select(driver.find_element_by_name('VACLocation'))
# except:
driver.find_element(By.ID, "EmailId").send_keys("kylikov_nikita@mail.ru")
driver.find_element(By.ID, "Password").send_keys("V515eeC938com!")
driver.find_element(By.ID, "CaptchaInputText").click()
input()
driver.find_element(By.ID, "Login").click()

driver.set_window_size(500, 500)

driver.find_element(By.ID, "VACLocation").click()
# 9 | select | id=VACLocation | label=VISA CENTRE OF FINLAND, ST. PETERSBURG | 
dropdown = driver.find_element(By.ID, "VACLocation")
dropdown.find_element(By.XPATH, "//option[. = 'VISA CENTRE OF FINLAND, ST. PETERSBURG']").click()
actions.send_keys(Keys.TAB)
# 10 | click | css=#VACLocation > option:nth-child(9) |  | 
driver.find_element(By.CSS_SELECTOR, "#VACLocation > option:nth-child(9)").click()
actions.send_keys(Keys.TAB)
# 11 | runScript | window.scrollTo(0,306) |  | 
driver.execute_script("window.scrollTo(0,306)")
# 12 | click | id=LastName |  | 
driver.find_element(By.ID, "LastName").click()
actions.send_keys(Keys.TAB)
# 13 | type | id=LastName | kulikov | 
driver.find_element(By.ID, "LastName").send_keys("kulikov")
actions.send_keys(Keys.TAB)
# 14 | type | id=LastNameAtBirth | kulikov | 
driver.find_element(By.ID, "LastNameAtBirth").send_keys("kulikov")
actions.send_keys(Keys.TAB)
# 15 | type | id=FirstName | nikita | 
driver.find_element(By.ID, "FirstName").send_keys("nikita")
actions.send_keys(Keys.TAB)
# 16 | type | id=Patronymic | sergeevich | 
driver.find_element(By.ID, "Patronymic").send_keys("sergeevich")
actions.send_keys(Keys.TAB)
# 17 | type | id=DateOfBirth | 05/02/1988 | 
driver.find_element(By.ID, "DateOfBirth").send_keys("05021988")
actions.send_keys(Keys.TAB)
# 18 | type | id=PlaceOfBirth | leningrad | 
driver.find_element(By.ID, "PlaceOfBirth").send_keys("leningrad")
actions.send_keys(Keys.TAB)
# 21 | select | id=CountryOfBirth | label=SOVIET UNION | 
dropdown = driver.find_element(By.ID, "CountryOfBirth")
dropdown.find_element(By.XPATH, "//option[. = 'SOVIET UNION']").click()
actions.send_keys(Keys.TAB)
# 22 | runScript | window.scrollTo(0,306) |  | 
driver.execute_script("window.scrollTo(0,306)")
# 24 | select | id=CurrentNationality | label=RUSSIAN FEDERATION | 
dropdown = driver.find_element(By.ID, "CurrentNationality")
dropdown.find_element(By.XPATH, "//option[. = 'RUSSIAN FEDERATION']").click()
actions.send_keys(Keys.TAB)
# 25 | runScript | window.scrollTo(0,306) |  | 
driver.execute_script("window.scrollTo(0,306)")
# 28 | select | id=NationalityAtBirth | label=SOVIET UNION | 
dropdown = driver.find_element(By.ID, "NationalityAtBirth")
dropdown.find_element(By.XPATH, "//option[. = 'SOVIET UNION']").click()
actions.send_keys(Keys.TAB)
# 29 | select | id=Gender | label=MALE | 
dropdown = driver.find_element(By.ID, "Gender")
dropdown.find_element(By.XPATH, "//option[. = 'MALE']").click()
actions.send_keys(Keys.TAB)
# 30 | runScript | window.scrollTo(0,372) |  | 
driver.execute_script("window.scrollTo(0,372)")
# 32 | select | id=MaritalStatus | label=SINGLE | 
dropdown = driver.find_element(By.ID, "MaritalStatus")
dropdown.find_element(By.XPATH, "//option[. = 'SINGLE']").click()
actions.send_keys(Keys.TAB)
# 33 | runScript | window.scrollTo(0,432) |  | 
driver.execute_script("window.scrollTo(0,432)")
# 35 | select | id=PassportTypeId | label=ORDINARY PASSPORT | 
dropdown = driver.find_element(By.ID, "PassportTypeId")
dropdown.find_element(By.XPATH, "//option[. = 'ORDINARY PASSPORT']").click()
actions.send_keys(Keys.TAB)
# 36 | runScript | window.scrollTo(0,716) |  | 
driver.execute_script("window.scrollTo(0,716)")
# 37 | type | id=passport | 717580417 | 
driver.find_element(By.ID, "passport").send_keys("717580417")
actions.send_keys(Keys.TAB)
# 38 | type | id=confirmpassport | 717580417 | 
driver.find_element(By.ID, "confirmpassport").send_keys("717580417")
actions.send_keys(Keys.TAB)
# 39 | type | id=IssueDate | 03/02/2012 | 
driver.find_element(By.ID, "IssueDate").send_keys("03022012")
actions.send_keys(Keys.TAB)
# 40 | type | id=ExpiryDate | 03/02/2022 | 
driver.find_element(By.ID, "ExpiryDate").send_keys("03022022")
actions.send_keys(Keys.TAB)
# 42 | select | id=IssuedByCountry | label=RUSSIAN FEDERATION | 
dropdown = driver.find_element(By.ID, "IssuedByCountry")
dropdown.find_element(By.XPATH, "//option[. = 'RUSSIAN FEDERATION']").click()
actions.send_keys(Keys.TAB)
# 43 | runScript | window.scrollTo(0,967) |  | 
driver.execute_script("window.scrollTo(0,967)")
# 44 | type | id=PassportIssuedBy | fms 78036 | 
driver.find_element(By.ID, "PassportIssuedBy").send_keys("fms 78036")
actions.send_keys(Keys.TAB)
# 45 | click | id=next |  | 
driver.find_element(By.ID, "next").click()
# 46 | runScript | window.scrollTo(0,306) |  | 
# driver.execute_script("window.scrollTo(0,306)")
# 49 | click | id=Address |  | 
# driver.find_element(By.ID, "Address").click()
# 50 | type | id=Address | pr lesnoi 61 1 100 | 
driver.find_element(By.ID, "Address").send_keys("pr lesnoi 61 1 100")
actions.send_keys(Keys.TAB)
# 51 | type | id=PostalCode | 0 | 
driver.find_element(By.ID, "PostalCode").send_keys("0")
actions.send_keys(Keys.TAB)
# 52 | type | id=City | sankt-peterburg | 
driver.find_element(By.ID, "City").send_keys("sankt-peterburg")
actions.send_keys(Keys.TAB)
# 54 | select | id=CountryId | label=RUSSIAN FEDERATION | 
dropdown = driver.find_element(By.ID, "CountryId")
dropdown.find_element(By.XPATH, "//option[. = 'RUSSIAN FEDERATION']").click()
actions.send_keys(Keys.TAB)
# 55 | runScript | window.scrollTo(0,306) |  | 
driver.execute_script("window.scrollTo(0,306)")
# 56 | type | id=ContactNumber | 79502203226 | 
driver.find_element(By.ID, "ContactNumber").send_keys("79502203226")
actions.send_keys(Keys.TAB)
# 57 | runScript | window.scrollTo(0,714) |  | 
driver.execute_script("window.scrollTo(0,714)")
# 58 | click | id=ddlCurrentOccupation |  | 
driver.find_element(By.ID, "ddlCurrentOccupation").click()
actions.send_keys(Keys.TAB)
# 59 | select | id=ddlCurrentOccupation | label=BLUE-COLLAR WORKER | 
dropdown = driver.find_element(By.ID, "ddlCurrentOccupation")
dropdown.find_element(By.XPATH, "//option[. = 'BLUE-COLLAR WORKER']").click()
actions.send_keys(Keys.TAB)
# 60 | click | css=#ddlCurrentOccupation > option:nth-child(7) |  | 
driver.find_element(By.CSS_SELECTOR, "#ddlCurrentOccupation > option:nth-child(7)").click()
# 61 | runScript | window.scrollTo(0,714) |  | 
driver.execute_script("window.scrollTo(0,714)")
# 62 | type | id=txtEmployer | ooo ekskpress pochta | 
driver.find_element(By.ID, "txtEmployer").send_keys("ooo express post")
actions.send_keys(Keys.TAB)
# 63 | type | id=OccupationAddress | pr ligovskii 154 | 
driver.find_element(By.ID, "OccupationAddress").send_keys("pr ligovskii 50/12")
actions.send_keys(Keys.TAB)
# 64 | type | id=OccupationPostalCode | 0 | 
driver.find_element(By.ID, "OccupationPostalCode").send_keys("0")
# 65 | type | id=OccupationCity | sankt-peterburg | 
driver.find_element(By.ID, "OccupationCity").send_keys("sankt-peterburg")
# 67 | select | id=OccupationCountryId | label=RUSSIAN FEDERATION | 
dropdown = driver.find_element(By.ID, "OccupationCountryId")
dropdown.find_element(By.XPATH, "//option[. = 'RUSSIAN FEDERATION']").click()
# 68 | runScript | window.scrollTo(0,714) |  | 
driver.execute_script("window.scrollTo(0,714)")
# 69 | type | id=OccupationContactNumber | 78122325903 | 
driver.find_element(By.ID, "OccupationContactNumber").send_keys("78122325903")
# 70 | click | id=next |  | 
driver.find_element(By.ID, "next").click()
# 71 | runScript | window.scrollTo(0,23) |  | 
driver.execute_script("window.scrollTo(0,23)")
# 72 | click | id=ddlMainTravelPurpose |  | 
driver.find_element(By.ID, "ddlMainTravelPurpose").click()
# 73 | select | id=ddlMainTravelPurpose | label=TOURISM | 
dropdown = driver.find_element(By.ID, "ddlMainTravelPurpose")
dropdown.find_element(By.XPATH, "//option[. = 'TOURISM']").click()
# 74 | click | css=#ddlMainTravelPurpose > option:nth-child(10) |  | 
driver.find_element(By.CSS_SELECTOR, "#ddlMainTravelPurpose > option:nth-child(10)").click()
# 75 | runScript | window.scrollTo(0,306) |  | 
driver.execute_script("window.scrollTo(0,306)")
# 76 | click | id=ddlMainDestinationId |  | 
driver.find_element(By.ID, "ddlMainDestinationId").click()
# 77 | select | id=ddlMainDestinationId | label=FINLAND | 
dropdown = driver.find_element(By.ID, "ddlMainDestinationId")
dropdown.find_element(By.XPATH, "//option[. = 'FINLAND']").click()
# 78 | click | css=#ddlMainDestinationId > option:nth-child(9) |  | 
driver.find_element(By.CSS_SELECTOR, "#ddlMainDestinationId > option:nth-child(9)").click()
# 79 | runScript | window.scrollTo(0,306) |  | 
driver.execute_script("window.scrollTo(0,306)")
# 80 | click | id=StateOfFirstEntry |  | 
driver.find_element(By.ID, "StateOfFirstEntry").click()
# 81 | select | id=StateOfFirstEntry | label=FINLAND | 
dropdown = driver.find_element(By.ID, "StateOfFirstEntry")
dropdown.find_element(By.XPATH, "//option[. = 'FINLAND']").click()
# 82 | click | css=#StateOfFirstEntry > option:nth-child(7) |  | 
driver.find_element(By.CSS_SELECTOR, "#StateOfFirstEntry > option:nth-child(7)").click()
# 83 | click | id=Page3 |  | 
driver.find_element(By.ID, "Page3").click()
# 84 | click | id=NumberOfEntries |  | 
driver.find_element(By.ID, "NumberOfEntries").click()
# 85 | select | id=NumberOfEntries | label=MULTI | 
dropdown = driver.find_element(By.ID, "NumberOfEntries")
dropdown.find_element(By.XPATH, "//option[. = 'MULTI']").click()
# 86 | click | css=#NumberOfEntries > option:nth-child(4) |  | 
driver.find_element(By.CSS_SELECTOR, "#NumberOfEntries > option:nth-child(4)").click()
# 87 | runScript | window.scrollTo(0,510) |  | 
driver.execute_script("window.scrollTo(0,510)")
# 88 | click | id=DurationOfIntendedStay |  | 
driver.find_element(By.ID, "DurationOfIntendedStay").click()
# 89 | mouseOver | id=SchengenVisasIssuesDuringYes |  | 
element = driver.find_element(By.ID, "SchengenVisasIssuesDuringYes")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
# 90 | mouseOut | id=SchengenVisasIssuesDuringYes |  | 
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
actions.move_to_element(element, 0, 0).perform()
# 91 | mouseOver | id=SchengenVisasIssuesDuringYes |  | 
element = driver.find_element(By.ID, "SchengenVisasIssuesDuringYes")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
# 92 | mouseOut | id=SchengenVisasIssuesDuringYes |  | 
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
actions.move_to_element(element, 0, 0).perform()
# 93 | type | id=DurationOfIntendedStay | 90 | 
driver.find_element(By.ID, "DurationOfIntendedStay").send_keys("90")
# 96 | mouseOver | id=SchengenVisasIssuesDuringYes |  | 
element = driver.find_element(By.ID, "SchengenVisasIssuesDuringYes")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
# 97 | click | id=SchengenVisasIssuesDuringYes |  | 
driver.find_element(By.ID, "SchengenVisasIssuesDuringYes").click()
# 98 | mouseOut | id=SchengenVisasIssuesDuringYes |  | 
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
actions.move_to_element(element, 0, 0).perform()
# 99 | mouseOver | id=SchengenVisasIssuesDuringYes |  | 
element = driver.find_element(By.ID, "SchengenVisasIssuesDuringYes")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
# 100 | mouseOut | id=SchengenVisasIssuesDuringYes |  | 
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
actions.move_to_element(element, 0, 0).perform()
# 101 | mouseUp | id=FromDate1 |  | 
element = driver.find_element(By.ID, "FromDate1")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
# 102 | click | id=FromDate1 |  | 
driver.find_element(By.ID, "FromDate1").click()
# 103 | type | id=FromDate1 | 01/06/2017 | 
driver.find_element(By.ID, "FromDate1").send_keys("01062017")
# 104 | type | id=ToDate1 | 31/05/2019 | 
driver.find_element(By.ID, "ToDate1").send_keys("31052019")
# 105 | click | id=FingerprintsCollectedYes |  | 
driver.find_element(By.ID, "FingerprintsCollectedYes").click()
# 106 | click | id=DOC |  | 
driver.find_element(By.ID, "DOC").click()
# 107 | type | id=DOC | 20/05/2017 | 
driver.find_element(By.ID, "DOC").send_keys("20052017")
# 108 | click | id=IntentedDateOfArrival |  | 
driver.find_element(By.ID, "IntentedDateOfArrival").click()
# 109 | type | id=IntentedDateOfArrival | 21/09/2019 | 
driver.find_element(By.ID, "IntentedDateOfArrival").send_keys("21092019")
# 110 | type | id=IntentedDateOfDeparture | 20/09/2021 | 
driver.find_element(By.ID, "IntentedDateOfDeparture").send_keys("20092021")
# 111 | click | id=next |  | 
driver.find_element(By.ID, "next").click()
# 112 | runScript | window.scrollTo(0,306) |  | 
driver.execute_script("window.scrollTo(0,306)")
# 113 | click | id=ddlinvitingid |  | 
driver.find_element(By.ID, "ddlinvitingid").click()
# 114 | select | id=ddlinvitingid | label=NO INVITATION | 
dropdown = driver.find_element(By.ID, "ddlinvitingid")
dropdown.find_element(By.XPATH, "//option[. = 'NO INVITATION']").click()
# 117 | click | id=1 |  | 
driver.find_element(By.ID, "1").click()
# 118 | click | id=CASH |  | 
driver.find_element(By.ID, "CASH").click()
# 120 | click | id=next |  | 
driver.find_element(By.ID, "next").click()
# 121 | runScript | window.scrollTo(0,201) |  | 
driver.execute_script("window.scrollTo(0,201)")
# 122 | click | id=additionalInfo |  | 
driver.find_element(By.ID, "additionalInfo").click()
# 123 | type | id=additionalInfo | helsinki imatra lappeenranta | 
driver.find_element(By.ID, "additionalInfo").send_keys("helsinki imatra lappeenranta")
# 124 | click | name=SAVE |  | 
driver.find_element(By.NAME, "SAVE").click()
# 125 | mouseOver | id=rdbYes |  | 
element = driver.find_element(By.ID, "rdbYes")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
# 126 | mouseOut | id=rdbYes |  | 
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
actions.move_to_element(element, 0, 0).perform()

