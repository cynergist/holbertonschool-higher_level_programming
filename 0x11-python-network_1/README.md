# 0x11. Python - Network #1

# Resources
[Python HOWTO Fetch Internet Resources Using the urllib Package](https://docs.python.org/3/howto/urllib2.html) <br />
[A PDF version of the above resource, Release 3.4.3](https://scicomp.ethz.ch/public/manual/Python/3.4.3/howto-urllib2.pdf) <br />
[Python Requests: HTTP for Humans](https://2.python-requests.org//en/master/) <br />
[GeeksforGeeks: GET and POST requests using Python](https://www.geeksforgeeks.org/get-post-requests-using-python/) <br />

# Learning Objectives
- How to fetch internet resources with the Python package `urllib`
- How to decode `urllib` body response
- How to use the Python `package` requests
- How to make HTTP `GET` request
- How to make HTTP `POST`/`PUT`/etc. request
- How to fetch JSON resources
- How to manipulate data from an external service

## Tasks

0. 0-hbtn_status.py // a Python script that fetches `https://intranet.hbtn.io/status`
- Using only the package `urllib`
- And a with statement

1. 1-hbtn_header.py // a Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.

- Using only the packages `urllib` and `sys`
- And a with statement

2. 2-post_email.py // a Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`)

- The email is sent in the `email` variable
- Using only the packages `urllib` and `sys`
- And a with statement

3. 3-error_code.py // a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`).

- Manage `urllib.error.HTTPError` exceptions and print: `Error code:` followed by the HTTP status code
- Using only the packages `urllib` and `sys`
- And a with statement

4. 4-hbtn_status.py // a Python script that fetches `https://intranet.hbtn.io/status`

- Using only the package `requests`

5. 5-hbtn_header.py // a Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header

- Using only the packages `requests` and `sys`
- The value of this variable is different for each request

6. 6-post_email.py // a Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response.

- The email is sent in the variable `email`
- Using the packages `requests` and `sys`

7. 7-error_code.py // a Python script that takes in a URL, sends a request to the URL and displays the body of the response.

- If the HTTP status code is greater than or equal to 400, print: `Error code:` followed by the value of the HTTP status code
- Using only the packages `requests` and `sys`

8. 8-json_api.py // a Python script that takes in a letter and sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.

- The letter is sent in the variable `q`
- If no argument is given, set `q=""`
- If the response body is properly JSON formatted and not empty, display the `id` and `name` like this: `[<id>] <name>`
- Otherwise:
  -- Display `Not a valid JSON` is the JSON is invalid
  -- Display `No result` is the JSON is empty
- Using only the packages `requests` and `sys`

9. 9-starwars.py // a Python script that takes in a string and sends a search request to the [Star Wars API](https://swapi.co/documentation) <br/ >

- Use the [Star Wars API search people endpoint](https://swapi.co/documentation#search) <br/ >
- String argument as the `search` value of the request
- The body response must be JSON and converted to a Python dictionary.
- Display: `Number of results: <count>`
- Display the `name` of each result (see example below)
- Using only the packages `requests` and `sys`
- No need to manage the pagination

10. 10-my_github.py // a Python script that takes your Github credentials (username and password) and uses the [Github API](https://developer.github.com/v3/users/#get-the-authenticated-user) to display your `id`

- Use [Basic Authentication](https://developer.github.com/v3/#basic-authentication) to access to your information
- First argument is `username`
- Second argument is `password`
- Using only the packages `requests` and `sys`
