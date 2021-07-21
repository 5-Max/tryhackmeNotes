to mitigate or remediate is the question lol

this site looks promising 
https://www.upguard.com/blog/top-20-owasp-vulnerabilities-and-how-to-fix-them

# 1 Injection

## 1- Sql Injection 
	- Most instances of SQL injection can be prevented by using *parameterized queries* (also known as prepared statements) instead of string concatenation within the query.
	
	`String query = "SELECT * FROM products WHERE category = '"+ input + "'";`
	`Statement statement = connection.createStatement();`
	`ResultSet resultSet = statement.executeQuery(query);`
	
becomes

	`PreparedStatement statement = connection.prepareStatement("SELECT * FROM products WHERE category = ?");`
	`statement.setString(1, input);`
	`ResultSet resultSet = statement.executeQuery();`
	
- For a parameterized query to be effective in preventing SQL injection, the string that is used in the query must always be a hard-coded constant, and must never contain any variable data from any origin. Do not be tempted to decide case-by-case whether an item of data is trusted, and continue using string concatenation within the query for cases that are considered safe. It is all too easy to make mistakes about the possible origin of data, or for changes in other code to violate assumptions about what data is tainted.

**so 0 concatenation**

research py
`eval("import os, os.system('rm -rf /')")`

## 2- Command Injection
		- passthu() function is calling command
			https://www.php.net/manual/en/function.passthru.php
		- similar to exec() and system()
		- When allowing user-supplied data to be passed to this function, use [escapeshellarg()](https://www.php.net/manual/en/function.escapeshellarg.php) or [escapeshellcmd()](https://www.php.net/manual/en/function.escapeshellcmd.php) to ensure that users cannot trick the system into executing arbitrary commands.
  - By far the most effective way to prevent OS command injection vulnerabilities is to **never call out to OS commands from application-layer code**. In virtually every case, there are alternate ways of implementing the required functionality using safer platform APIs.

	- If it is considered unavoidable to call out to OS commands with user-supplied input, then strong input validation must be performed. Some examples of effective validation include:

		-   Validating against a whitelist of permitted values.
		-   Validating that the input is a number.
		-   Validating that the input contains only alphanumeric characters, no other syntax or whitespace.

3- Email injection
	- 
	
# 2 Broken Authentication
Weak passwords 
	- strong password policy
	- IDS monitoring number of logins
	- MFA

Cookie manipulation 
  	- use JSON webtoken with good signature

Reset Password 
	- 2FA would fix this


## 3 Sensitive Data Exposure


database dump
	- database location 


## 4 XXE

- Virtually all XXE vulnerabilities arise because the application's XML parsing library supports potentially dangerous XML features that the application does not need or intend to use. The easiest and most effective way to prevent XXE attacks is to disable those features.

- Generally, it is sufficient to disable resolution of external entities and disable support for `XInclude`. This can usually be done via configuration options or by programmatically overriding default behavior. Consult the documentation for your XML parsing library or API for details about how to disable unnecessary capabilities.

## 5 Broken Access Control

