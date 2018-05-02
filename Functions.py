
def choose_gun(Kind, Caliber, Company, Features):
    gun = {
        'Kind':Kind,
        'Caliber':Caliber,
        'Company':Company,
        'Features':Features,
        }
    return gun

Ar = choose_gun('Assult Rifle', '.223/.556 NATO', 'F&N', 'Muzzle Brake, Fluted Rail, Red Dot/Green Dot')
Pistol = choose_gun('Pistol', '.45', 'Glock', 'Reflex')

def display_gun(gun):
    for key, value in gun.items():
        print(key + ": " + value)
    print("\n")

display_gun(Ar)
display_gun(Pistol)
