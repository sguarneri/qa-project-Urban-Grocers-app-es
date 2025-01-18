import sender_stand_request
import data

def get_kit_body(name):
    current_name = data.kit_body.copy()
    current_name["name"] = name
    return current_name

def get_new_user_token():
    user_body = data.user_body
    user_response = sender_stand_request.post_new_user(user_body)
    return user_response.json()["authToken"]

def positive_assert(name):
    kit_body = get_kit_body(name)
    auth_token = get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert kit_response.status_code == 201

def negative_assert_code_400(name):
    kit_body = get_kit_body(name)
    auth_token = get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400
    assert kit_response.json()["message"] == "El nombre debe contener sólo letras latino, "\
                                             "un espacio y un guión. De 2 a 15 caracteres"

def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")

def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def test_create_kit_empty_name_get_error_response():
    negative_assert_code_400("")

def test_create_kit_512_letter_name_get_error_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def test_create_kit_has_special_symbols_in_name_get_success_response():
    positive_assert("№%@,")

def test_create_kit_has_space_in_name_get_success_response():
    positive_assert(" A Aaa ")

def test_create_kit_has_numbers_in_name_get_success_response():
    positive_assert("123")

def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_code_400(kit_body)

def test_create_kit_has_number_type_in_name_get_error_error():
    negative_assert_code_400(123)
