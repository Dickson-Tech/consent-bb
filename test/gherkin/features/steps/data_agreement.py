from behave import given, when, then
import requests
import json

# This step is assumed to be defined in smoke.py and shared across the test suite
# @given("A URL of a Consent Building Block instance")
# def step_impl(context):
#     context.api_url = context.session.api_url

@given("a data agreement ID \"{dataAgreementId}\"")
def step_impl(context, dataAgreementId):
    context.dataAgreementId = dataAgreementId

@when("I make a GET request to /config/data/agreement/{dataAgreementId}")
def step_impl(context):
    # Construct the full API endpoint URL
    url = f"{context.api_url}/config/data/agreement/{context.dataAgreementId}"
    # Make the GET request
    context.response = requests.get(url, verify=False)  # Adjust SSL verification as per your project's requirements

@then("The response should have a status code of 200")
def step_impl(context):
    # Assert that the response status code is 200
    assert context.response.status_code == 200, f"Expected 200, got {context.response.status_code}"

@then("The response should contain the data agreement details for \"{dataAgreementId}\"")
def step_impl(context, dataAgreementId):
    # Parse the response content and assert the data agreement details
    response_data = json.loads(context.response.content)
    assert response_data['id'] == dataAgreementId, "Data agreement ID does not match"

@then("The response should have a status code of 400")
def step_impl(context):
    assert context.response.status_code == 400, f"Expected 400, got {context.response.status_code}"
