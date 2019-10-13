import requests
import json
import sys

baseURI = "http://localhost:5000/tasks"
post_request_id = {}


# POST request
def test_post_request():
    endpoint = '?id=76aqua13'
    service_url = baseURI + endpoint
    contenttype = 'application/json'
    headers = {
        'Content-Type': contenttype,
        'Accept': contenttype
    }
    data = {
        "task": "aqua task",
        "completed": True
    }
    try:
        response = requests.post(service_url, json=data)
        response_data = response.json()
        print response_data

        post_request_id.clear()
        post_request_id['tid'] = str(response_data['task_id'])
        print post_request_id['tid']
        assert response.status_code == 200
    except requests.exceptions.RequestException as error:
        sys.stderr.write(error)
        sys.exit(1)


# GET request
def test_get_request():
    try:
        service_url = baseURI + '/'
        endpoint = post_request_id['tid']
        response = requests.get(baseURI, params=endpoint)
        print response.status_code
        data = response.json()
        print data
        assert response.status_code == 200
    except requests.exceptions.RequestException as error:
        sys.stderr.write(error)
        sys.exit(1)


# marking completed using POST request
def test_mark_completed():
    try:
        task_id = post_request_id['tid']
        service_url = baseURI + '/' + task_id + '/completed'
        print '\n --------------------service URL------------------------\n'
        print service_url
        response = requests.post(service_url, json=None)
        response_data = response.json()
        assert response.status_code == 200
    except requests.exceptions.RequestException as error:
        sys.stderr.write(error)
        sys.exit(1)


# negative test case, assertion with response code 500
# change the Expected status to 200 (correct response) to assert with Actual Response

def test_put_request():
    try:
        endpoint = '?id=76aqua13'
        service_url = baseURI + endpoint
        contenttype = 'application/json'
        headers = {
            'Content-Type': contenttype,
            'Accept': contenttype
        }
        payload = {
            "task": "aqua task",
            "completed": True
        }
        task_id = post_request_id['tid']
        service_url = baseURI + '/' + task_id
        print 'service_url------------------------', service_url
        response = requests.put(service_url, data=json.dumps(payload), headers=headers)
        response_data = response.json()
        assert response.status_code == 500
    except requests.exceptions.RequestException as error:
        sys.stderr.write(error)
        sys.exit(1)


def test_delete_request():
    try:
        task_id = post_request_id['tid']
        service_url = baseURI + '/' + task_id
        response = requests.delete(service_url)
        response_data = response.json()
        assert response.status_code == 200
    except requests.exceptions.RequestException as error:
        sys.stderr.write(error)
        sys.exit(1)
