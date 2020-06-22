## case happy path :
* greet
  - utter_greet
* request_status_led{"led": "quarto"}
  - action_response_led
* request_resolve_led_on{"led": "quarto"}
  - action_resolve_led_on
* request_status_pwm{"pwm": "sala"}
  - action_response_pwm
* request_resolve_pwm_on{"pwm": "sala"}
  - action_resolve_pwm_on
* goodbye
  - utter_goodbye

## case happy path 2:
* greet
  - utter_greet
* request_status_led{"led": "quarto"}
  - action_response_led
* request_resolve_led_off{"led": "quarto"}
  - action_resolve_led_off
* request_status_pwm{"pwm": "sala"}
  - action_response_pwm
* request_resolve_pwm_off{"pwm": "sala"}
  - action_resolve_pwm_off
* goodbye
  - utter_goodbye

## case happy path inverse :
* greet
  - utter_greet
* request_status_pwm{"pwm": "sala"}
  - action_response_pwm
* request_resolve_pwm_on{"pwm": "sala"}
  - action_resolve_pwm_on
* request_status_led{"led": "quarto"}
  - action_response_led
* request_resolve_led_on{"led": "quarto"}
  - action_resolve_led_on
* goodbye
  - utter_goodbye

## case happy path without consult led:
* greet
  - utter_greet
* request_resolve_led_on{"led": "quarto"}
  - action_resolve_led_on
* goodbye
  - utter_goodbye

## case happy path without consult pwm:
* greet
  - utter_greet
* request_resolve_pwm_on{"pwm": "sala"}
  - action_resolve_pwm_on
* goodbye
  - utter_goodbye