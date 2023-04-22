import pytest

# @pytest.mark.one
# def test_method1():
#     x = 5
#     y = 10
#     assert x == y

# @pytest.mark.two
# def test_method2():
#     a = 15
#     b = 20
#     assert a + 5 == b


# @pytest.mark.parametrize("maybe_palindrome, expected_result", [
#     ("", True),
#     ("a", True),
#     ("Bob", True),
#     ("Never odd or even", True),
#     ("Do geese see God?", True),
#     ("abc", False),
#     ("abab", False),
# ])
# def test_is_palindrome(maybe_palindrome, expected_result):
#     assert is_palindrome(maybe_palindrome) == expected_result


@pytest.fixture
def example_people_data():
    return [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]

def format_data_for_display(people):
    display_list = []
    for i in people:
        # print(i['given_name'])
        display_list.append(i['given_name'] + " " +  i['family_name'] + ": " + i['title'])

    return display_list

# def test_format_data_for_display():
#     people = [
#         {
#             "given_name": "Alfonsa",
#             "family_name": "Ruiz",
#             "title": "Senior Software Engineer",
#         },
#         {
#             "given_name": "Sayid",
#             "family_name": "Khan",
#             "title": "Project Manager",
#         },
#     ]

#     assert format_data_for_display(people) == [
#         "Alfonsa Ruiz: Senior Software Engineer",
#         "Sayid Khan: Project Manager",
#     ]

def test_format_data_for_display(example_people_data):
    assert format_data_for_display(example_people_data) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]