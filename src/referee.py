import random


class Referee:
    def __init__(self, referee_queue, referee_lock, player_1_queue, player_1_lock, player_2_queue,
                 player_2_lock):
        self.referee_queue = referee_queue
        self.referee_lock = referee_lock
        self.player_1_queue = player_1_queue
        self.player_1_lock = player_1_lock
        self.player_2_queue = player_2_queue
        self.player_2_lock = player_2_lock

    def referee(self):
        with self.player_1_lock, self.player_2_lock:
            if not self.player_1_queue and not self.player_2_queue:
                starting_number = random.randint(1000, 1000000)
                random_player = random.randint(0, 1)
                if random_player == 0:
                    self.player_1_queue.append(starting_number)
                else:
                    self.player_2_queue.append(starting_number)

        while True:
            with self.referee_lock:
                if self.referee_queue:
                    value = self.referee_queue.pop(0)
                else:
                    value = None
            if value:
                with self.player_1_lock, self.player_2_lock:
                    self.player_2_queue.append("STOP")
                    self.player_1_queue.append("STOP")

                print(value)
                break
