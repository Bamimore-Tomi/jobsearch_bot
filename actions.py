# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
import logging
from typing import Any, Text, Dict, List, Union, Optional
from rasa_sdk.forms import FormAction
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import urllib.parse as url_parser
import requests
from rasa_sdk.events import SlotSet,EventType
from bs4 import BeautifulSoup as Bs
import re
import requests
import demjson
def get(k_w,jt='None', loc='Lagos', age='None',radius='0',lang='en'):
    try:
        ht = 'https://ng.indeed.com/jobs?q='+k_w+'&l='+loc+'&radius='+radius+'&jt='+jt+'&fromage='+age
        req = requests.get(ht)
    except:
        return dipatcher.utter_message(text='Please, choose another sets of kewords')
    soup = Bs(req.text , 'html.parser')
    js = soup.find_all('script')
    un_matched = str(js)
    try:
        pattern = '\{jk.*\}'
        res = re.findall(pattern, un_matched)
        jobs = []
        for i in res:
            job= demjson.decode(i)
            comp_name=job['cmp']
            title=job['title']
            jobs.append([comp_name,title])
        index=0
        for h in soup.find_all('h2', {'class':'title'}):
            anchor,idn = h.find('a')['href'],h.find('a')['id'][3:]
            jobs[index].append(ht+'&vjk='+str(idn).strip())
            index+=1
        final=[]
        x='''\nCompany Name: {}\nVacancy: {}\nApplication Link: {}'''
        for i in jobs:
            final.append(x.format(*i))
        return final
    except:
        return None


class GetJobs(Action):
    
    def name(self) -> Text:
        return "action_get_jobs"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if tracker.get_slot('field') is not None:
            k_w= tracker.get_slot('field').strip().replace(" ","+")
        else:
            k_w= tracker.latest_message.text
        job_type = tracker.get_slot('job_type')
        loc = tracker.get_slot('location').replace(" ","")
        age = tracker.get_slot('p_age')
        try:
            #dispatcher.utter_message(text='Please wait while I carry out the Job search for you. ⏰⏲️⏱️')
            alljobs = get(k_w, job_type, loc,age)
            print(alljobs)
            txt = '\n'.join(alljobs)
            if len(alljobs)==0: 
                dispatcher.utter_message(text='No jobs avaliable for this location currently.Please, choose other search parameter. start by saying hi')
                return [SlotSet('jobs_gotten', 'false')]
            else:
                dispatcher.utter_message(txt)
                dispatcher.utter_message(text='To search for another job, say HI')
                return [SlotSet('jobs_gotten', 'true')]
        except:
            print(k_w, job_type, loc, age)
        return []
