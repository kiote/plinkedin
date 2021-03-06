Project name
----
Linkedin Tornado API

Mission
----

1. Get practical skills with:
    * Tornado async web framework;
    * Python 2.7;
    * Linkedin API;
    * testing async python app;
    * mogoDB.
2. Demostrate the way of coding and testing on github

Specifications
----

**Short**

1. Http running at any python-installed machine with no external lib installing;
2. json responce to json request: “find top 10 IT companies in Russia”;
3. json responce to json request: “find quantity of vacancies for top 10”;
4. Cashing responce from API for 5 minutes.
5. User should be able to register and save API credentials.

**Installation**
Serever able to run with no installation.

**Production**
Project should run on any public-available serever.

Architecture
----

1. Tornado as async. http-server;
2. MongoDB as data storage;
3. http/json as interface;
4. Oauth for authorization;
5. Unit Tests and mock for testing

Quality assuarance plan
----

Software development plan
----
[google doc](https://docs.google.com/spreadsheets/d/10OBG5gPGC5YATgCJHDJoNUr6Q8I1h7dYXLaqucDWxRA)

Top-10 risks list
----
1. Lost interest. 
   If I'm as a mainteiner will loose the intrest to the project.
   Result: project will stop.
2. Lack of skills. 
   Too much time to making simple tasks.
   Result: project will lasts too much time. Risk 1 turns real.
3. Too much time. 
   Wasting time and not making project move.
   Result: project will lasts too much time. Risk 1 turns real.
4. Low quality.
   Reduce: Use code standards, use testing
5. Can't or too much time to run in production.
   Reduce: try to run on production at early stages. Try to run via tunnelbrick
6. Unstable tools
   Reduce: -
   
How to avoid/reduce: remember about the mission. Set propper deadlines. Make good plan and follow it. Make acceptance tests.
