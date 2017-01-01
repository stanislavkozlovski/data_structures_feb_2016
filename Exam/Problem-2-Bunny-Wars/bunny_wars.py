import datrie
import string
from sortedcontainers import SortedDict, SortedSet


class Bunny:
    def __init__(self, name, teamid, room):
        self.name = name
        self.reversed_name = ''.join(reversed(name))
        self.room = room
        self.health = 100
        self.score = 0
        self.team = teamid

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __gt__(self, other):
        return self.name > other.name

    def __lt__(self, other):
        return self.name < other.name


class Room:
    def __init__(self, id):
        self.id = id
        self.bunny_count = 0
        self.bunnies = dict()

    def __hash__(self):
        return hash(id)

    def __eq__(self, other):
        return self.id == other.id

    def __gt__(self, other):
        return self.id > other.id

    def __lt__(self, other):
        return self.id < other.id

    def __len__(self):
        return self.bunny_count

    def detonate(self, bunny):
        """
        Detonate bunnyName – detonates the bunny, causing all bunnies from other teams in the same room
           to suffer 30 damage to their health (their health is reduced by 30).

        If a bunny with the given name does not exist, the command should throw an exception.
        If a bunny falls to 0 or less health as a result of the detonation, it should be removed from the game.

        For each removed enemy bunny, the detonated bunny should gain +1 score.
        """
        score = 0
        dead_bunnies = []
        orig_bunny_team = bunny.team
        for team_id in self.bunnies.keys():
            if team_id != orig_bunny_team:
                for enemy_bunny in self.bunnies[team_id].values():
                    enemy_bunny.health -= 30
                    if enemy_bunny.health <= 0:
                        dead_bunnies.append(enemy_bunny)
                        score += 1
        for dead_bunny in dead_bunnies:
            del self.bunnies[dead_bunny.team][dead_bunny.name]
        bunny.score += score
        return dead_bunnies

    def add_bunny(self, bunny_name, team_id):
        if team_id not in self.bunnies:
            self.bunnies[team_id] = dict()
        bunny = Bunny(name=bunny_name, teamid=team_id, room=self.id)
        self.bunnies[team_id][bunny_name] = bunny
        self.bunny_count += 1
        return bunny

    def move_bunny_in(self, bunny: Bunny):
        if bunny.team not in self.bunnies:
            self.bunnies[bunny.team] = dict()
        self.bunnies[bunny.team][bunny.name] = bunny
        self.bunny_count += 1

    def remove_bunny(self, bunny):
        self.bunny_count += 1
        del self.bunnies[bunny.team][bunny.name]


