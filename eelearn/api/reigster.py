import frappe
from datetime import datetime


@frappe.whitelist(allow_guest=True)
def register(email, passwrd,mobile_no,first_name,last_name,gender,birth_date,interests = None,profession=None,education_info=None):
        frappe.flags.in_import = True
    # if education_info:
    #     for education in education_info:
    #         detail = frappe.get_doc(
	# 		{
	# 			"doctype": "Education Detail",
	# 			"institution_name": education.institution_name,
	# 			"location": education.location,
    #             "degree_type": education.degree_type,
    #             "major":education.major
	# 		}
	# 	)
        user = frappe.get_doc(
			{
				"doctype": "User",
				"email": email,
				"first_name": first_name,
                "last_name": last_name,
                "mobile_no":mobile_no,
				"enabled": 1,
                "gender":gender,
                "birth_date":birth_date,
				"new_password": passwrd,
				"user_type": "Website User",
                "interests":interests,
                "profession":profession
			}
		)
        user.flags.no_email = True
        user.flags.ignore_permissions = True
        user.flags.ignore_password_policy = True
        user.insert()
        frappe.flags.in_import = False 