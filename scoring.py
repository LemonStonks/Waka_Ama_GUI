class scoring_c():
    def __init__ (self):
        pass
    
    @staticmethod
    def return_scores(formatted_file_contents, points_reference): # file_content is a list
        # this returns the regional association scores
        
        last_option = False
        if list(points_reference.keys())[-1] == ">":
            last_option = True
            last_option_value = list(points_reference.values())[-1]
            points_reference.pop(">") # removes the " last option "
            
        regional_association_scoring = {}
        
        team_list = formatted_file_contents[1] # gets the list of the team
        last_points_reference = list(points_reference.keys())[-1]
        
        for team_dict in team_list:
            team_place = team_dict["place"]
            team_regional_association = team_dict["regional_association"]
            for place_reference in points_reference.keys():
                if place_reference == team_place:
                    
                    if team_regional_association in regional_association_scoring:
                        regional_association_scoring[team_regional_association] += points_reference[place_reference]
                    else:
                        regional_association_scoring[team_regional_association] = points_reference[place_reference]
                
                elif last_option == True and team_place > last_points_reference:
                    if team_regional_association in regional_association_scoring:
                        regional_association_scoring[team_regional_association] += last_option_value
                    else:
                        regional_association_scoring[team_regional_association] = last_option_value
                        
        return regional_association_scoring
    
    @staticmethod
    def return_year_score(file_region_score_list): # {filename: {reg1:100, reg2:200}, filename{reg1:100, reg2:200}}
        # this returns the total year score e.g {reg1:500, reg2:600}
        
        scores_dictionary = {}
        
        for scores_dictionary in file_region_score_list: # [{scores_dictionary}]
            
            for i in scores_dictionary: # {regionalassoc:1}
                if i in scores_dictionary: # scores{reg} == reg
                    scores_dictionary[i] += scores_dictionary[i]
                else:
                    scores_dictionary[i] = scores_dictionary[i]
                    
        return scores_dictionary
    
    @staticmethod
    def score_sort(regional_association_score_dictionary):
        # To sort out the dictionary by values in descending order
        sorted_desc_scores = dict(sorted(regional_association_score_dictionary.items(), key=lambda item: item[1], reverse=True))
        return sorted_desc_scores                        