import re

class TagManipulator():    
    def parse_string(self, tags, regex=""):
        result = []
        
        tempResults = re.split( regex, tags )

        for i in range(tempResults.__len__()):
            tempResults[i] = tempResults[i].lstrip()

        if( len(tempResults[0]) > 0 ):
            result = tempResults 

        return result