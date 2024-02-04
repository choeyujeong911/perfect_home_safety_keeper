# https://horrorgamenews.com/home-safety-hotline-answers/
class Clients:
    def __init__(self):
        # DICT { client's name: hazard }
        self.clients_dict = {'Null': 'No-Such-Name',
                             'Fred': 'Carpenter Ants',
                             'Belinda': 'Attic Gnome',
                             'Jay': 'Autumn Vines',
                             'Paul': 'Bed Bugs',
                             'Christie': 'Bed Hag',
                             'Harvey': 'Bed Teeth',
                             'Mike': 'Black Mold',
                             'Gary': 'Boggart',
                             'John': 'Cockroaches',
                             'Hunnigan': 'Common Hobb',
                             'Robert': 'Common Hobb',
                             'Dan': 'Desk Hobb',
                             'Claire': 'Fae Feast',
                             'Phil': 'Fae Flu',
                             'May': 'False Artifact',
                             'Ash': 'False Beet',
                             'Pamela': 'False Plant',
                             'Albert': 'Floor Roots',
                             'Ashley': 'Fracture Hobb',
                             'Peter': 'Frozen Pipes',
                             'Linda': 'Grotto Basement',
                             'Ramona': 'Horde',
                             'Andy': 'Lamp Sprite',
                             'Charles': 'Leprechaun',
                             'Quaid': 'Memory Wisp',
                             'Grace': 'Mice',
                             'Michelle': 'Mice',
                             'Howie': 'Mirror Nymph',
                             'Hank': 'Mole',
                             'Jill': 'Neighbors Doorway',
                             'Felicia': 'Night Gnome',
                             'Maple': 'Night Wisp',
                             'Rachael': 'Pooka',
                             'Patty': 'Portal',
                             'Jules': 'Soap Sprite',
                             'Howard': 'Spriggan',
                             'Patrice': 'Sprig Tree',
                             'Reed': ['Stair Slug', 'Wood Secretions'],
                             'David': 'Stair Slug',
                             'Sheila': 'Tea Sprite',
                             'Tim': 'Ticks',
                             'Wanda': 'Termites',
                             'Jackie': 'Travel Gnome',
                             'Edward': 'Troll',
                             'Kyle': 'Unicorn Fungi',
                             'Carla': 'Whistling Fungi',
                             'Brittany': 'Wine Sprite',
                             'Prank-Call': 'Just-Prank-Call'
                             }

    def how_can_i_help_u(self, client: str):
        print(">> {0}\n".format(self.clients_dict[client]))

if __name__ == '__main__':
    helper = Clients()
    print("If you want to finish typing, type 'q' to")
    while True:
        name = input("Who is it ? : ")
        name = name.lower()
        name = name.capitalize()
        if name == "q" or name == "Q":
            break
        elif name not in helper.clients_dict.keys():
            name = 'Null'
        helper.how_can_i_help_u(name)