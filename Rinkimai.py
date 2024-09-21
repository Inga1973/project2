import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#  NUBRAIŽOM  GRAFIKĄ

x = np.linspace(0, 100, 500) 

y = np.linspace(0, 100, 500)  

X, Y = np.meshgrid(x, y)

# Slenkstis, nuo kurio kandidatas laimi
Z = Y - (50 + (100 - X)/2)


plt.figure(figsize=(10, 8))
contour = plt.contourf(X, Y, Z, levels=[-100, 0, 100], colors=['green', 'white', 'blue'])


plt.axhline(50, color='grey', linestyle='--')
plt.axvline(50, color='grey', linestyle='--')


plt.xlabel('Dalyvavusių rinkėjų (%)')
plt.ylabel('Iš jų balsavo už kandidatą (%)')
plt.title('Seimo rinkimai (vienmandatė apygarda, 1-as turas)') 
plt.text(60, 60, 'laimėjo', color='white', fontsize=14, ha='center')

plt.grid(True)
plt.show()


# Pirma užduotis
#  Sąlygos, kurios yra būtinos, kad kandidatas į LT Respublikos prezidentus būtų išrinktas 1-mame rinkimų ture.

# 1.Išrinktu laikomas tas kandidatas į Respublikos Prezidento vietą, kuris pirmą kartą balsuojant ir dalyvaujant ne mažiau kaip pusei visų rinkėjų,
# gavo daugiau kaip pusę visų rinkimuose dalyvavusių rinkėjų balsų. 
# 2.Jeigu rinkimuose dalyvavo mažiau kaip pusė visų rinkėjų, išrinktu laikomas tas kandidatas, kuris gavo daugiausia, bet ne mažiau kaip 1/3 visų rinkėjų balsų.
# 3.Jeigu pirmajame balsavimo rate nė vienas kandidatas nesurenka reikiamos balsų daugumos, po dviejų savaičių rengiamas pakartotinis balsavimas dėl dviejų kandidatų, gavusių daugiausia balsų. Išrinktu laikomas kandidatas, surinkęs daugiau balsų.
# Jeigu pirmajame rate dalyvavo ne daugiau kaip du kandidatai ir nė vienas negavo reikiamo balsų skaičiaus, rengiami pakartotiniai rinkimai.

def president_election_outcome(total_voters, voters_participated, candidates_votes):
    participation_rate = voters_participated / total_voters * 100
    elected_candidate = None
    
    if participation_rate >= 50:
    
        for candidate, votes in candidates_votes.items():
            if votes / voters_participated * 100 > 50:
                elected_candidate = candidate
                break
    else:
   
        for candidate, votes in candidates_votes.items():
            if votes >= (total_voters / 3):
                elected_candidate = candidate
                break
    
    if elected_candidate:
        return True, f"{elected_candidate} yra išrinktas prezidentu pirmajame ture."
    else:
  
        top_two_candidates = sorted(candidates_votes.items(), key=lambda item: item[1], reverse=True)[:2]
        return False, f"Nė vienas kandidatas nėra išrinktas. Rengiamas pakartotiniai rinkimai dėl dviejų kandidatų, gavusių daugiausia balsų: {top_two_candidates[0][0]} ir {top_two_candidates[1][0]}."


total_voters = 1000000  # Visi registruoti rinkėjai
voters_participated = 600000  # Dalyvavę rinkėjai

# Rinkėjų balsai
candidates_votes = {
    "Kandidatas 1": 350000,
    "Kandidatas 2": 150000,
    "Kandidatas 3": 100000,
    "Kandidatas 4": 30000,
    "Kandidatas 5": 20000
}

result, message = president_election_outcome(total_voters, voters_participated, candidates_votes)

print(message)



