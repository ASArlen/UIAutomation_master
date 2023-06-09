from behave import *

use_step_matcher('re')


@step('Login111 (.*)')
def step_impl(context,text):
    context.test1_page.Login111(text)