class BunnyWars:
    def __init__(self):
        self.rooms_by_idx = SortedSet()  # integer ID only
        self.rooms = SortedDict()  # key: id, value: room
        self.bunnies_by_team = {}  # key: team id, value: SortedSet(key=bunny.reversed_name) of Bunny objects
        self.bunnies_by_suffix = datrie.Trie(string.ascii_letters)
        self.bunny_names = {}

    def next_bunny(self, bunny_name):
        if bunny_name not in self.bunny_names:
            raise Exception()
        bunny = self.bunny_names[bunny_name]
        old_room_id = bunny.room
        old_room = self.rooms[old_room_id]
        next_room_index = self.rooms_by_idx.index(old_room_id) + 1
        if next_room_index >= len(self.rooms_by_idx):
            next_room_index = 0
        new_room_id = self.rooms_by_idx[next_room_index]
        bunny.room = new_room_id

        new_room = self.rooms[new_room_id]

        old_room.remove_bunny(bunny)
        new_room.move_bunny_in(bunny)

    def prev_bunny(self, bunny_name):
        if bunny_name not in self.bunny_names:
            raise Exception()
        bunny = self.bunny_names[bunny_name]
        old_room_id = bunny.room
        old_room = self.rooms[old_room_id]
        next_room_index = self.rooms_by_idx.index(old_room_id) - 1
        if next_room_index < 0:
            next_room_index = len(self.rooms_by_idx)-1
        new_room_id = self.rooms_by_idx[next_room_index]
        bunny.room = new_room_id
        new_room = self.rooms[new_room_id]
        old_room.remove_bunny(bunny)
        new_room.move_bunny_in(bunny)

    def bunny_count(self):
        return len(self.bunny_names)

    def room_count(self):
        return len(self.rooms)

    def list_bunnies_by_team(self, team_id):
        return reversed(self.bunnies_by_team[team_id])

    def list_bunnies_by_suffix(self, suffix):
        return self.bunnies_by_suffix.values(''.join(reversed(suffix)))

    def detonate(self, bunny_name):
        if bunny_name not in self.bunny_names:
            raise Exception('Bunny does not exist!')
        bunny = self.bunny_names[bunny_name]
        room = self.rooms[bunny.room]
        dead_bunnies = room.detonate(bunny)
        for dead_bunny in dead_bunnies:
            self._delete_bunny(dead_bunny)

    def add_room(self, id):
        """
        Add roomId – adds a room to the structure.
            Rooms have unique ids.
            Rooms should be situated according to their id in ascending order.
            If a room with the given Id exists the command should throw an exception.
        """
        if id in self.rooms:
            raise Exception('Room with id {id} is already registered!'.format(id=id))
        self.rooms_by_idx.add(id)
        self.rooms[id] = Room(id)

    def add_bunny(self, bunny_name, team_id, room_id):
        if room_id not in self.rooms or team_id > 4 or team_id < 0:
            raise Exception('Invalid room/team id!')
        if bunny_name in self.bunny_names:
            raise Exception('A bunny with the given name already exists!')
        # 1. Add to the room
        bunny_obj = self.rooms[room_id].add_bunny(bunny_name, team_id)
        # 2. Add to overall bunnies
        self.bunny_names[bunny_name] = bunny_obj
        # 3. Add to suffixes
        self.bunnies_by_suffix[bunny_obj.reversed_name] = bunny_obj
        # 4. Add to bunnies by team
        if bunny_obj.team not in self.bunnies_by_team:
            self.bunnies_by_team[bunny_obj.team] = SortedSet()
        self.bunnies_by_team[bunny_obj.team].add(bunny_obj)

    def remove_room(self, room_id):
        if room_id not in self.rooms:
            raise Exception('A room with the id {id} does not exist!'.format(id=room_id))
        room = self.rooms[room_id]
        del self.rooms[room_id]
        self.rooms_by_idx.remove(room_id)

        # delete every bunny there
        for bunnies_from_team in room.bunnies.values():
            for bunny in bunnies_from_team.values():
                self._delete_bunny(bunny)

    def _delete_bunny(self, bunny: Bunny):
        # 1.Remove from overall bunnies
        del self.bunny_names[bunny.name]
        # 2.Remove from suffixes
        del self.bunnies_by_suffix[bunny.reversed_name]
        # 3.Remove from bunnies by team
        self.bunnies_by_team[bunny.team].remove(bunny)

bra_wars = BunnyWars()
bra_wars.add_room(3)
bra_wars.add_room(4)
bra_wars.add_room(1)
bra_wars.add_bunny("Alei", 2, 3)
bra_wars.add_bunny("Drizzy", 2, 3)
bra_wars.add_bunny("Rrizzy", 3, 4)
bra_wars.add_bunny("REAL", 3, 3)
bra_wars.prev_bunny("Rrizzy")
bra_wars.next_bunny("Rrizzy")
bra_wars.next_bunny("Rrizzy")
bra_wars.next_bunny("Rrizzy")
bra_wars.detonate("Alei")
bra_wars.detonate("Alei")
bra_wars.detonate("Alei")
bra_wars.remove_room(3)
bra_wars.add_room(3)
print("Bunnies alive -> {}".format(bra_wars.bunny_count()))
print("Detonating Alei")
# bra_wars.detonate("Alei")
print("Bunnies alive -> {}".format(bra_wars.bunny_count()))

# alei = bra_wars.bunny_names["Alei"]
print(bra_wars.room_count())
# print(alei.score)

# bra_wars.detonate("Alei")
# bra_wars.detonate("Alei")
# bra_wars.detonate("Alei")

# bra_wars.add_bunny("Tpen", 2, 3)
# bra_wars.add_bunny("apen", 2, 3)
# bra_wars.add_bunny("aapen", 2, 3)
# bra_wars.add_bunny("bapen", 2, 3)
# bra_wars.add_bunny("bpen", 2, 3)
# nubbies = bra_wars.list_bunnies_by_suffix("pen")
# for nub in nubbies:
#     print(nub.name)
#
# team_3 = bra_wars.list_bunnies_by_team(3)  # Rrizzy
# for drizzy in team_3:
#     print(drizzy.name)