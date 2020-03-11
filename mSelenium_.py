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
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Firefox()
driver.get(r"https://www.vfsvisaservicesrussia.com/onlinevaf-finland?Country=NhRR5Ee0CQYQchCJG6L+TmyspNLVu6Jjk/QOcheOSo9pDuGGZHwtmEl7tuos+PHK&Culture=ru-RU")
driver.set_window_size(500, 1000)
# try:
    # driver.get("https://www.vfsvisaservicesrussia.com/OnlineVAF-Finland/Applicant/Page1")
    # select = Select(driver.find_element_by_name('VACLocation'))
# except:
driver.find_element(By.ID, "EmailId").send_keys("kylikov_nikita@mail.ru")
driver.find_element(By.ID, "Password").send_keys("V515eeC938com!")
driver.find_element(By.ID, "CaptchaInputText").click()
input()
driver.find_element(By.ID, "Login").click()
time.sleep(2)

dropdown = driver.find_element(By.ID, "VACLocation")
dropdown.find_element(By.XPATH, "//option[. = 'VISA CENTRE OF FINLAND, ST. PETERSBURG']").click()
driver.find_element(By.ID, "LastName").send_keys("KULIKOV")
driver.find_element(By.ID, "LastNameAtBirth").send_keys("KULIKOV")
driver.find_element(By.CSS_SELECTOR, "#CurrentNationality > option:nth-child(229)").click()
driver.find_element(By.ID, "FirstName").send_keys("NIKITA")
driver.find_element(By.ID, "Patronymic").send_keys("SERGEEVICH")
driver.find_element(By.CSS_SELECTOR, "#NationalityAtBirth > option:nth-child(261)").click()
driver.find_element(By.ID, "DateOfBirth").send_keys("05021988")
driver.find_element(By.ID, "PlaceOfBirth").send_keys("LENINGRAD")
driver.find_element(By.CSS_SELECTOR, "#CountryOfBirth > option:nth-child(261)").click()
dropdown = driver.find_element(By.ID, "Gender")
dropdown.find_element(By.XPATH, "//option[. = 'MALE']").click()
dropdown = driver.find_element(By.ID, "MaritalStatus")
dropdown.find_element(By.XPATH, "//option[. = 'SINGLE']").click()
dropdown = driver.find_element(By.ID, "PassportTypeId")
dropdown.find_element(By.XPATH, "//option[. = 'ORDINARY PASSPORT']").click()
driver.find_element(By.ID, "passport").send_keys("717580417")
driver.find_element(By.ID, "confirmpassport").send_keys("717580417")
driver.find_element(By.ID, "IssueDate").send_keys("03022012")
driver.find_element(By.ID, "ExpiryDate").send_keys("03022022")
driver.find_element(By.CSS_SELECTOR, "#IssuedByCountry > option:nth-child(229)").click()
driver.find_element(By.ID, "PassportIssuedBy").send_keys("FMS78036")
# 23 | click | id=next |  | 
driver.find_element(By.ID, "next").click()
# 24 | type | id=Address | lesnoy 61/1 | 
driver.find_element(By.ID, "Address").send_keys("lesnoy 61/1")
# 25 | type | id=PostalCode | 194100 | 
driver.find_element(By.ID, "PostalCode").send_keys("194100")
# 26 | type | id=City | stpeterburg | 
driver.find_element(By.ID, "City").send_keys("stpeterburg")
# 27 | select | id=CountryId | label=RUSSIAN FEDERATION | 
driver.find_element(By.CSS_SELECTOR, "#CountryId > option:nth-child(184)").click()
# dropdown = driver.find_element(By.ID, "CountryId")
# dropdown.find_element(By.XPATH, "//option[. = 'RUSSIAN FEDERATION']").click()
# 28 | type | id=ContactNumber | +79502203226 | 
driver.find_element(By.ID, "ContactNumber").send_keys("79502203226")
# 29 | type | id=EmailId | kylikov_nikita@mail.ru | 
driver.find_element(By.ID, "EmailId").send_keys("kylikov_nikita@mail.ru")
# 30 | select | id=ddlCurrentOccupation | label=OTHERS | 
dropdown = driver.find_element(By.ID, "ddlCurrentOccupation")
dropdown.find_element(By.XPATH, "//option[. = 'OTHERS']").click()
# 31 | type | id=OtherOccupation | MAIL | 
driver.find_element(By.ID, "OtherOccupation").send_keys("MAIL")
# 32 | type | id=txtEmployer | ExpressPost | 
driver.find_element(By.ID, "txtEmployer").send_keys("ExpressPost")
# 33 | type | id=OccupationAddress | LIGOVSKIY 50 | 
driver.find_element(By.ID, "OccupationAddress").send_keys("LIGOVSKIY 50")
# 34 | type | id=OccupationCity | stpeterburg | 
driver.find_element(By.ID, "OccupationCity").send_keys("stpeterburg")
# 35 | select | id=OccupationCountryId | label=RUSSIAN FEDERATION | 
driver.find_element(By.CSS_SELECTOR, "#OccupationCountryId > option:nth-child(184)").click()
# dropdown = driver.find_element(By.ID, "OccupationCountryId")
# dropdown.find_element(By.XPATH, "//option[. = 'RUSSIAN FEDERATION']").click()
# 36 | type | id=OccupationContactNumber | 88126330225 | 
driver.find_element(By.ID, "OccupationContactNumber").send_keys("88126330225")
# 37 | click | id=next |  | 
driver.find_element(By.ID, "next").click()
# 38 | select | id=ddlMainTravelPurpose | label=TOURISM | 
dropdown = driver.find_element(By.ID, "ddlMainTravelPurpose")
dropdown.find_element(By.XPATH, "//option[. = 'TOURISM']").click()
driver.find_element(By.CSS_SELECTOR, "#ddlMainDestinationId > option:nth-child(9)").click()
# 39 | select | id=ddlMainDestinationId | label=FINLAND | 
# dropdown = driver.find_element(By.ID, "ddlMainDestinationId")
# dropdown.find_element(By.XPATH, "//option[. = 'FINLAND']").click()
# 40 | select | id=StateOfFirstEntry | label=FINLAND | 
driver.find_element(By.CSS_SELECTOR, "#StateOfFirstEntry > option:nth-child(7)").click()
# dropdown = driver.find_element(By.ID, "StateOfFirstEntry")
# dropdown.find_element(By.XPATH, "//option[. = 'FINLAND']").click()
# 41 | select | id=NumberOfEntries | label=MULTI | 
dropdown = driver.find_element(By.ID, "NumberOfEntries")
dropdown.find_element(By.XPATH, "//option[. = 'MULTI']").click()
# 42 | type | id=DurationOfIntendedStay | 30 | 
driver.find_element(By.ID, "DurationOfIntendedStay").send_keys("30")
# 43 | click | id=SchengenVisasIssuesDuringYes |  | 
driver.find_element(By.ID, "SchengenVisasIssuesDuringYes").click()
# 44 | type | id=FromDate1 | 01/06/2017 | 
driver.find_element(By.ID, "FromDate1").send_keys("01062017")
# 45 | type | id=ToDate1 | 31/05/2019 | 
driver.find_element(By.ID, "ToDate1").send_keys("31052019")
# 46 | click | id=FingerprintsCollectedYes |  | 
driver.find_element(By.ID, "FingerprintsCollectedYes").click()
# 47 | type | id=IntentedDateOfArrival | 01/06/2020 | 
driver.find_element(By.ID, "IntentedDateOfArrival").send_keys("01062020")
# 48 | type | id=IntentedDateOfDeparture | 15/06/2020 | 
driver.find_element(By.ID, "IntentedDateOfDeparture").send_keys("15062020")
# 49 | click | id=next |  | 
driver.find_element(By.ID, "next").click()
# 50 | select | id=ddlinvitingid | label=NO INVITATION | 
dropdown = driver.find_element(By.ID, "ddlinvitingid")
dropdown.find_element(By.XPATH, "//option[. = 'NO INVITATION']").click()
# 51 | click | id=1 |  | 
driver.find_element(By.ID, "1").click()
# 52 | click | id=CASH |  | 
driver.find_element(By.ID, "CASH").click()
# 53 | click | id=rdominortru |  | 
driver.find_element(By.ID, "rdominortru").click()
# 54 | click | id=next |  | 
driver.find_element(By.ID, "next").click()
# 55 | click | name=SAVE |  | 
driver.find_element(By.NAME, "SAVE").click()
# 56 | mouseOver | id=rdbYes |  | 
# element = driver.find_element(By.ID, "rdbYes")
# actions = ActionChains(driver)
# actions.move_to_element(element).perform()
# 57 | click | id=rdbYes |  | 
driver.find_element(By.ID, "rdbYes").click()
# 58 | mouseOut | id=rdbYes |  | 
# element = driver.find_element(By.CSS_SELECTOR, "body")
# actions = ActionChains(driver)
# actions.move_to_element(element, 0, 0).perform()
# 59 | click | id=rdbTourist |  | 
driver.find_element(By.ID, "rdbTourist").click()
# 60 | click | id=btnSubmit |  | 
driver.find_element(By.ID, "btnSubmit").click()
