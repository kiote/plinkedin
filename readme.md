Project name
----
Linkedin Tornado API

Mission
----

1. Get practical skills with:
a. Tornado async web framework;
b. Python 2.7;
c. Linkedin API;
d. testing async python app.
2. Demostrate the way of coding and testing on github

Specifications
----

**Short**

1. Http running at any python-installed machine with no external lib installing;
2. json responce to json request: “find top 10 IT companies in Russia”;
3. json responce to json request: “find quantity of vacancies for top 10”;
3. Cashing responce from API for 5 minutes.

**Installation**
Serever able to run with no installation. API keys putted to yaml-file.

Architecture
----

1. Tornado as async. http-server;
2. MongoDB as data storage;
3. http/json as interface;
4. Oauth for authorization;
5. Unit Tests and mock for testing
