# ------------------- CHECK MAIL & SEND CODE & ADMIN ACOUNT -------------------

json_for_check_email_for_login =  \
    json_for_check_admin_acount = json_for_send_confirm_code = \
    {"email": "abc@yandex.ru"}

expected_params_check_login = \
    expected_params_check_admin_acount = ["registrationRequired"]

list_of_expected_params_from_comfirm_code = ["status"]

# ----------------------------------- LOGIN -----------------------------------

json_for_login = {
    "email": "abc@yandex.ru",
    "code": "12345"
}

expected_params_login = ["access", "refresh"]

# ------------------------------- REFRESH TOKEN -------------------------------

expected_params_resresh = ["access", "refresh", "expire"]

