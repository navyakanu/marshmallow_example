*******************************************************************************************************************************

*) Automate apis in https://reqres.in/ 
*) Uses Marshest to create api models and asserts 

API'S AUTOMTED ::

1) create : curl -X POST -H "Content-Type: application/json" -d '{"name":"abcd","job":"QA"}'  https://reqres.in/api/users
2) single user :  curl -X GET -H "Content-Type: application/json" https://reqres.in/api/users/1 



Dependencies: Runs only with python3 and above

*) pip install requirements.txt
*) Run in command line
	python -m all