# Antra užduotis
# Sąlygos, kurios yra būtinos, kad kandidatas į mero postą būtų išrinktas pirmajame rinkimų ture.
# 1.Pirmajame ture kandidatas išrenkamas, jei surenka daugiau nei pusę balsų ir rinkimuose dalyvauja daugiau 40 proc. rinkėjų. 
# 2.Jei rinkimuose dalyvauja mažiau nei 40 proc. rinkėjų, kandidatas turi surinkti bent 20 proc. visų rinkėjų balsų. 
# 3.Jei pirmame ture nei vienas kandidatas nesurenka reikiamo kiekio balsų, antrame ture rinkėjai renkasi iš dviejų, 
# daugiausia balsų pirmajame ture surinkusių kandidatų.

def mayor_election_outcome(total_voters, voters_participated, candidates_votes):
    participation_rate = voters_participated / total_voters * 100
    elected_candidate = None
    
    if participation_rate >= 40:
    
        for candidate, votes in candidates_votes.items():
            if votes / voters_participated * 100 > 50:
                elected_candidate = candidate
                break
    else:
        
        for candidate, votes in candidates_votes.items():
            if votes >= (total_voters / 5):
                elected_candidate = candidate
                break
    
    if elected_candidate:
        return True, f"{elected_candidate} yra išrinktas meru pirmajame ture."
    else:
  
        top_two_candidates = sorted(candidates_votes.items(), key=lambda item: item[1], reverse=True)[:2]
        return False, f"Nė vienas kandidatas nėra išrinktas. Rengiamas pakartotiniai rinkimai dėl dviejų kandidatų, gavusių daugiausia balsų: {top_two_candidates[0][0]} ir {top_two_candidates[1][0]}."


total_voters = 100000  # Visi registruoti rinkėjai
voters_participated = 60000  # Dalyvavę rinkėjai

# Rinkėjų balsai
candidates_votes = {
    "Kandidatas 1": 35000,
    "Kandidatas 2": 15000,
    "Kandidatas 3": 10000,
    "Kandidatas 4": 3000,
    "Kandidatas 5": 2000
}

result, message = mayor_election_outcome(total_voters, voters_participated, candidates_votes)

print(message)




# Trečia užduotis
# Sąlygos, kurios yra būtinos, kandidatas į Seimo nario postą būtų išrinktas vienmandatėje apygardoje pirmajame rinkimų ture.

# 1. Vienmandatėse rinkimų apygardose rinkimai laikomi įvykusiais, jei rinkimuose dalyvauja daugiau kaip 40 procentų rinkėjų, 
# įrašytų į tos rinkimų apygardos rinkėjų sąrašus.
# 2. Išrinktu laikomas kandidatas, už kurį rinkimuose balsavo daugiau kaip pusė rinkimuose dalyvavusių rinkėjų.
# 3. Jeigu rinkimų apygardoje balotiravosi daugiau kaip du kandidatai ir nė vienas iš jų nebuvo išrinktas Seimo nariu, 
# Vyriausioji rinkimų komisija, laikydamasi šio įstatymo reikalavimų, ne vėliau kaip per dvi savaites nuo rinkimų rezultatų paskelbimo rengia pakartotinį balsavimą, 
# kuriame dalyvauja du kandidatai, pirmajame balsavime gavę daugiausia balsų. Po pakartotinio balsavimo išrinktu laikomas tas kandidatas, už kurį balsavo daugiau rinkėjų. Jeigu abu kandidatai gavo vienodą balsų skaičių, Seimo nariu tampa tas kandidatas, už kurį pirmajame rinkimų ture balsavo daugiau rinkėjų. Jeigu ir pirmajame rinkimų ture abu kandidatai buvo gavę vienodą balsų skaičių, Seimo nariu tampa vyresnio amžiaus kandidatas.
# 4. Jeigu rinkimų apygardoje balotiravosi ne daugiau kaip du kandidatai ir nė vienas iš jų nebuvo išrinktas, rengiami pakartotiniai rinkimai.

