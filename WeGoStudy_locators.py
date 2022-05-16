import datetime
import locale
import random

from faker import Faker
faker = Faker()


app = 'WeGoStudy'
app_url = 'http://34.233.225.85/'
homepage_title = 'WeGoStudy'
admin_email = 'chris.velasco78@gmail.com'
admin_password = '123cctb'
login_page_url = 'http://34.233.225.85/partner/home'
student_page_url = 'http://34.233.225.85/partners/student_details'

first_name = faker.first_name()
last_name = faker.last_name()
birthday = str(faker.date_of_birth())
passport_num = faker.pyint(1111111, 9999999)
country = faker.country()
state = faker.state()
city = faker.city()
address = faker.street_address()
zip_code = faker.zipcode()
phone_num = faker.pyint(1111111111, 9999999999)
email = faker.email()
school = f'{country} University'
program = random.choice(['Computer', 'Physics', 'Statistic', 'Math', 'Language', 'Chemistry', 'Medicine'])
gpa = faker.pyint(1,100)

lst_column = ['First Name', 'Last Name', 'Passport Number', 'Phone Number', 'Mailing Address', 'Zip Code', 'Email', 'School Name', 'Program', 'GPA']
lst_id = ['user_student_detail_attributes_first_name', 'user_student_detail_attributes_last_name',
          'user_student_detail_attributes_passport_number', 'phone_number',
          'user_student_detail_attributes_address_attributes_mailing_address',
          'user_student_detail_attributes_address_attributes_zip_code', 'user_email',
          'user_student_detail_attributes_user_educations_attributes_0_school_name',
          'user_student_detail_attributes_user_educations_attributes_0_program',
          'user_student_detail_attributes_user_educations_attributes_0_gpa']
lst_value = [first_name, last_name, passport_num, phone_num, address, zip_code, email, school, program, gpa]
