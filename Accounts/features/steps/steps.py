from behave import *
from account import *

@given('a non admin account')
def step_impl(context):
    context.Nonaccount = Account('accountName', False)

@then('account has name and false app status')
def step_impl(context):
    assert context.Nonaccount.name and not context.Nonaccount.appStatus

@then('account is not admin')
def step_impl(context):
    assert context.Nonaccount.improveCheck() == 'invalid admin'



@given('an admin account')
def step_impl(context):
    context.adminAccount = Account('accountName', True)

@when('app is enabled')
def step_impl(context):
    context.adminAccount.enableApp()

@then('app status is active')
def step_impl(context):
    assert (context.adminAccount.appStatus == True)

@then('account is admin')
def step_impl(context):
    assert context.adminAccount.improveCheck() == 'valid admin'