def parlament_election_outcom(total_voters, voters_participated, candidates_votes):
    participation_rate = voters_participated / total_voters * 100
    elected_candidate = None
    
    if participation_rate >= 40:
       
        for candidate, votes in candidates_votes.items():
            if votes / voters_participated * 100 > 50:
                elected_candidate = candidate
                break
  
    
    if elected_candidate:
        return True, f"{elected_candidate} yra išrinktas Seimo nariu pirmajame ture."
    else:
  
        top_two_candidates = sorted(candidates_votes.items(), key=lambda item: item[1], reverse=True)[:2]
        return False, f"Nė vienas kandidatas nėra išrinktas. Rengiamas pakartotiniai rinkimai dėl dviejų kandidatų, gavusių daugiausia balsų: {top_two_candidates[0][0]} ir {top_two_candidates[1][0]}."


total_voters = 110000  # # Visi registruoti rinkėjai
voters_participated = 70000  # Dalyvavę rinkėjai

# Rinkėjų balsai
candidates_votes = {
    "Kandidatas 1": 24000,
    "Kandidatas 2": 15000,
    "Kandidatas 3": 12000,
    "Kandidatas 4": 7000,
    "Kandidatas 5": 5000
}

result, message = parlament_election_outcom(total_voters, voters_participated, candidates_votes)

print(message)



# Ketvirta užduotis
# Sąlygos, kurios yra būtinos, kad konsultaciniame referendume būtų sėkmingai pritarta referendumui pateikto sprendimo priėmimui.

# 1.Konsultacinis (patariamasis) referendumas laikomas įvykusiu, jeigu jame dalyvavo daugiau kaip pusė piliečių, turinčių rinkimų teisę ir įrašytų į rinkėjų sąrašą.
# 2.Tuo atveju, kai konsultaciniame (patariamajame) referendume dalyvavo daugiau kaip pusė piliečių ir šiam referendumui pateikto sprendimo priėmimui pritarė 
# ne mažiau kaip pusė jame dalyvavusių piliečių, sprendimas yra laikomas priimtu.


    

def REFERENDUM_DECISION(total_registered_voters, total_votes, votes_for_decision):

    participation_rate = total_votes / total_registered_voters * 100
   
    decision_support_percentage = votes_for_decision / total_votes * 100
    
    if participation_rate >= 50 and decision_support_percentage >= 50:
        return True
    else:
        return False
    
total_registered_voters = 1000000   # Visi registruoti rinkėjai
total_votes = 600000  # Dalyvavę rinkėjai
votes_for_decision = 310000 # Pritarančių referendumui

result = REFERENDUM_DECISION(total_registered_voters, total_votes, votes_for_decision)

if result:
    print('Pritarta konsultaciniam referendumui')
else:
    print('Nepritarta konsultaciniam referendumui') 

# Penkta užduotis
# Sąlygos, kurios yra būtinos, kad privalomajame referendume būtų sėkmingai pritarta referendumui pateikto sprendimo priėmimui.

# 1.Privalomasis referendumas laikomas įvykusiu, jeigu jame dalyvavo daugiau kaip pusė piliečių, turinčių rinkimų teisę ir įrašytų į rinkėjų sąrašą.
# 2.Sprendimas  yra laikomas priimtu, jeigu tam pritarė daugiau kaip pusė piliečių, dalyvavusių referendume, bet ne mažiau kaip 1/3 piliečių, 
# turinčių rinkimų teisę ir įrašytų į rinkėjų sąrašą.

def mandatory_referdum(total_registered_voters, total_votes, votes_for_decision):

    participation_rate = total_votes / total_registered_voters * 100
    

    decision_support_percentage = votes_for_decision / total_votes * 100

    if participation_rate >= 50 and decision_support_percentage >= 50 and votes_for_decision > total_registered_voters / 3:
        return True
    else:
        return False

