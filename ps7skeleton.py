import random as rand
import string

class AdoptionCenter(object):
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        self.name = name
        self.species = species_types
        self.location = location
        
    def get_number_of_species(self, animal):
        try:
            return self.species[animal]
        except:
            return 0
        
    def get_location(self):
        x = float(self.location[0])
        y = float(self.location[1])
        return (x,y)

    def get_species_count(self):
        return self.species.copy()

    def get_name(self):
        return self.name
        
    def adopt_pet(self, species):
        self.species[species] -= 1
        if self.get_number_of_species(species) == 0:
            del self.species[species]

class Adopter(object):
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        self.name = name
        self.desired = desired_species
        
    def get_name(self):
        return self.name
        
    def get_desired_species(self):
        return self.desired
        
    def get_score(self, adoption_center):
        score = 1 * adoption_center.get_number_of_species(self.desired)
        return float(score)

class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.consider = considered_species

    def get_score(self, adoption_center):
        adoptscore = Adopter.get_score(self, adoption_center)
        considernumber = 0
        for char in self.consider:
            considernumber += adoption_center.get_number_of_species(char)
        flexscore = 0.3 * considernumber        
        return float(adoptscore + flexscore)
        
class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        self.fear = feared_species

    def get_score(self, adoption_center):
        adoptscore = Adopter.get_score(self,adoption_center)
        fearscore = 0.3 * adoption_center.get_number_of_species(self.fear)
        return float(max(0,adoptscore - fearscore))

class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.allergic = allergic_species

    def get_score(self, adoption_center):
        adoptscore = Adopter.get_score(self,adoption_center)
        for char in self.allergic:
            if adoption_center.get_number_of_species(char) >= 1:
                return 0.0
        return float(adoptscore)

class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        self.med_effect = medicine_effectiveness

    def get_score(self, adoption_center):
        adoptscore = Adopter.get_score(self,adoption_center)
        lowest_eff = 1
        for char in self.allergic:
            if adoption_center.get_number_of_species(char) >=1 and self.med_effect[char] < lowest_eff:
                lowest_eff = self.med_effect[char]
        return float(lowest_eff * adoptscore)

class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.location = location

    def get_linear_distance(self,to_location):
        x1, y1 = self.location
        x2, y2 = to_location
        dist = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        return float(dist)
        
    def get_score(self, adoption_center):
        adoptscore = Adopter.get_score(self,adoption_center)
        if self.get_linear_distance(adoption_center.get_location()) < 1:
            return float(adoptscore)
        elif 1 <= self.get_linear_distance(adoption_center.get_location()) < 3:
            return float(random.uniform(0.7,0.9) * adoptscore)
        elif 3 <= self.get_linear_distance(adoption_center.get_location()) < 5:
            return float(random.uniform(0.5,0.7) * adoptscore)
        else:
            return float(random.uniform(0.1,0.5) * adoptscore)     
    
def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    adoptlistscore = {}
    centerlist = []
    for i in list_of_adoption_centers:
        adoptlistscore[adopter.get_score(i)] = i
    adoptlistscore.sort(reverse=True)
    for k in adoptlistscore:
        centerlist.append(adoptlistscore[k])
    return centerlist
    
def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    adlist = []
    adoptlist = {}
    num = n
    count = 0
    for i in list_of_adopters:
        adoptlist[i]=i.get_score(adoption_center)
    adoptlist.sort(reverse=True)
    while num > 0:
        adlist.append(count)
        num -= 1
        count +=1
    return adlist
