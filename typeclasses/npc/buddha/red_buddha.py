# /mygame/typeclasses/npc/buddha/red_buddha.py

from typeclasses.npc.buddha.buddha import Buddha


class RedBuddha(Buddha):
    def at_object_creation(self):
        super().at_object_creation()
        self.db.desc = "A Red Buddha statue sitting in the lotus position"