import datetime
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys
from selenium.common.exceptions import NoSuchElementException
import WeGoStudy_locators as locators
#from webdriver_manager.chrome import ChromeDriverManager

# AWS HEADLESS MODE
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

# s = Service(executable_path='../chromedriver.exe')
# driver = webdriver.Chrome(service=s)

# s=Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=s)




def setUp():
    print(f'Test starts at {datetime.datetime.now()}.')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.app_url)

    if driver.current_url == locators.app_url and locators.homepage_title in driver.title:
        print(f'{locators.app} website launched successfully!')
        print(f'{locators.app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.app} did not launch successfully, please check your code and launch again!')
        print(f'Current URL: {driver.current_url}, Current page title: {driver.title}.')
        driver.close()
        driver.quit()


def tearDown():
    if driver is not None:
        print(f'---------The test is passed.----------------')
        print(f'---------The test is completed on {datetime.datetime.now()}.-------------')
        sleep(0.5)
        driver.close()
        driver.quit()


def login():
    print('------------ login -----------------')
    driver.find_element(By.XPATH, '//b[normalize-space()="LOGIN"]').click()
    sleep(0.25)
    driver.find_element(By.ID, 'user_email').send_keys(locators.admin_email)
    sleep(0.25)
    driver.find_element(By.ID, 'user_password').send_keys(locators.admin_password)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[@value="SIGN IN"]').click()
    sleep(0.5)
    driver.find_element(By.ID, 'authentication-popup').is_displayed()
    sleep(3)
    print('------------ logged in successfully!-----------------')


def logout():
    driver.find_element(By.XPATH, "//img[@alt='Partner']").click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//a[contains(., "Log out")]').click()
    sleep(0.25)
    driver.find_element(By.ID, 'authentication').is_displayed()
    sleep(0.25)
    print('-----------------Signed out successfully.-----------------')


def create_new_student():
    if driver.current_url == locators.login_page_url:
        print(f'----------Current URL: {locators.login_page_url}--------')
    driver.find_element(By.XPATH, '//span[normalize-space()="My WeGoStudy"]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Students"]').click()
    sleep(0.25)
    if driver.current_url == locators.student_page_url:
        print(f'-------------Create New Student----------------------')
    driver.find_element(By.XPATH, '//a[normalize-space()="Create New Student"]').click()
    sleep(0.25)

    # date of birth
    driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').send_keys('1')
    sleep(1.5)
    driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').send_keys(10 * Keys.BACKSPACE)
    sleep(1.5)
    driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').send_keys(locators.birthday)
    sleep(0.5)

    # select citizenship
    driver.find_element(By.ID, 'select2-user_student_detail_attributes_country_of_citizenship-container').click()
    sleep(1.25)
    driver.find_element(By.CLASS_NAME, 'select2-search__field').send_keys(locators.country)
    sleep(1.25)
    driver.find_element(By.CLASS_NAME, 'select2-search__field').send_keys(Keys.RETURN)
    sleep(1.25)

    # select country
    driver.find_element(By.XPATH, '//span[text()="Country"]').click()
    sleep(0.25)
    driver.find_element(By.CLASS_NAME, 'chosen-search-input').send_keys('Australia')
    sleep(0.25)
    driver.find_element(By.CLASS_NAME, 'chosen-search-input').send_keys(Keys.RETURN)
    sleep(0.25)
    # x = random.randint(1,20)
    # driver.find_element(By.XPATH, f'//li[@data-option-array-index="{x}"]').click()
    # sleep(0.5)

    # select province
    driver.find_element(By.XPATH, '//span[text()="Province/State"]').click()
    sleep(0.5)
    driver.find_element(By.XPATH, '//li[@data-option-array-index = "1"]').click()
    sleep(0.5)
    # y = random.randint(1,2)
    # driver.find_element(By.XPATH, f'(//li[@data-option-array-index = "{y}"])[2]').click()
    # sleep(0.5)
    # driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_address_attributes_state_chosen"]/div/div/input').send_keys(Keys.RETURN)
    # sleep(0.25)

    # select city
    driver.find_element(By.XPATH, '//span[text()="City"]').click()
    sleep(0.5)

    driver.find_element(By.XPATH,
                        '//*[@id="user_student_detail_attributes_address_attributes_city_chosen"]/div/ul/li[2]').click()
    sleep(0.5)
    # driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_address_attributes_city_chosen"]/div/div/input').send_keys(Keys.RETURN)
    # sleep(0.25)

    # select Credentials
    driver.find_element(By.XPATH, '//span[contains(., "Credentials")]').click()
    sleep(0.25)
    driver.find_element(By.XPATH,
                        '//*[@id="user_student_detail_attributes_user_educations_attributes_0_credentials_chosen"]/div/div/input').send_keys(
        'Degree')
    sleep(0.25)
    driver.find_element(By.XPATH,
                        '//*[@id="user_student_detail_attributes_user_educations_attributes_0_credentials_chosen"]/div/div/input').send_keys(
        Keys.RETURN)
    sleep(0.25)

    # select GPA Scale
    driver.find_element(By.XPATH, '//span[contains(., "GPA Scale")]').click()
    sleep(0.25)
    driver.find_element(By.XPATH,
                        '//*[@id="user_student_detail_attributes_user_educations_attributes_0_gpa_scale_chosen"]/div/div/input').send_keys(
        '100')
    sleep(0.25)
    driver.find_element(By.XPATH,
                        '//*[@id="user_student_detail_attributes_user_educations_attributes_0_gpa_scale_chosen"]/div/div/input').send_keys(
        Keys.RETURN)
    sleep(0.25)

    for i in range(len(locators.lst_column)):
        clm, fid, val = locators.lst_column[i], locators.lst_id[i], locators.lst_value[i]
        driver.find_element(By.ID, fid).send_keys(str(val))
        sleep(0.25)

    driver.find_element(By.XPATH, '//input[@value="Save"]').click()
    sleep(0.5)
    driver.find_element(By.CLASS_NAME, 'toast-message').is_displayed()
    sleep(5)
    print('-------------Student is created successfully.-----------')


