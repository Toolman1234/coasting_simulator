import threading
import time


class Combat_Model:
    def __init__(self, dmg, dmg_reduction, hps, hitpoint, attack_speed, name):
        self.dmg = dmg
        self.dmg_reduction = dmg_reduction
        self.hps = hps
        self.cur_hp = hitpoint
        self.attack_speed = attack_speed
        self.name = name
        self.max_hp = hitpoint

    def isAlive(self):
        return self.cur_hp > 0

    def isHealth(self):
        return self.cur_hp == self.max_hp


def attack(attacker, defender):
    while attacker.isAlive() and defender.isAlive():
        final_dmg = attacker.dmg * (1 - defender.dmg_reduction)
        print("{} attacked {} and dealt {} dmg".format(attacker.name, defender.name, final_dmg))
        defender.cur_hp -= final_dmg
        print("{} HP: {}".format(defender.name, defender.cur_hp))
        time.sleep(attacker.attack_speed)
    print("Done Fighting!")


def heal(char):
    while char.isAlive():
        char.cur_hp += char.hps
        if char.cur_hp > char.max_hp:
            char.cur_hp = char.max_hp
        print("{} heal self: {} to {}".format(char.name, char.hps, char.cur_hp))
        time.sleep(1)
    print("dead")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dummy_attacker = Combat_Model(100, 0.08, 10, 1000, 5, "Dummy_attacker")
    dummy_defender = Combat_Model(10000, 0.08, 10, 1000, 5, "Dummy_defender")

    threads = list()

    sim_attack = threading.Thread(target=attack, args=(dummy_attacker, dummy_defender))
    sim_heal = threading.Thread(target=heal, args=(dummy_defender,), daemon=True)
    threads.append(sim_attack)
    threads.append(sim_heal)

    sim_attack.start()
    sim_heal.start()

    for thread in threads:
        thread.join()
