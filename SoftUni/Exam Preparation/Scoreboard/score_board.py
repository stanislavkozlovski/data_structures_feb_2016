from sortedcontainers import SortedDict
from trie import Trie
# Python 2

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __hash__(self):
        return hash(self.username)

    def __eq__(self, other):
        return self.username == other.username


class Scoreboard:
    def __init__(self):
        # dictionary, key: username, value: bool (doesnt matter)
        self.scores = {}
        # Sorted dictionary, key: score, value: [username]
        self.ordered_scores = SortedDict()

    def __len__(self):
        return len(self.ordered_scores)

    def add_score(self, username, score):
        self.scores[username] = True
        if score not in self.ordered_scores:
            self.ordered_scores[score] = []
        self.ordered_scores[score].append(username)

    def show(self):
        """ Shows the top 10 highest scores """
        to_break = False
        count_left = 10
        keys = self.ordered_scores.keys()
        start = len(keys) - 10
        scores = []
        for i in reversed(range(start, len(keys))):
            if i < 0:
                break
            key = keys[i]
            sorted_scored = sorted(self.ordered_scores[key])
            for score in sorted_scored:
                count_left -= 1
                scores.append("#{num} {name} {score}".format(
                    num=10-count_left, name=score, score=key
                ))
                if count_left == 0:
                    to_break = True
                    break

            if to_break:
                break

        return unicode('\n'.join(scores))


class Game:
    def __init__(self, game_name, game_password):
        self.name = game_name
        self.password = game_password
        self.scoreboard = Scoreboard()

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def add_score(self, username, score):
        self.scoreboard.add_score(username, score)

    def show_scoreboard(self):
       return self.scoreboard.show()


class System:
    def __init__(self):
        self.games = Trie()
        self.users = {}

    def main_loop(self):
        command = raw_input()
        while not command.startswith('End'):
            output = self.command_controller(command)
            print(output)
            command = raw_input()

    def command_controller(self, command):
        if command.startswith('RegisterUser'):
            username, password = command.split()[1:]
            return self.register_user(username, password)
        elif command.startswith('RegisterGame'):
            name, password = command.split()[1:]
            return self.register_game(name, password)
        elif command.startswith('AddScore'):
            username, user_pass, game_name, game_pass, score = command.split()[1:]
            score = int(score)
            return self.add_score(username, user_pass, game_name, game_pass, score)
        elif command.startswith('ShowScoreboard'):
            game_name = command.split()[1]
            return self.show_scoreboard(game_name)
        elif command.startswith('ListGamesByPrefix'):
            prefix = command.split()[1]
            return self.list_games_by_prefix(prefix)
        elif command.startswith('DeleteGame'):
            game_name, game_pass = command.split()[1:]
            return self.delete_game(game_name, game_pass)

    def register_user(self, username, password):
        if username in self.users:
            return unicode('Duplicated user')
        self.users[username] = User(username, password)
        return "User registered"

    def register_game(self, game_name, game_password):
        if self.games.has_key(game_name):
            return unicode('Duplicated game')
        self.games[game_name] = Game(game_name, game_password)
        return unicode('Game registered')

    def add_score(self, username, user_pass, game_name, game_pass, score):
        if username not in self.users or user_pass != self.users[username].password\
                or not self.games.has_key(game_name) or self.games.get(game_name).password != game_pass:
            return unicode('Cannot add score')
        game = self.games.get(game_name)
        game.add_score(username, score)
        return unicode('Score added')

    def show_scoreboard(self, game):
        if not self.games.has_key(game):
            return unicode('Game not found')
        game = self.games.get(game)
        if len(game.scoreboard) == 0:
            return unicode('No score')
        return game.show_scoreboard()

    def list_games_by_prefix(self, prefix):
        try:
            keys = sorted(self.games.keys(prefix=prefix))[:10]
        except:
            keys = None

        if not keys:
            return unicode('No matches')
        else:
            return unicode(', '.join([''.join(key) for key in sorted(keys)]))

    def delete_game(self, game_name, game_password):
        if not self.games.has_key(game_name) or self.games[game_name].password != game_password:
            return unicode('Cannot delete game')

        self.games.pop(game_name)
        return unicode('Game deleted')

