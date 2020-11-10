#### This file contains tests to evaluate that your bot behaves as expected.
#### If you want to learn more, please see the docs: https://rasa.com/docs/rasa/user-guide/testing-your-assistant/

## happy path 1
* greet: hello there!
  - utter_greet
* firstname: angel
  - action_greet
* affirm : yes
  - utter_ask_field
* area_of_interest: JavaScript
  - utter_ask_jobtype
* jobtype: fulltime
  - utter_ask_howlong
* how_long: 14
  - utter_ask_location
* state: osun
  - utter_patience
  - action_get_jobs
  - slot{"jobs_gotten": "true"}
  - utter_goodbye
  - action_restart

## happy path 1
* greet: hello there!
  - utter_greet
* firstname: angel
  - action_greet
* affirm : yes
  - utter_ask_field
* area_of_interest: Clergy
  - utter_ask_jobtype
* jobtype: fulltime
  - utter_ask_howlong
* how_long: 14
  - utter_ask_location
* state: Borono
  - utter_patience
  - action_get_jobs
  - slot{"jobs_gotten": "false"}
  - action_restart