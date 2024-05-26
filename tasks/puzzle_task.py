from textwrap import dedent
from crewai import Task


class PuzzleTask():
    def create_initial_murdle_json_task(self, agent, input_text,output_file_path):
        input_msg = '''
                !create a json that would be used for creating MURDLE puszzle on next step. 
                here what need to be created:
                
                
                Rules for filling json.
                
               Location - 1 short sentence of description of location, with in description of Setting. It should have next attributes: Indoor/outdoor, Accessibility, Lighting, Noise Level. There should not be all Locations with same attributes.
                Setting: Select multiple possible locations for the murder within your story’s setting. Each location should have unique features that can be referenced in clues.
                
                # Suspects - 5 sentences of description of character, with includes Character Depth, Alibis and Motives. In 1 sentence describe sustpect background.. These sentence shuold also include attributes all suspects attributes that include in this description. The most distinctive features of appearance and the most important elements of clothing.
                Character Depth: Create suspects with distinct personalities, backgrounds, occupation, and potential motives. A mix of obvious and obscure suspects adds complexity. Describe relation ship with victim and with one of other suspects.
                Alibis and Motives: Give each suspect a motive for committing the crime but also provide them with possible alibis that can be proven true or false through clues.
                It should have also next attributes: height, right/left handed, color and hair style, clothing and ant its colors. use profession and name to identify suspects
                
                Motives - 2 sentences of reason of crime. It should be based on history of relation of suspect and victim. In most cases it shold be consist to other story. Sometimes be very creative, so this movive should be very suprisive and captive. Motive shoud be general and not connected to any specific person. Here it shoud be just general description of motive that coud be fit to anyone. there shoudl be same amount of motives as suspects.
                
                Weapons - 2 sentence of description of weapon, it should be comprehensive a artistic description in conjunction with attributes. Description should add additional atmosphere. It should have next attributes: type,  light/heavy weight, material, Condition, Ease of Use, Potential for Silence.
                Variety: Choose a range of potential murder weapons, each with distinct characteristics or implications (e.g., a knife, a poison, a firearm). Be more creative when you would be imagine a weapons. be unexpected. 30% of weapon should be unexpected and creative. This variety allows for more nuanced clues. Do not use all Atributes for each weapon, select most significant for that weapon.
                Plausibility: Ensure the weapons are plausible within the setting of your story and can be logically connected to the murder. Ensure that all weapons cannot have same combination of attributes. 
                
                # SWL - purpose is to asign each ssupect only one location and one wheapon where they were during murder. only one can me killer. assigning weapons should be logically connected to their atributes.
                
                 # Scenario:
                Scenario description - should have no more 15 sentence. 1  sentence for general background and scene. 3 sentences for creating atmosphere. 2 Sentences describe the victim (His name ccupation, appearence, clothes). 1 for describing reletionship between each suspects and victim. 2 sentence for highlevel describing what was happened in background before crime, without descibing direct people, weapons, butcould be includng locations. 1 sentence for describing the crime scene (without describing location, without suspect and withuot weapon). 
                Theme: Decide on a theme or setting for your story (e.g., a dinner party, a haunted mansion). The setting will influence the suspects, weapons, and locations.
                
                Victim description: describe his background and profession, where he was seen before the crime and what he was doing before. total 5 sentences.
                Victim appearance: 5 sentences of description of victim, with includes Height,age, Hair Style, Clothing in details and its colors.
                Motivation: Each character should have a potential motive for committing the crime, adding depth and red herrings to your puzzle.
                
                Scenario title - should be 3-5 words title that describes whole scenario. no any clues should be in title related to location and weapon, either suspect.
                
                Crime scene description - 2 sentence of description of crime scene. It should be based on suspect (who is killer) location and victim description, bu it shuod not be directed lead who is a killer. It should have next attributes: Condition of the body, Position of the body, Evidence of struggle, Evidence of entry, Evidence of exit. Location should be  location of killer from SWL. use direct name of location in this description. Location shod not be private place of killer.
                                
                here is example 
                    {
                    "Suspects": {"Full_suspect_Name": {"description": "suspect_description", "attributes" : ["Suspects attributes as a list"]}},
                    "Weapons" :{"Short_weapon_name": {"description": "weapon_description", "attributes" : ["weapon attributes as a list"]}},
                    "Locations" :{"Short_location_name": {"description": "location_description", "attributes" : ["location attributes as a list"]}},
                    "Motive" : {"Short_motive_name": {description: "motive_description", "attributes" : ["motive attributes as a list"]}},
                    "SWLM" : {"suspect_name" : {"location" : "suspect location", "weapon": "suspect weapon", "motive": "suspect motive", "is_killer": true/false}},
                    "Scenario":{"name": "scenario_title", 
                    "Description": "scenario Description", 
                    "CrimeScene": "crime_scene_description", 
                    "visual_style": "theme",
                    "victim": {"name": "victim_name", "occupation": "victim_occupation", "appearence": "victim_appearence", "clothes": "victim_clothes"},
                    "suspect_relations": ["suspect1":"relation", "suspect2":"relation", ...]}
                    }
                
                your json should be based n next information: \n"""''' + input_text + '\n"""'

        return Task(description=dedent(input_msg),
                    agent=agent,
                    output_file=output_file_path,
                    # output_json="JSON.json",
                    expected_output='''
                    return raw json. no any quotes or braces. 
                    
                    '''
                    )

    def create_clues_task(self, agent, output_file_path):

        old_task = """
            you will have a json with a data. 
                    
                    !Add new information to input json with clues that would help to identify who is a killer.
                    
                    you will have a json with a data. 
                    Create a clues that would help to identify who is a killer. 
                    for all clues do not use direct names of locations, weapons, and suspects names. Use only their attributes in clue description.
                    use unique combination of attributes of suspects, locations and weapons to create clues. It should be easy to identify element by its attributes.
                    
                    all clues should be one short sentence.
                    use SWL from json to identify it connection between suspect, location and weapon. 
                    it should be numerated list of clues.
                    
                    types of clues:
                    PSW - POSITIVE SUSPECT WEAPON - that describes who was seen with weapon. 
                    PLW - POSITIVE LOCATION WEAPON - that describes where weapon was seen.
                    PSL - POSITIVE SUSPECT LOCATION - that describes where suspect was seen.
                    NSW - NEGATIVE SUSPECT WEAPON - that describes who was not seen with weapon.
                    NLW - NEGATIVE LOCATION WEAPON - that describes where weapon was not seen.
                    NSL - NEGATIVE SUSPECT LOCATION - that describes where suspect was not seen.
                    PSM - POSITIVE SUSPECT MOTIVE - that describe who has a motive
                    NSM - NEGATIVE SUSPECT MOTIVE - that describes whom does not have motive
                    ADD - additional clue where was found body and what was condition of the body. It should expand location of killer and weapon of killer, without describing approach of kill.
                    Check clues to consist this rules. before printing
                    2 clues in a row should not be related to same suspect, location or weapon.
                    
                                        
                    IF there are 3 suspects select one of option for Clues: 
                    option 3A: 1 PSW + 1 PLW + 1 PSL + ADD
                    option 3B: 1 PSW + 1 PSL + NSW + NLW + NSL + ADD
                    option 3C: 1 PSW + 1 PLW + NSW + NLW + NSL + ADD
                    option 3D: 1 PLW + 1 PSL + NLW + NSL + ADD
                    
                    IF there are 4 suspects select one of option for Clues: :
                    Option 4A: PSW + PLW + PSL + NSW + NLW + NSL + PWS + ADD
                    Option 4B: PSW + PLW + PSL + NLW + NSL + PWS + PLW + ADD
                    
                    Select one option and build clues and its description according to that option depends on number of suspect.
                    Negative and positive should not be related to suspect, location, weapon that was already mention in positive sign of clue.
                    all attributes should be bold
                    do not provide clues about killer.
                    think before generating answer.
                    Before print updated json with clues, verify that all clues are correct and align with SWL.
                    Before print updated json with clues verify it for consisntenly and logical connection between suspects, locations and weapons. It should not contradict SWL information.
                    
                    
                    
                    """
        old_json = """return raw json. no any quotes or braces..
                     here is example of json structure for answer:  
                    { 
                'Suspects': {'name': {'description': suspect_description, 'attributes' : [Suspects attributes as a list]}},
                'Weapons' :{'name': {'description': weapon_description, 'attributes' : [weapon attributes as a list]}},
                'Locations' :{'name': {'description': location_description, 'attributes' : [location attributes as a list]}}
                'Motive' : {'name': {'description': 'motive_description', 'attributes' : ['motive attributes as a list']}},
                'Scenario':{'name': 'scenario_title', 
                'Description': 'scenario Description',  
                'visual_style': 'theme',
                'victim': {'name': 'victim_name', 
                'occupation': 'victim_occupation',
                 'appearence': 'victim_appearence', 
                 'clothes': 'victim_clothes'}, 
                 'suspect_relations': ['suspect1':'relation', 'suspect2':'relation', ...]},
                 'SWLM' : {'suspect_name' : {'location' : 'suspect location', 'weapon': 'suspect weapon', 'motive': 'suspect motive', 'is_killer': true/false}},
                'clues' : [clue1, clue2, clue3, ...] }"""

        new_task = '''
        you will have a json with a data. 

!Add new information to input json with clues that would help to identify who is a killer.

you will have a json with a data. 
Create a clues that would help to identify who is a killer. 
for all clues do not use direct names of locations, weapons, and suspects names. Use only their attributes in clue description.
Use unique combination of attributes of suspects, locations and weapons to create clues. It should be easy to identify element by its attributes.

all clues should be one short sentence.
use SWL from json to identify it connection between suspect, location and weapon. 
it should be numerated list of clues.

At whe beginning describe crime scene with 1 sentence - it should be always a killer location and store it to variable MURDER_LOCATION.



types of clues:
PSW - POSITIVE SUSPECT WEAPON - that describes who was seen with weapon. 
PLW - POSITIVE LOCATION WEAPON - that describes where weapon was seen.
PSL - POSITIVE SUSPECT LOCATION - that describes where suspect was seen.
PSM - POSITIVE SUSPECT MOTIVE - that describe who has a motive
NSW - NEGATIVE SUSPECT WEAPON - that describes who was not seen with weapon.
NLW - NEGATIVE LOCATION WEAPON - that describes where weapon was not seen.
NSL - NEGATIVE SUSPECT LOCATION - that describes where whom was not seen.
NSM - NEGATIVE SUSPECT MOTIVE - that describes whom does not have motive
SST - SUSPECT STATEMENT - 1-2 sentences of suspect statement. it should be any of other type of clues, described what suspect heard or seen, it could be also blaiming other person. it could be supporing own or other person alibi. All person statement shuod be TRUE, except killer. Killers statments always should be Lie.




Check clues to consist this rules. before printing


Your task is to update SWL section of json.
each person should have own PSW, PLW, PSL clues in own part. 

Return only json with clues in text block, nothing more. 

here is example of returned SWL section:
"""
{"SWL" : {"suspect_name" : {"location" : suspect location, "weapon": suspect weapon,"motive":"suspect motive", "is_killer": true/false}, 
"clues": {
"PSW":"psw_clu", "PLW":"plw_clue", "PSL":"psl_clue","PSM":"psm_clue", 
"SST":"sst_clue", 
"NSW":"nsw_clue", "NLW":"nlw_clue", "NSL":"nsl_clue", "NSM":"SNM_clue"}}
}
"""
        '''
        new_json = """return raw json. no any quotes or braces..
                     here is example of json structure for answer:
        {"SWL" : {"suspect_name" : {"location" : suspect location, "weapon": suspect weapon,"motive":"suspect motive", "is_killer": true/false}, 
        "clues": {
        "PSW":"psw_clu", "PLW":"plw_clue", "PSL":"psl_clue","PSM":"psm_clue", 
        "SST":"sst_clue", 
        "NSW":"nsw_clue", "NLW":"nlw_clue", "NSL":"nsl_clue", "NSM":"SNM_clue"}}
        }
        """

        return Task(description=dedent(new_task),
                    agent=agent,
                    expected_output=new_json,

                    output_file=output_file_path,
                    )

    # clue rules:
    # 1.	NUMBER OF CLUES should be next - (sum(Locations) + sum(suspects) + sum(weapons)) /2 + 1
    # 2.	All clues should be numerated.
    # 3.	Each clues should be only 1 sentence.
    # 4.	INSTRUCTION TO WORK WITH CLUES:
    # 5.	ALL CLUES MUST BE BASED ON A SWL information.
    # 6.	There could be POSITIVE clues: (e.g. person (without name) with attribute was seen near attribute of location or location name).
    # 7.	There could be negative clues: (e.g. person  (without name) with attribute wasn’t seen with attribute weapon)
    # 8.	Most of clues should be positive.
    # 9.	All clues should be lead to make conclusion that gives results same as SWL information.
    # 10.	Do not provide a clues by direct name of weapon, suspect or location. Preferably Clues should have attributes of weapon, location or suspect, than their names.
    # 11.	You can do exception only 2 times one for one obvious weapon, and one time for location. That means you must user direct location name only once, and only once for weapon name. But both mustn’t be related to murder.
    # 12.	MUST: ONLY last clue could be related to murder weapon, location and killer. Show location of the murder and condition of the body. This condition could be additional clue and help to identify murder weapon, but it should not describe of Attributes of murder weapon. Only approach. Only last clue should lead to place and weapon of murder. Here you can describe direct location.
    # 13.	MUST: There have not me a clue connected real killer to murder location.
    # 14.	MUST: There have not be any clue that describe where killer was, and no any killer attributes should not related to any location.
    # 15.	MUST: There have not be a clue connected real killer to murder weapon.
    # 16.	MUST: There have not be a clue connected murder weapon to murder location.
    # 17.  MUST: in one clue have not me mention of all 3 elements (or their attributes) from same element of wsl. max 2 property of same element could be in one clue.
    # 18.	There should be no misleading statements. If users didn’t ask for it.
    # 19.	Clues should not contradict each other.
    # 20.	There should not be any clues that just describe just one element. All clues should leads to some logical conclusion. Not just description of elements or their attributes.
    # 21.	There should not be clues that duplicate connection descripton.
    # 22.	Conclusions about the connection of elements must be made only from one clue, and not from several.
    # 23.	Connection to Elements: Clues should be carefully crafted to relate directly to one or more of the suspects, weapons, and locations. They should allow players to logically exclude certain combinations of these elements.
    # 24.	Clues should balance of using names of elements and their attributes.
    # 25.	DO NOT use any additional description or headend meaning of elements that user should guess. Use only names of elements and its attributes. User shouldn’t do any assumption of related clues to any attribute of any element.
    # 26.	ALL ELEMENTS or their ATTRIBUTES should be bold in clues.
    # 27.	!THINK Before Creating CLUES. READ carefully rules for Clues. Count required amount off clues according to rule below. All clues should be created according to rules.
    # 28.	Do clues at first internally without printing. That solve the task according the clues. Try to get same conclusion and in SWL table. If conclusion same – print clues to user. Repeat internal generation clues, until result of conclusion would be equal to SWL table