def view_student_details():
    print(f'***************** View Details ******************')
    driver.find_element(By.XPATH, '//span[normalize-space()="My WeGoStudy"]').click()
    # driver.find_element(By.CSS_SELECTOR, 'a[aria-expanded="false"] span[class="my-auto mr-2"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Students"]').click()
    sleep(4)
    driver.find_element(By.XPATH, '//a[@href="/partners/student_details/christopher-knapp"]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//body//form').click()
    sleep(6)


def edit_student_details():
    print(f'***************** Edit Student Details ******************')
    driver.find_element(By.XPATH, '//span[normalize-space()="My WeGoStudy"]').click()
    # driver.find_element(By.CSS_SELECTOR, 'a[aria-expanded="false"] span[class="my-auto mr-2"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Students"]').click()
    sleep(4)
    driver.find_element(By.XPATH, '//a[@href="/partners/student_details/christopher-knapp"]').click()
    sleep(2)
    # driver.find_element(By.XPATH, '//body//form').click()
    # sleep(6)
    # select country
    driver.find_element(By.XPATH,
                        '//*[@id="user_student_detail_attributes_address_attributes_country_chosen"]/div/div/input').send_keys(
        'Mexico')
    sleep(0.25)
    driver.find_element(By.XPATH,
                        '//*[@id="user_student_detail_attributes_address_attributes_country_chosen"]/div/div/input').send_keys(
        Keys.RETURN)
    sleep(0.25)

    driver.find_element(By.XPATH,
                        '//*[@id="user_student_detail_attributes_user_educations_attributes_0_credentials_chosen"]/div/div/input').send_keys(
        'Master')
    sleep(0.25)
    driver.find_element(By.XPATH,
                        '//*[@id="user_student_detail_attributes_user_educations_attributes_0_credentials_chosen"]/div/div/input').send_keys(
        Keys.RETURN)
    sleep(5)

    driver.find_element(By.XPATH, '//body//form').click()
    sleep(6)
    print(f'***************** Student Detail was successfully updated ******************')


