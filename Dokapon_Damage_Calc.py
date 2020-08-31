print()
print("Dokapon Damage Calculator")
print("by Benjamin Wilson (subzero258)")
while True:
    aTp = "py"
    print()
    while aTp != "attack" and aTp != "magic" and aTp != "strike" and aTp != "full" and aTp != "field magic" and aTp != "done":
        print("In the selection below, type \"strike\", \"attack\", or \"magic\" for a damage calculation.")
        print("Type \"full\" for strike, attack, and magic calculations.")
        print("Type \"field magic\" for field magic damage calculations.")
        print("Type \"done\" to finish.")
        print()
        print("Press enter to confirm your selection")
        print("All inputs must be in lowercase")
        aTp = input("Selection: ")
        if aTp != "attack" and aTp != "magic" and aTp != "strike" and aTp != "full" and aTp != "field magic" and aTp != "done":
            print()
            print("Invalid selection")
            print()
    if aTp == "done":
        exit
    if aTp == "attack" or aTp == "full":
        atk = float(input("Your attack: "))
        proficiency = input("Do you have a proficiency: ")
        if proficiency == "yes":
            proficiency = 1.3
        else:
            proficiency = 1.0
        dfn = float(input("Their defense: "))
        baseDamage = (atk * 5.6 - dfn * 2.4)
        defendDamage = (baseDamage * 0.5)
        magicDefendDamage = (baseDamage * 0.7)
        counterDamage = (baseDamage * 0.9)
        print()
        print("Attack:")
        print("If opponent defends: ", round((defendDamage * 0.95) * proficiency), "damage, or", round((defendDamage * 1.05) * proficiency), "damage")
        print("If opponent magic defends: ", round((magicDefendDamage * 0.95) * proficiency), "damage, or", round((magicDefendDamage * 1.05) * proficiency), "damage")
        print("If opponent counters: ", round((counterDamage * 0.95) * proficiency), "damage, or", round((counterDamage * 1.05) * proficiency), "damage")
        print("If opponent can't react: ", round((baseDamage * 0.95) * proficiency), "damage, or", round((baseDamage * 1.05) * proficiency), "damage")
        print()
    if aTp == "magic" or aTp == "full":
        atk = float(input("Your MG: "))
        dfn = float(input("Their MG: "))
        atkSpell = input("Your offensive spell: ")
        dfnSpell = input("Their defensive spell (if they have no defensive spell, type \"none\"): ")
        atkPower = 0
        while True:
            if atkSpell == "scorch":
                atkPower = 3.9
                break
            elif atkSpell == "scorcher":
                atkPower == 5.3
                break
            elif atkSpell == "giga blaze":
                atkPower = 7.4
                break
            elif atkSpell == "zap":
                atkPower = 4.5
                break
            elif atkSpell == "zapper":
                atkPower = 6.3
                break
            elif atkSpell == "lectro beam":
                atkPower = 8.9
                break
            elif atkSpell == "chill":
                atkPower = 4.2
                break
            elif atkSpell == "chiller":
                atkPower = 5.8
                break
            elif atkSpell == "ice barrage":
                atkPower = 8.2
                break
            elif atkSpell == "gust":
                atkPower = 4.9
                break
            elif atkSpell == "guster":
                atkPower = 6.4
                break
            elif atkSpell == "f5 storm":
                atkPower = 9.5
                break
            elif atkSpell == "mirror image":
                atkPower = 4.8
                break
            elif atkSpell == "teleport":
                atkPower = 6.0
                break
            elif atkSpell == "aurora":
                atkPower = 10.0
                break
            elif atkSpell == "curse":
                atkPower = 3.2
                break
            elif atkSpell == "sleepy":
                atkPower = 2.2
                break
            elif atkSpell == "blind":
                atkPower = 2.8
                break
            elif atkSpell == "banish":
                atkPower = 5.0
                break
            elif atkSpell == "drain":
                atkPower = 0.0
                break
            elif atkSpell == "swap":
                atkPower = 0.0
                break
            elif atkSpell == "pickpocket":
                atkPower = 3.0
                break
            elif atkSpell == "rust":
                atkPower = 7.2
                break
            else:
                print("Invalid spell")
                atkSpell = input("Your offensive spell: ")
        dfnPower = 0
        while True:
            if dfnSpell == "m guard":
                dfnPower = 0.2
                break
            elif dfnSpell == "m guard+":
                dfnPower = 0.6
                break
            elif dfnSpell == "m guard dx":
                dfnPower = 0.9
                break
            elif dfnSpell == "refresh":
                dfnPower = 0.2
                break
            elif dfnSpell == "refresh+":
                dfnPower = 0.35
                break
            elif dfnSpell == "refresh dx":
                dfnPower = 0.5
                break
            elif dfnSpell == "super cure":
                dfnPower = 0.5
                break
            elif dfnSpell == "seal magic":
                dfnPower = 0.3
                break
            elif dfnSpell == "seal magic+":
                dfnPower = 0.5
                break
            elif dfnSpell == "shock":
                dfnPower = 0.6
                break
            elif dfnSpell == "mirror":
                dfnPower = 0.5
                break
            elif dfnSpell == "mg charge":
                dfnPower = 0.35
                break
            elif dfnSpell == "at charge":
                dfnPower = 0.35
                break
            elif dfnSpell == "df charge":
                dfnPower = 0.35
                break
            elif dfnSpell == "sp charge":
                dfnPower = 0.35
                break
            elif dfnSpell == "charge all":
                dfnPower = 0.6
                break
            elif dfnSpell == "charm":
                dfnPower = 0.7
                break
            elif dfnSpell == "bounce":
                dfnPower = 0.0
                break
            elif dfnSpell == "super bounce":
                dfnPower = 0.0
                break
            elif dfnSpell == "none":
                dfnPower = 0.0
                break
            else:
                print("Invalid spell")
                dfnSpell = input("Their defensive spell (if they have no defensive spell, type \"none\".: ")
        baseDamage = (atk * 2.4 - dfn) * atkPower* (1 - dfnPower)
        defendDamage = (baseDamage * 0.7)
        magicDefendDamage = (baseDamage * 0.5)
        counterDamage = (baseDamage * 0.9)
        print()
        print("Magic attack:")
        print("If opponent defends: ", round((defendDamage * 0.95)), "damage, or", round((defendDamage * 1.05)), "damage")
        if atkSpell == "bounce":
            print("If opponent magic defends: They will deal", round((magicDefendDamage * 0.95)), "damage, or", round((magicDefendDamage * 1.05)), "damage to you")
        elif atkSpell == "super bounce":
            print("If opponent magic defends: They will deal", round((magicDefendDamage * 0.95) * 4), "damage, or", round((magicDefendDamage * 1.05) * 4), "damage to you")
        elif atkSpell == "mirror":
            print("If opponent magic defends: You will deal", round((magicDefendDamage * 0.95)), "damage, or", round((magicDefendDamage * 1.05)), "damage to them. and they will deal", round((magicDefendDamage * 0.95) / 2),", or", round((magicDefendDamage * 1.05) / 2),"damage to you")
        else:
            print("If opponent magic defends: ", round((magicDefendDamage * 0.95)), "damage, or", round((magicDefendDamage * 1.05)), "damage")
        print("If opponent counters: ", round((counterDamage * 0.95)), "damage, or", round((counterDamage * 1.05)), "damage")
        print("If opponent can't react: ", round((baseDamage * 0.95)), "damage, or", round((baseDamage * 1.05)), "damage")
        print()
    if aTp == "strike" or aTp == "full":
        atkAtk = float(input("Your attack: "))
        atkDfn = float(input("Your defense: "))
        atkMagic = float(input("Your MG: "))
        atkSpeed = float(input("Your speed: "))
        dfnAtk = float(input("Their attack: "))
        dfnDfn = float(input("Their defense: "))
        dfnMagic = float(input("Their MG: "))
        dfnSpeed = float(input("Their speed: "))
        baseDamage = (atkAtk + atkMagic + atkSpeed) * 6.25 - (dfnDfn + dfnMagic + dfnSpeed) * 2.5
        defendDamage = (baseDamage * 0.64)
        magicDefendDamage = (baseDamage * 0.68)
        counterDamage = (dfnAtk + dfnMagic + dfnSpeed) * 4 + (atkAtk - atkDfn) * 2
        print()
        print("Strike:")
        print("If opponent defends: ", round((defendDamage * 0.95)), "damage, or", round((defendDamage * 1.05)), "damage")
        print("If opponent magic defends: ", round((magicDefendDamage * 0.95)), "damage, or", round((magicDefendDamage * 1.05)), "damage")
        print("If opponent counters: ", round((counterDamage * 0.95)), "damage, or", round((counterDamage * 1.05)), "damage to you")
        print("If opponent can't react: ", round((baseDamage * 0.95)), "damage, or", round((baseDamage * 1.05)), "damage")
        print()
    if aTp == "field magic":
        atkMagic = input("Your MG: ")
        dfnMagic = input("Their MG: ")
        atkSpell = input("Your field magic: ")
        atkPower = 0
        while True:
            if atkSpell == "magma":
                atkPower = 1.5
                break
            elif atkSpell == "magma+":
                atkPower = 2.1
                break
            elif atkSpell == "magma dx":
                atkPower = 4.5
                break
            elif atkSpell == "ice":
                atkPower = 1.2
                break
            elif atkSpell == "ice+":
                atkPower = 1.8
                break
            elif atkSpell == "ice dx":
                atkPower = 3.6
                break
            elif atkSpell == "volt":
                atkPower = 0.96
                break
            elif atkSpell == "volt+":
                atkPower = 1.56
                break
            elif atkSpell == "volt dx":
                atkPower = 3.0
                break
            elif atkSpell == "flash bomb":
                atkPower = 5.0
                break
            else:
                print("Invalid spell")
                atkSpell = input("Your field magic: ")
        baseDamage = (atkMagic * 2 - dfnMagic) * atkPower
        print()
        print("Field magic:")
        print("You will deal: ", floor(baseDamage),", or", floor(baseDamage * 1.1),"damage")
        print()