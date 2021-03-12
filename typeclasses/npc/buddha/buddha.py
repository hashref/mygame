# /mygame/typeclasses/npc/buddha/buddha.py

from evennia import CmdSet, default_cmds
from typeclasses.objects import Object

DefaultMeditationMessages = [
    "You sit down and begin to meditate with the %s.",
    "You continue meditating with the %s.",
    "You have achieved enlightenment!",
]


class CmdMeditate(default_cmds.MuxCommand):

    key = "meditate"
    locks = "cmd:all()"
    auto_help = False

    category = "buddha"
    state_key = "meditation.state"

    def __parse_message(self, message):
        if "%s" in message:
            return message % (self.obj.key)

        return message

    def func(self):
        if self.caller.tags.get("enlightened with the %s" % self.obj.key, category="achievement"):
            self.caller.msg("This buddha has nothing left to teach you.")

        else:
            meditation_messages = self.obj.db.meditation_messages or DefaultMeditationMessages

            if self.caller.attributes.has(self.state_key, category=self.category):
                current_meditation_state = self.caller.attributes.get(self.state_key, category=self.category)

                if current_meditation_state >= len(meditation_messages) - 1:
                    self.caller.attributes.remove(self.state_key, category=self.category)
                    self.caller.tags.add("enlightened with the %s" % self.obj.key, category="achievement")
                    self.caller.msg(self.__parse_message(meditation_messages[-1]))

                else:
                    new_meditation_state = current_meditation_state + 1

                    self.caller.attributes.add(self.state_key, new_meditation_state, category=self.category)
                    self.caller.msg(self.__parse_message(meditation_messages[current_meditation_state]))

            else:
                self.caller.attributes.add(
                    self.state_key,
                    1,
                    category=self.category,
                    lockstring="attread:perm('Admins');attredit('Admins')",
                )
                self.caller.msg(self.__parse_message(meditation_messages[0]))


class BuddhaCmdSet(CmdSet):

    key = "buddhacmdset"

    def at_cmdset_creation(self):
        self.add(CmdMeditate())


class Buddha(Object):
    def at_object_creation(self):
        self.db.desc = "A Buddha statue sitting in the lotus position"
        self.db.meditation_messages = DefaultMeditationMessages
        self.cmdset.add_default(BuddhaCmdSet, permanent=True)