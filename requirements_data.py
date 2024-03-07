

class Requirements_Data:

    def __init__(self, requirement_type: str, name: str, criticality: str, 
                 status: int, description: str, parent_type: str, parent_id: str):
        
        """
        !!!!  TODO  !!!!
        == add custom field ==
        == add category ==
        """
        # check that all the parameters are of the right type
        string_attributes = [requirement_type, name, criticality, status, description, parent_type]
        for attribute in string_attributes:
            if not isinstance(attribute, str):
                raise ValueError(f'{attribute} must be a string')
            
        if not isinstance(status, int):
            raise ValueError('status must be an integer')
        
        if criticality not in ['MINOR', 'MAJOR', 'CRITICAL', 'UNDEFINED']:
            raise ValueError('criticality must be : MINOR, MAJOR, CRITICAL or UNDEFINED')
        
        if status not in ['UNDER_REVIEW', 'APPROVED', 'OBSOLETE', 'WORK_IN_PROGRESS']:
            raise ValueError('status must be : UNDER_REVIEW, APPROVED, OBSOLET or WORK_IN_PROGRESS')
        if type(parent_id) != type(000):
            raise ValueError('parent_id must be an integer')
        
        if parent_type not in ['requirement', 'requirement-folder']:
            raise ValueError('parent_type must be : requirement or requirement-folder')
        
        self._requirement_type = requirement_type
        self._name = name
        self._criticality = criticality
        self._status = status
        self._description = description
        self._parent_type = parent_type
        self._parent_id = parent_id

    

    def to_dict(self):
        return {
            "_type" : self._requirement_type,
            "current_version" : {
                "_type" : "requirement-version",
                "name" : self._name,
                "criticality" : self._criticality,
                "category" : {
                    "code" : 'CAT_UNDEFINED'
                },
                "status" : self._status,
                "description" : self._description,   
            },
            "parent" : {
                "_type" : self._parent_type,
                "id" : self._parent_id
            }
        }