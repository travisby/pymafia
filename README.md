pymafia is a django app to automate a game of "mafia"


STYLE GUIDE:

imports

	<general python module1>
	<general python module2>

	<django module1>
	<django module2>

	<local module1>
	<local module2>

	alphabetize within each section

	imports to the shortest names possible -1, using "as" only where appropriate
	from a.b.c import d.e

	OR

	import a.b.c.d.e as De

	Long imports: use parenthesis, each on their own line
		from blank import (
				blank, blank, blank
				blank
				)
classes

	<stuff before it>


	class <SnakeCasedClassName>
	"""Docstring"""
	
	<python code>

	Model Metaclasses don't need docstrings, and should be one line after field definitions


Docstrings

	"""Oneline docstring"""

	<python code>

	OR

	"""Small Description

	Longer Description that
	fits on multiple ilnes
	"""

	<python <code>


Parameters

	parameters(a, b, c)
	parameters(something=a, somethingelse=b)

Operators

	variable = a + b
	variable = (a + b) / 6


Modules

	Where possible, alphabetize classes
	Leave comments where impossible

Comments

	Line for themselves
	On the line preceding the code they comment
	space between # and message

	# message
	<python code described by message>

	Should explain why, not how in most cases
	Any "heavy" lines can, and should, explain how (multi-nested paranthesis, chained function calls, etc.)

Tests
	100% code coverage, using nosetests --with-coverage
	Seperate setup code from the assert statement
	one assert per test
	Factories, not fixtures
	Seperate each set of factory calls
	fact1 = Fact1()
	fact2 = Fact1()

	fact3 = Fact2()


Pylint
	Use it, but not for automation.  Until I find a good way to lint in django, I'm going to use pylint and mentally ignore many of the warnings/errors.  Unfortunately, I don't know a way to ignore certain spots for certain rules (ex., we don't need docstrings for modules, but we do for classes).  So use your best judgement.