def view_application_list():
    print(f'***************** View Application list for one student  ******************')
    driver.find_element(By.XPATH, '//span[normalize-space()="My WeGoStudy"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Students"]').click()
    sleep(4)
    driver.find_element(By.XPATH, '//div[@id="student_list"]//div[1]//div[3]//a[3]').click()
    sleep(2)
    # driver.find_element(By.CSS_SELECTOR, '.btn.btn-default.btn-sm').click()
    driver.find_element(By.XPATH, '//button[@class="btn btn-default btn-sm"]').click()
    sleep(2)




def create_referral():  # cannot delete referrals, don't make more. Doesnt work, (pop up window)
    print(f'***************** create_referral ******************')

    driver.find_element(By.XPATH, '//span[normalize-space()="My WeGoStudy"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Referrals"]').click()
    sleep(1.5)
    driver.find_element(By.LINK_TEXT, 'Create Referral').click()
    sleep(5)
    driver.find_element(By.ID, 'referral_first_name').send_keys('Ran')
    sleep(2)
    driver.find_element(By.ID, 'referral_last_name').send_keys('Dom')
    driver.find_element(By.ID, 'referral_email_id').send_keys('ran.dom@hotmail.com')
    sleep(2)
    driver.find_element(By.ID, 'school_id').click()
    sleep(2)
    driver.find_element(By.XPATH, '//option[@value="20"]').click()
    sleep(1.5)
    driver.find_element(By.ID, 'program_id').click()
    sleep(2)
    driver.find_element(By.XPATH, '//option[@value="1922"]').click()
    sleep(1.5)
    driver.find_element(By.ID, 'submit_referral').click()
    sleep(6)


def commissions():
    print(f' ************ Commissions ************************************')
    driver.find_element(By.XPATH, '//span[normalize-space()="My WeGoStudy"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Commission"]').click()
    sleep(2)



def sort_by_dropdown_menu():
    print(f'***************** Sort By Dropdown Menu  ******************')
    driver.find_element(By.XPATH, '//span[normalize-space()="My WeGoStudy"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Students"]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//div[@role="button"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Last Name"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//div[@role="button"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Profile Created"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//div[@role="button"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="First Name"]').click()
    sleep(1.25)


def create_new_application():
    print(f'***************** create_new_application ******************')

    # driver.find_element(By.XPATH, '//span[normalize-space()="My WeGoStudy"]').click()
    # # driver.find_element(By.CSS_SELECTOR, 'a[aria-expanded="false"] span[class="my-auto mr-2"]').click()
    # sleep(1.25)
    # driver.find_element(By.XPATH, '//a[normalize-space()="Students"]').click()
    # sleep(1.5)
    driver.find_element(By.XPATH, f"//h4[normalize-space()='{locators.first_name} {locators.last_name}']").is_displayed()
    sleep(2)
    driver.find_element(By.LINK_TEXT, 'Create Application').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//span[normalize-space()="Select School"]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//*[@id="admission_institute_detail_id_chosen"]/div/ul/li[7]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//span[normalize-space()="Select Course"]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//*[@id="admission_institute_program_id_chosen"]/div/ul/li[2]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//span[normalize-space()="Select Starting Semester"]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//*[@id="admission_starting_semester_chosen"]/div/ul/li[3]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//span[normalize-space()="Select Start Day"]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//*[@id="admission_start_day_chosen"]/div/ul/li[3]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//span[normalize-space()="Select Year"]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//*[@id="admission_start_year_chosen"]/div/ul/li[3]').click()
    sleep(0.75)
    driver.find_element(By.CSS_SELECTOR, '#admission_last_name').send_keys(locators.last_name)
    sleep(0.75)
    driver.find_element(By.XPATH, '//input[@id="admission_electronic_communication_true"]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//input[@name="commit"]').click()
    sleep(2)
    driver.find_element(By.CLASS_NAME, 'toast-message').is_displayed()
    sleep(4)
    print('-------------application is created successfully.-----------')



