# DJANGO-BDD
Tutorial de como hacer  BDD con Django basado en [la documentacion oficial](https://behave.readthedocs.io/en/latest/)


## Instalacion 

* Instale las bibliotecas que se encuentran en el archivo requirements.txt
> pip install -r requirements.txt


Para ejecutar los tests, necesitaras descargar la ultima version de geckodriver para ejecutar Firefox con selenium. 
Puede descargar geckodriver para Firefox en el 
[repositorio oficial de Mozilla](https://github.com/mozilla/geckodriver/releases "") 

Luego de haber descargado geckodriver para Firefox, debera anadir el directorio que contiene el archivo ejecutable a sus variables de entorno. 
* En sistemas Unix, podra ejecutar el siguiente comando 
> export PATH=$PATH:/path/to/directory/of/executable/downloaded/in/previous/step

Puede encontrar [mas referencias para utilizar Selenium con Python aca.](https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path)

## Implentacion de features con BDD

### Crear un nuevo feature

Se desea implementar el feature myfeature.

1. Cree el archivo /features/myfeature.feature

2. En myfeature.feature describa el Feature, Scenario, Given, When y Then de la siguiente forma:

```
Feature: To do a custom task

  Scenario: User is in specific page

	Given The user is in the page /specific-page/
	When Executes a specific task
	Then The website redirects user to page /specific-result/ and show a specific content
```

3. Cree el archivo /features/steps/myfeature.py

```python
from behave import given, when, then

@given('The user is in the page /specific-page/')
def step_impl(context):
	br = context.browser
	br.get(context.base_url + '/specific-page/')
	assert br.current_url.endswith('/specific-page/')


@when('Executes a specific task')
def step_impl(context):
	br = context.browser
	br.get(context.base_url + '/specific-page/')

	# Check assertions for /specific-page/ before doing a task
	assert ...
	
	# Execute a specific task using the selenium browser
    # Example, fill values and click a submit button
	br.find_element_by_id('an-input-id').send_keys('A value')
	br.find_element_by_id('a-button-id').click()

@then('The website redirects user to page /specific-result/ and show a specific content')
def step_impl(context):
	br = context.browser

	# Checks success status
	assert br.current_url.endswith('/specific-result/')
	assert br.find_element_by_id('result').text == "Some value"

```
[Mas referencias para ejecutar tareas con selenium ](https://selenium-python.readthedocs.io/)

4. Pruebe el feature ejecutando 
> python manage.py behave
