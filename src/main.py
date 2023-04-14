from threading import Lock, Thread

from src.player import Player
from src.referee import Referee

if __name__ == '__main__':
    p1_queue = []
    p1_lock = Lock()

    p2_queue = []
    p2_lock = Lock()

    referee_queue = []
    referee_lock = Lock()

    p1 = Player("Player 1", p1_queue, p1_lock, p2_queue, p2_lock, referee_queue, referee_lock)
    p2 = Player("Player 2", p2_queue, p2_lock, p1_queue, p1_lock, referee_queue, referee_lock)
    referee = Referee(referee_queue, referee_lock, p1_queue, p1_lock, p2_queue, p2_lock)

    threads = [
        Thread(target=referee.referee),
        Thread(target=p1.play),
        Thread(target=p2.play),
    ]

    for t in threads:
        t.start()
    for t in threads:
        t.join()