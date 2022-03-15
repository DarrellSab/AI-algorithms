"""""
ISit-18 grupė Darius S.
Užduotis yra su bokšto figūra nueiti į nurodytą langelį ir parodyti patį optimaliausią kelią tai padaryti
Užduočiai išspręsti panaudoti keli AI algoritmai
Tai:
breadth_first_graph_search ir depth_first_graph_search
"""


from search import *

class BokstoEjimai(Problem):
    """""
    Panaudojus esamos būsenos reikšmę, tai langelis, kuriame bokštas ir atlikus nurodytą veiksmą grąžinama
    nauja bokšto vieta, kur jis jau perėjo
    """

    def __init__(self, initial, goal):
        """
         Apibrėžimas tikslo ir problemos inicijavimas
         Čia yra python kalbos konstruktorius inicijuoti klasės egzempliorių
        """
        super().__init__(initial, goal)

    def actions(self, state):

        # Masyve surašomos galimos bokšto ėjimo kryptys
        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']

        # Dabartinė bokšto pozicija, nurodomas pozicijos indeksas
        index_current_square = state

        # Apribojimai
        if index_current_square % 8 == 0:
            if 'LEFT' in possible_actions: possible_actions.remove('LEFT')
        if index_current_square % 8 == 7:
            if 'RIGHT' in possible_actions: possible_actions.remove('RIGHT')
        if index_current_square < 8:
            if 'UP' in possible_actions: possible_actions.remove('DOWN')
        if index_current_square > 55:
            if 'DOWN' in possible_actions: possible_actions.remove('UP')

        return possible_actions


    def result(self, state, action):
        """""
        Panaudojus esamos būsenos reikšmę, tai langelis, kuriame stovi bokštas ir atlikus nurodytą veiksmą grąžinama
        nauja bokšto vieta, kur jis jau perėjo
        """""

        # currentState yra esama būsena
        currentState = state

        # delta pokytis, tai yra kiek turi pasikeisti, o tiksliau kiek pamažėti ar padidėti indekso reikšmė, kad figūra persikeltų
        delta = {'UP': 8, 'DOWN': -8, 'LEFT': -1,  'RIGHT': 1}

        # Sukuriama nauja new_state kintamojo reikšmė
        new_state = currentState + delta[action]

        # Tada gražinama naują būsena
        return new_state

    def goal_test(self, state):
        # Patikrinama, ar bokštas jau pasiekė galutinę būseną
        return state == self.goal

## Surašomos pradinės ir galutinės reiksmės, kad patikrinti algoritmą ##

# Pradinės reikšmės, kadangi Python indeksai nuo nulio, tai eilučių ir stulpelių skaiččiavimas vyksta irgi nuo nulio
pradine_busena_eil = 0;
pradine_busena_st = 1;
# Paskutinis langelis - tikslas kur turi nueiti figūra, kadangi Python indeksai nuo nulio, tai eilučių ir stulpelių skaiččiavimas vyksta irgi nuo nulio
galutine_reiksme_eil = 5;
galutine_reiksme_st = 0;
# Pradinio langelio indekso apskaičiavimas
pradzios_id = pradine_busena_eil * 8 + pradine_busena_st
# Tikslo langelio indekso apskaičiavimas
pabaigos_id = galutine_reiksme_eil * 8 + galutine_reiksme_st
print("Pradinis langelis", pradzios_id)
print("Tikslo langelis", pabaigos_id)

bokstas = BokstoEjimai(pradzios_id, pabaigos_id)

# Čia tikrinami algoritmai, jie duos atsakymą, kaip greičiau nueiti bokštui į nurodytą langelį
solution = breadth_first_graph_search(bokstas).solution()
#solution = depth_first_graph_search(bokstas).solution()

print(solution)
