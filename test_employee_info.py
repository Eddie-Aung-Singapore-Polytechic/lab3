import employee_info

def test_get_employees_by_age_range():
    upper_limit = 31
    lower_limit = 18
    expected_names = ['John','Jane','Mary']
    return_list = employee_info.get_employees_by_age_range(lower_limit,upper_limit)
    for i in return_list:
        for k in expected_names:
            if i['name'] == k:
                expected_names.remove(k)
    
    assert(expected_names == [])

    '''
def test_calculate_average_salary():
    #assert()
    return 0
def test_get_employees_by_dept():
    #assert()
    return 0
    '''

#test_get_employees_by_age_range()