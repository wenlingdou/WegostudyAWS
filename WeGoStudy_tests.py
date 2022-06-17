import unittest
import WeGoStudy_locators as locators
import WeGoStudy_methods as methods


class PositiveTestCases(unittest.TestCase):
    @staticmethod
    def test_main_wegostudy():
        methods.setUp()
        methods.login()
        # methods.create_new_student() #  no more new students
        # methods.edit_student_details()
        # methods.sort_by_dropdown_menu()
        # methods.create_new_application()  # don't need new applications
        # methods.view_application_list()
        # # methods.create_referral()  # cannot delete referrals, don't make more. Doesnt work, (pop up window)
        methods.commissions()
        methods.filter_by_study_area()
        methods.filter_by_city()
        methods.filter_by_program()
        methods.schools()
        methods.schools_sort_by()
        methods.add_my_favorite()
        methods.connect_to_wegostudy()
        methods.visit_college_website()
        methods.tuition()
        methods.apply_now()
        methods.study_area_prog_lev()
        # methods.application_page()
        methods.logout()
        methods.tearDown()
