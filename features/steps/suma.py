from behave import given, when, then
import random

S1, S2 = random.randint(0,1000), random.randint(0,1000)

@given('El usuario está en el formulario para sumar')
def step_impl(context):
	br = context.browser
	br.get(context.base_url + '/suma/')
	assert br.current_url.endswith('/suma/')


@when('Ingresa dos sumandos y clickea el boton enviar')
def step_impl(context):
	br = context.browser
	br.get(context.base_url + '/suma/')

	# Checks for Cross-Site Request Forgery protection input
	assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

	print(S1, S2)
	# Fill login form and submit it (valid version)
	br.find_element_by_name('s1').send_keys(str(S1))
	br.find_element_by_name('s2').send_keys(str(S2))
	br.find_element_by_name('submit').click()

@then('Le muestro la suma de los dos sumandos')
def step_impl(context):
	br = context.browser

	# Checks success status
	assert br.current_url.endswith('/suma/')
	assert br.find_element_by_id('result').text == str(S1 + S2)
