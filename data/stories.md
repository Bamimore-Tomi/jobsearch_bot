## story 1
* greet
    - utter_greet
    - utter_ask_field
* area_of_interest{"field": "graphics design"}
    - slot{"field": "graphics design"}
    - utter_ask_jobtype
* job_type{"job_type": "fulltime"}
    - slot{"job_type": "fulltime"}
    - utter_ask_howlong
* how_long{"p_age": "14"}
    - slot{"p_age": "14"}
    - utter_ask_location
* state{"location": "lagos"}
    - slot{"location": "lagos"}
	- utter_assurance
    - action_get_jobs
    - slot{"jobs_gotten": "true"}
    - utter_goodbye
    - action_restart

## story 2
* greet
    - utter_greet
    - utter_ask_field
* area_of_interest{"field": "graphics design"}
    - slot{"field": "graphics design"}
    - utter_ask_jobtype
* job_type{"job_type": "fulltime"}
    - slot{"job_type": "fulltime"}
    - utter_ask_howlong
* how_long{"p_age": "14"}
    - slot{"p_age": "14"}
    - utter_ask_location
* state{"location": "lagos"}
    - slot{"location": "lagos"}
	- utter_assurance
    - action_get_jobs
    - slot{"jobs_gotten": "false"}
    - action_restart
