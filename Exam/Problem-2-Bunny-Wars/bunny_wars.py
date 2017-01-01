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

    def __str__(self):
        return self.name


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
        orig_bunny_team_id = bunny.team
        for team_id in self.bunnies.keys():
            # go through each bunny that's not from the original bunny's team
            if team_id != orig_bunny_team_id:
                for enemy_bunny in self.bunnies[team_id].values():
                    enemy_bunny.health -= 30
                    if enemy_bunny.health <= 0:
                        dead_bunnies.append(enemy_bunny)
                        score += 1
        for dead_bunny in dead_bunnies:  # delete each dead bunny
            del self.bunnies[dead_bunny.team][dead_bunny.name]
        bunny.score += score
        return dead_bunnies  # return the dead bunnies to be deleted from other collections

    def add_bunny(self, bunny):
        """ Adds the bunny to the room"""
        if bunny.team not in self.bunnies:
            self.bunnies[bunny.team] = dict()
        self.bunnies[bunny.team][bunny.name] = bunny
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
        self._move_bunny(bunny_name)

    def prev_bunny(self, bunny_name):
        self._move_bunny(bunny_name, prev=True)

    def bunny_count(self):
        return len(self.bunny_names)

    def room_count(self):
        return len(self.rooms)

    def list_bunnies_by_team(self, team_id):
        """
        ListBunniesByTeam teamId - returns all bunnies from the specified team in (sorted by name in descending order).
        """
        return reversed(self.bunnies_by_team[team_id])

    def list_bunnies_by_suffix(self, suffix):
        """
        ListBunniesBySuffix suffix -
            returns all bunnies ending with the specified suffix (sorted by the ASCII code of the reversed name
            in ascending order as a first criteria and by length in ascending order as a second criteria).
            Example Tpen < apen < aapen < bapen < bpen.
        """
        return self.bunnies_by_suffix.values(''.join(reversed(suffix)))

    def detonate(self, bunny_name):
        if bunny_name not in self.bunny_names:
            raise Exception('Bunny does not exist!')
        bunny = self.bunny_names[bunny_name]
        room = self.rooms[bunny.room]
        dead_bunnies = room.detonate(bunny)  # detonate the bunny and get all the bunnies that have died
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
        bunny_obj = Bunny(name=bunny_name, teamid=team_id, room=room_id)
        # 1. Add to the room
        self.rooms[room_id].add_bunny(bunny_obj)
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

    def _move_bunny(self, bunny_name, prev=False):
        if bunny_name not in self.bunny_names:
            raise Exception()
        bunny = self.bunny_names[bunny_name]
        old_room_id = bunny.room
        old_room = self.rooms[old_room_id]
        old_room_index = self.rooms_by_idx.index(old_room_id)
        if prev:
            next_room_index = old_room_index - 1
        else:
            next_room_index = old_room_index + 1
        if next_room_index >= len(self.rooms_by_idx) or next_room_index < 0:  # is out of bounds
            next_room_index = 0 if prev else len(self.rooms_by_idx) - 1
        # get the new room id and assign it to the bunny
        new_room_id = self.rooms_by_idx[next_room_index]
        bunny.room = new_room_id
        new_room = self.rooms[new_room_id]
        # remove the bunny from the old room and move it to the new one
        old_room.remove_bunny(bunny)
        new_room.move_bunny_in(bunny)

    def _delete_bunny(self, bunny: Bunny):
        # 1.Remove from overall bunnies
        del self.bunny_names[bunny.name]
        # 2.Remove from suffixes
        del self.bunnies_by_suffix[bunny.reversed_name]
        # 3.Remove from bunnies by team
        self.bunnies_by_team[bunny.team].remove(bunny)


def main_loop():
    """ Take commands from the bunny wars commander! """
    wars = BunnyWars()
    while True:
        command = input()
        args = command.split()
        if command.startswith('Add'):
            # add commands
            if len(args) > 2:  # add a bunny
                bunny_name = args[1]
                team_id = int(args[2])
                room_id = int(args[3])
                wars.add_bunny(bunny_name, team_id, room_id)
            else:  # add a room
                room_id = int(args[1])
                wars.add_room(room_id)
        elif command == 'BunnyCount':
            print('The amount of bunnies is: {}'.format(wars.bunny_count()))
        elif command == 'RoomCount':
            print('The amount of rooms is: {}'.format(wars.room_count()))
        elif command.startswith('Remove'):
            # remove a room
            room_id = int(args[1])
            wars.remove_room(room_id)
        elif command.startswith('Next'):
            # move the bunny to the next room
            bunny_name = args[1]
            wars.next_bunny(bunny_name)
        elif command.startswith('Previous'):
            # move the bunny to the previous room
            bunny_name = args[1]
            wars.prev_bunny(bunny_name)
        elif command.startswith('Detonate'):
            # detonates a bunny
            bunny_name = args[1]
            wars.detonate(bunny_name)
        elif command.startswith('ListBunniesByTeam'):
            # lists the bunnies from the given team
            team_id = int(args[1])
            print('\n'.join([str(bun) for bun in wars.list_bunnies_by_team(team_id)]))
        elif command.startswith('ListBunniesBySuffix'):
            # lists the bunnies that end in the given suffix
            suffix = args[1]
            print('\n'.join([str(bun) for bun in wars.list_bunnies_by_suffix(suffix)]))


def main():
    main_loop()


if __name__ == '__main__':
    main()
