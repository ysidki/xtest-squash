import logging 
from requirements_data import Requirements_Data

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class Requirements:

    def __init__(self, session):
        self._session = session

        url = session.url

        self._apis= {
            'get_all_requirements' : url + '/requirements', 
            'create_requirement' : url + '/requirements',
            'modify_requirement' : lambda id: url + '/requirements/{}'.format(id),
            'delete_requirement' : lambda ids: url + '/requirements/{}' + ','.join(map(str, ids)),
            'get_requirement' : lambda id: url + '/requirements/{}'.format(id),
            'get_requirement_children' : lambda id: url + '/requirements/{}/children'.format(id),
            'get_issues_requirement' : lambda id: url + '/requirements/{}/issues'.format(id),
            'link_test_to_requirement' : lambda id,testcases: url + '/requirements/{}/coverages/{}'.format(id, ','.join(map(str, testcases))),
            'unlink_test_to_requirement' : lambda id,testcases: url + '/requirements/{}/coverages/{}'.format(id, ','.join(map(str, testcases))),
        }


    def get_all_requirements(self):
        """
        get all requirements. 

        Returns: a dictionnary of all requirements
        """
        LOGGER.info('Getting all requirements from '+ self._apis['get_all_requirements'] + "\n")
        response = self._session.get_session.get(self._apis['get_all_requirements'])
        dict_response = response.json()
        
        return [dict_response, response.status_code]
    
    def create_requirement(self, requirement_type, name, criticality, status, description, 
                           parent_type, parent_id):
        """
        create a requirement. 

        Args:
            _type : the type of the requirement | Mandatory \
                values=(requirement, requirement-folder)
            current_version : object | Mandatory 
            parent : object | Mandatory

        Returns: a dictionnary of the created requirement

        """
    
        data = Requirements_Data(requirement_type, name, criticality, 
                                 status, description, parent_type, parent_id)
        
        dict_data = data.to_dict()
        
        LOGGER.info('Creating requirement '+ name + ' with data: ' + str(dict_data) + "\n")

        response = self._session.get_session.post(self._apis['create_requirement'], json=dict_data)
        dict_response = response.json()
        
        return [dict_response, response.status_code]
    
    def modify_requirement(self, id, name, description, parent_id=None):
        """
        modify a requirement. 

        Args:
            id: the id of the requirement
            name: the name of the requirement
            description: the description of the requirement
            parent_id: the parent id of the requirement

        Returns: a dictionnary of the modified requirement
        """

        data = Requirements_Data('requirement', name, 'UNDEFINED',)
        

        print('Modifying requirement '+ name)
        data = {
            'name': name,
            'description': description,
            'parentId': parent_id
        }
        response = self._session.get_session.put(self._apis['modify_requirement'](id), json=data)
        response_json = response.json()
        
        return response_json
    
    def delete_requirement(self, ids):
        """
        delete a requirement. 

        Args:
            ids: the ids of the requirement

        Returns: a dictionnary of the deleted requirement
        """
        print('Deleting requirement '+ ','.join(map(str, ids)))
        response = self._session.get_session.delete(self._apis['delete_requirement'](ids))
        response_json = response.json()
        
        return response_json
    

    def get_requirement(self, id):
        """
        get a requirement. 

        Args:
            id: the id of the requirement

        Returns: a dictionnary of the requirement
        """
        print('Getting requirement '+ id)
        response = self._session.get_session.get(self._apis['get_requirement'](id))
        response_json = response.json()
        
        return response_json
    

    def get_requirement_children(self, id):
        """
        get the children of a requirement. 

        Args:
            id: the id of the requirement

        Returns: a dictionnary of the children of the requirement
        """
        print('Getting children of requirement '+ id)
        response = self._session.get_session.get(self._apis['get_requirement_children'](id))
        response_json = response.json()
        
        return response_json
    


    def get_issues_requirement(self, id):   
        """
        get the issues of a requirement. 

        Args:
            id: the id of the requirement

        Returns: a dictionnary of the issues of the requirement
        """
        print('Getting issues of requirement '+ id)
        response = self._session.get_session.get(self._apis['get_issues_requirement'](id))
        response_json = response.json()
        
        return response_json
    
    def link_test_to_requirement(self, id, testcases):
        """
        link a test to a requirement. 

        Args:
            id: the id of the requirement
            testcases: the testcases to link to the requirement

        Returns: a dictionnary of the linked testcases
        """
        print('Linking testcases to requirement '+ id)
        response = self._session.get_session.post(self._apis['link_test_to_requirement'](id, testcases))
        response_json = response.json()
        
        return response_json
    
    def unlink_test_to_requirement(self, id, testcases):
        """
        unlink a test to a requirement. 

        Args:
            id: the id of the requirement
            testcases: the testcases to unlink to the requirement

        Returns: a dictionnary of the unlinked testcases
        """
        print('Unlinking testcases to requirement '+ id)
        response = self._session.get_session.delete(self._apis['unlink_test_to_requirement'](id, testcases))
        response_json = response.json()
        
        return response_json
    
    def __str__(self):
        return "Requirements: " + self._session.username + " " + self._session.password + " " + self._session.url

    




