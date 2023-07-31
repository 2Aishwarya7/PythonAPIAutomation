import json
import requests

def get_request(url,payload,headers,in_json):
    response=requests.get(url=url,headers=headers,data=json.dumps(payload))
    if in_json is True:
        return response.json()
    return response

def post_request(url,auth,headers,payload,in_json):
    post_response=requests.post(url=url,headers=headers,auth=auth,data=json.dumps(payload))
    if in_json is True:
        return post_response.json()
    return post_response

def patch_request(url,auth,headers,payload,in_json):
    patch_response_data = requests.patch(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return patch_response_data.json()
    return patch_response_data

def delete_data(url, headers, auth, in_json):
    delete_response_data = requests.delete(url=url, headers=headers, auth=auth)
    if in_json is True:
        return delete_response_data.json()
    return delete_response_data

def put_request(url, auth, headers, payload, in_json):
    update_response_data=requests.put(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:
        return update_response_data.json()
    return update_response_data