def filter_by_study_area():
    print(f' *********** Filter By Study Area *******************')
    driver.find_element(By.XPATH, '//a[normalize-space()="Schools"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Filter By Study Area"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//span[contains(., "Engineering and electronics")]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//span[contains(., "Law programs")]').click()
    sleep(3)
    driver.find_element(By.XPATH, '//div[@id="filter_by_study_area"]//a[@class="apply_filter disable_apply"][normalize-space()="Apply"]').click()
    sleep(6)


def filter_by_city():
    print(f' *********** Filter By City *******************')
    driver.find_element(By.XPATH, '//a[normalize-space()="Schools"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Filter By City"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//span[contains(., "Windsor")]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//span[contains(., "Vancouver")]').click()
    sleep(3)
    driver.find_element(By.XPATH, '//div[@id="filter_by_city"]//a[@class="apply_filter disable_apply"][normalize-space()="Apply"]').click()
    sleep(6)


def filter_by_program():
    print(f' *********** Filter By Program *******************')
    driver.find_element(By.XPATH, '//a[normalize-space()="Schools"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Filter By Program"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//span[contains(., "Bachelor of Engineering")]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//span[contains(., "Master of Fine Arts (MFA)")]').click()
    sleep(3)
    driver.find_element(By.XPATH, '//div[@id="filter_by_program"]//a[@class="apply_filter disable_apply"][normalize-space()="Apply"]').click()
    sleep(6)


def schools():
    driver.find_element(By.XPATH, '//a[normalize-space()="Schools"]').click()
    sleep(0.5)
    original_window = driver.current_window_handle
    driver.find_element(By.XPATH, '//a[contains(., "Visit College Website")]').click()
    print('-----------Visit College Website Successfully.------------')
    sleep(5)
    driver.switch_to.window(original_window)
    sleep(1)
    driver.find_element(By.XPATH, '//a[contains(., "Tution")]').click()
    print('----------------------Tuition website opened.-------------')
    sleep(5)
    driver.switch_to.window(original_window)
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="featured_institutes"]/div[2]/div[3]/a/div').click()
    print('-----------We can launch the college website successfully---------')
    sleep(5)


def schools_sort_by():
    print(f'***************** Sort By ******************')
    driver.find_element(By.XPATH, '//a[normalize-space()="Schools"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//div[@role="button"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Alphabetic A to Z"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//div[@role="button"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Alphabetic Z to A"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//div[@role="button"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Location A to Z"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//div[@role="button"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Location Z to A"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//div[@role="button"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Program"]').click()
    sleep(1.25)

def add_my_favorite():
    print(f' *********** Add My Favorite *******************')
    driver.find_element(By.XPATH, '//a[normalize-space()="Schools"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//div[@class="col-12 col-lg-12 col-md-12"]//div[1]//div[3]//a[1]//div[1]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[@class="favorites-btn"]').click()
    sleep(6)
    driver.find_element(By.XPATH, '//a[normalize-space()="Schools"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//div[@id="featured_institutes"]//div[1]//div[3]//a[1]//div[1]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//i[@class="fa fa-heart"]').click()
    sleep(1.25)



def connect_to_wegostudy():
    print(f' *********** Connect To We GoStudy *******************')
    driver.find_element(By.XPATH, '//a[normalize-space()="Schools"]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//div[@class="col-12 col-lg-12 col-md-12"]//div[1]//div[3]//a[1]//div[1]').click()
    sleep(4)
    original_window = driver.current_window_handle
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Connect to WeGoStudy"]').click()
    sleep(4)
    driver.switch_to.window(original_window)



def visit_college_website():
    print(f' *********** Visit College Website *******************')
    driver.find_element(By.XPATH, '//a[normalize-space()="Schools"]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//div[@class="col-12 col-lg-12 col-md-12"]//div[1]//div[3]//a[1]//div[1]').click()
    sleep(8)
    original_window = driver.current_window_handle
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Visit College Website"]').click()
    sleep(8)
    driver.switch_to.window(original_window)