total_registered_voters = 900000    # Visi registruoti rinkėjai
total_votes = 700000  # Dalyvavę rinkėjai
votes_for_decision = 590000 # Pritariančių referendumui balsai

result = mandatory_referdum(total_registered_voters, total_votes, votes_for_decision)

if result:
    print('Pritarta privalomo referendumo pasiūlymui')
else:
    print('Nepritarta privalomo referendumo pasiūlymui')


# Šešta užduotis
# Sąlygos, kurios yra būtinos, privalomajame referendume būtų sėkmingai pritarta dėl Konstitucijos XIV skirsnio nuostatų pakeitimo.

# 1. Sprendimas dėl Konstitucijos I skirsnio „Lietuvos valstybė“ ir XIV skirsnio „Konstitucijos keitimas“ nuostatų pakeitimo yra laikomas priimtu, 
# jeigu tam pritarė daugiau kaip pusė piliečių, turinčių rinkimų teisę ir įrašytų į rinkėjų sąrašą.
# 2.Privalomasis referendumas laikomas įvykusiu, jeigu jame dalyvavo daugiau kaip pusė piliečių, turinčių rinkimų teisę ir įrašytų į rinkėjų sąrašą.

def is_mandatory_referendum_succeeded_1(total_registered_voters, total_votes, votes_for_decision):


    participation_rate = total_votes / total_registered_voters * 100

    decision_support_percentage = votes_for_decision / total_registered_voters * 100
    
  

    if participation_rate >= 50 and decision_support_percentage >= 50:
        return True
    else:
        return False


total_registered_voters = 1000000   # Visi registruoti rinkėjai
total_votes = 850000  # Dalyvavę rinkėjai
votes_for_decision = 750000  # Pritarė referendumui

result = is_mandatory_referendum_succeeded_1(total_registered_voters, total_votes, votes_for_decision)

if result:
    print('Pritarta privalomo referendumo pasiūlymui dėl Konstitucijos XIV skirsnio nuostatų pakeitimo')
else:
    print('Nepritarta privalomo referendumo pasiūlymui dėl Konstitucijos XIV skirsnio nuostatų pakeitimo')


# Septinta užduotis
# Sąlygos, kurios yra būtinos, privalomajame referendume būtų sėkmingai pritarta dėl Konstitucijos 1 straipsnio nuostatos pakeitimo.

# 1.Sprendimas dėl Konstitucijos 1 straipsnio nuostatos „Lietuvos valstybė yra nepriklausoma demokratinė respublika“, 
# taip pat dėl 1992 m. birželio 8 d. Konstitucinio akto „Dėl Lietuvos Respublikos nesijungimo į postsovietines Rytų sąjungas“ pakeitimo yra laikomas priimtu, 
# jeigu tam pritarė ne mažiau kaip 3/4 piliečių, turinčių rinkimų teisę ir įrašytų į rinkėjų sąrašą
# 2.Privalomasis referendumas laikomas įvykusiu, jeigu jame dalyvavo daugiau kaip pusė piliečių, turinčių rinkimų teisę ir įrašytų į rinkėjų sąrašą.

def is_mandatory_referendum_succeeded_2(total_registered_voters, total_votes, votes_for_decision):


    participation_rate = total_votes / total_registered_voters * 100
    
   

    if participation_rate >=50 and votes_for_decision >= total_registered_voters * 3 / 4:
        return True
    else:
        return False


total_registered_voters = 1000000   # Visi registruoti rinkėjai
total_votes = 850000  # Dalyvavę rinkėjai
votes_for_decision = 760000  # Pritarė referendumui

result = is_mandatory_referendum_succeeded_2(total_registered_voters, total_votes, votes_for_decision)

if result:
    print('Pritarta privalomo referendumo pasiūlymui dėl Konstitucijos 1 straipsnio nuostatos pakeitimo')
else:
    print('Nepritarta privalomo referendumo pasiūlymui ddėl Konstitucijos 1 straipsnio nuostatos pakeitimo')
