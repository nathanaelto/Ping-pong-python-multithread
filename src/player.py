class Player:
    def __init__(self, name, player_queue, player_lock, opponent_queue, opponent_lock,
                 reference_queue, reference_lock):
        self.name = name
        self.player_queue = player_queue
        self.player_lock = player_lock
        self.opponent_queue = opponent_queue
        self.opponent_lock = opponent_lock
        self.reference_queue = reference_queue
        self.reference_lock = reference_lock

    def calculate(self, n):
        if n % 2 == 0:
            return n // 2
        else:
            return 3 * n + 1

    def play(self):
        while True:
            with self.player_lock:
                if self.player_queue:
                    value = self.player_queue.pop(0)
                else:
                    value = None
            if value == "STOP":
                break
            if not value:
                continue
            new_value = self.calculate(value)
            if new_value == 1:
                with self.reference_lock:
                    self.reference_queue.append({
                        "name": self.name,
                        "value": "WIN"
                    })
            else:
                with self.opponent_lock:
                    self.opponent_queue.append(new_value)
        print("Player {} finished".format(self.name))