def tuition():
    print(f' *********** Tuition *******************')
    driver.find_element(By.XPATH, '//a[normalize-space()="Schools"]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//div[@class="col-12 col-lg-12 col-md-12"]//div[1]//div[3]//a[1]//div[1]').click()
    sleep(6)
    original_window = driver.current_window_handle
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[@class="btn btn-green btn-sm pull-right"]').click()
    sleep(4)
    driver.switch_to.window(original_window)



def apply_now():
    print(f' *********** Apply Now *******************')
    driver.find_element(By.XPATH, '//a[normalize-space()="Schools"]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//div[@class="col-12 col-lg-12 col-md-12"]//div[1]//div[3]//a[1]//div[1]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//a[@class="btn btn-blue btn-sm"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//button[normalize-space()="Close"]').click()
    sleep(1.25)



def study_area_prog_lev():
    print(f' *********** Study Area *******************')
    driver.find_element(By.XPATH, '//a[contains(.,  "Schools")]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//h3[normalize-space()="British Columbia Institute of Technology"]').is_displayed()
    sleep(0.25)
    driver.find_element(By.XPATH, '//div[3]//div[3]//a[1]//div[1]').click()
    sleep(0.25)
    Select(driver.find_element(By.ID, 'study_area')).select_by_value('Computer, information and services')
    sleep(0.25)
    Select(driver.find_element(By.ID, 'level')).select_by_value('Bachelor of Technology')
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[@value="GO"]').click()
    sleep(0.25)



# def application_page():
#   if driver.current_url == locators.application_page_url:
#         print(f'*****************Navigate to Application Page  ******************')
#
#     # test the "search the student" function
#     driver.find_element(By.XPATH, '//span[normalize-space()="My WeGoStudy"]').click()
#     sleep(0.25)
#     driver.find_element(By.XPATH, '//a[normalize-space()="Applications"]').click()
#     sleep(0.5)
#     driver.find_element(By.XPATH, "//input[@id='student']").send_keys(locators.first_name)
#     sleep(0.5)
#     driver.find_element(By.ID, 'filter_application').click()
#     sleep(1.5)
#     driver.find_element(By.XPATH, "//a[normalize-space()='All Applications']").click()
#     sleep(0.5)

    # test all the buttons: First, Previous, 1, 2, Next, Last
    # if we only have 1 page applictions, the following "2" will not work because we don't have 2 pages applications.
    # driver.find_element(By.XPATH, "//a[normalize-space()='2']").click()
    # sleep(0.5)
    # driver.find_element(By.ID, 'admission_list_first').click()
    # sleep(0.5)
    # driver.find_element(By.ID, 'admission_list_last').click()
    # sleep(0.5)
    # driver.find_element(By.ID, 'admission_list_previous').click()
    # sleep(0.5)
    # driver.find_element(By.ID, 'admission_list_next').click()
    # sleep(0.5)
    # driver.find_element(By.XPATH, "//a[normalize-space()='1']").click()
    # sleep(0.5)
    # delete single application
    # driver.find_element(By.XPATH, "//label[@for='application_ids_117']").click()
    # sleep(0.25)

    # delete all applications
    # driver.find_element(By.ID, 'select_all').click()
    # sleep(0.5)
    # driver.find_element(By.ID, 'delete_applications').click()
    # sleep(0.5)
    # print('---------Application(s) deleted successfully.--------')







# setUp()
# login()
# create_new_student()
# edit_student_details()
# view_application_list()
# create_referral()
# commissions()
# sort_by_dropdown_menu()
# create_new_application()
# filter_by_study_area()
# filter_by_city()
# filter_by_program()
# schools()
# schools_sort_by()
# add_my_favorite()
# connect_to_wegostudy()
# visit_college_website()
# tuition()
# apply_now()
# study_area_prog_lev()
# application_page()
# logout()
# tearDown()
