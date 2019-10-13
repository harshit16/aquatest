from behave import given, when, then
import requests

global_general_variables = {}
http_request_header = {}
http_request_body = {}
http_request_url_query_param = {}


# setting api url in a dictionary.
@given(u'Set application url is "{basic_app_url}"')
def set_app_url(context, basic_app_url):
    global_general_variables['basic_application_URL'] = basic_app_url


@given(u'Set task details as "{paramKey}" and "{paramValue}" below')
def step_set_task_details(context, paramKey, paramValue):
    for row in context.table:
        temp_value = row['paramValue']
        global_general_variables[row['paramKey']] = temp_value
        if 'empty' in temp_value:
            global_general_variables[row['paramKey']] = ''


# setting api endpoints in a dictionary.
@when(u'Set HEADER param request content type as "{header_content_type}"')
def step_header_content(context, header_content_type):
    http_request_header['content-type'] = header_content_type


# setting api response in a dictionary.
@when(u'Set HEADER param response accept type as "{header_accept_type}"')
def step_header_accept(context, header_accept_type):
    http_request_header['Accept'] = header_accept_type


# setting api endpoints in a dictionary.
@given(u'Set GET api endpoint as "{get_api_endpoint}"')
def step_getReuest_endpoint(context, get_api_endpoint):
    global_general_variables['GET_api_endpoint'] = get_api_endpoint


@given(u'Set POST api endpoint as "{post_api_endpoint}"')
def step_postReuest_endpoint(context, post_api_endpoint):
    global_general_variables['POST_api_endpoint'] = post_api_endpoint


@given(u'Set PUT api endpoint as "{put_api_endpoint}"')
def step_putReuest_endpoint(context, put_api_endpoint):
    global_general_variables['PUT_api_endpoint'] = put_api_endpoint


@when(u'Set DELETE api endpoint as "{delete_api_endpoint}"')
def step_deleteReuest_endpoint(context, delete_api_endpoint):
    global_general_variables['DELETE_api_endpoint'] = delete_api_endpoint


@when(u'Raise "{http_request_type}" HTTP request')
def step_raiseRequest(context, http_request_type):
    base_url = global_general_variables['basic_application_URL']
    temp_url = []

    if 'GET' == http_request_type:
        print 'inside GET'  # need to be removed
        temp_url.append(base_url)
        temp_url.append('/')
        temp_url.append(global_general_variables['GET_api_endpoint'])
        service_url = ''
        service_url = service_url.join(temp_url)
        http_request_body.clear()
        global_general_variables["response_full"] = requests.get(service_url, data=http_request_body,
                                                                 headers=http_request_header)
    if 'POST' == http_request_type:
        print 'inside POST'
        temp_url.append(base_url)
        temp_url.append("?id=")
        temp_url.append(global_general_variables['POST_api_endpoint'])
        service_url = ''
        print 'service_url'
        service_url = service_url.join(temp_url)
        print service_url
        http_request_url_query_param.clear()
        global_general_variables['response_full'] = requests.post(service_url,
                                                                  headers=http_request_header,
                                                                  params=http_request_url_query_param,
                                                                  data=http_request_body)
    if 'PUT' == http_request_type:
        print 'inside put'
        http_request_body.clear()
        temp_url.append(base_url)
        temp_url.append('/')
        temp_url.append(global_general_variables['PUT_api_endpoint'])
        service_url = ''
        print  "FFFFFFFFFFFFFF0", temp_url

        print 'service_url'
        service_url = service_url.join(temp_url)
        print service_url
        http_request_url_query_param.clear()
        global_general_variables['response_full'] = requests.put(service_url,
                                                                 headers=http_request_header,
                                                                 params=http_request_url_query_param,
                                                                 data=http_request_body)
        print 'PPEEEEEEEEEEEEEEEEEEEEEEEEEE', global_general_variables

    else:
        "harshit"

@then(u'Valid HTTP response should be received')
def step_getHttpResponse(context):
    if None in global_general_variables['response_full']:
        assert False, 'Null response received'


@then(u'Response http code should be {expected_response_code:d}')
def step_validateHttpResponse(context, expected_response_code):
    global_general_variables['expected_response_code'] = expected_response_code
    actual_response_code = global_general_variables['response_full'].status_code
    if str(actual_response_code) not in str(expected_response_code):
        print (str(global_general_variables['response_full'].json()))
        assert False, '***ERROR: Following unexpected error response code received: ' + str(actual_response_code)


@then(u'Response HEADER content type should be "{expected_response_content_type}"')
def step_headerContentType(context, expected_response_content_type):
    global_general_variables['expected_response_content_type'] = expected_response_content_type
    actual_response_content_type = global_general_variables['response_full'].headers['Content-Type']
    if expected_response_content_type not in actual_response_content_type:
        assert False, '***ERROR: Following unexpected error response content type received: ' + actual_response_content_type


@when(u'Set BODY form param using Set task details')
def step_body_form_param(context):
    http_request_body['tasks'] = global_general_variables['task_name']
    http_request_body['completed'] = global_general_variables['complete_status']


@then(u'Response BODY should not be null or empty')
def step_validate_response_body(context):
    if None in global_general_variables['response_full']:
        assert False, '***ERROR:  Null or none response body received'


@when('Modify BODY form param using Set task details')
def step_update_body_param(context):
    http_request_body['tasks'] = global_general_variables['new_task_name']
    # raise NotImplementedError(
    #     u'STEP: And Modify BODY form param task_name as "aquaApi300" and complete_status as "true"')