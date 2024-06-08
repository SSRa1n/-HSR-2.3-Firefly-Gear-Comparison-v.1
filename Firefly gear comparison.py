import math

level = 80 #Firefly's Level
toughness = 90 #Enhanced Skill's toughness damage
toughness_blast = 45 #Blast's toughness damage

break_in_enhanced = 2 #Total weakness break in enhanced skill
actions_in_enhanced = 4 #Actions in enhanced skill

enemies_level = 95 #Enemy's level
enemies = 1
enemies_res = 0
enemies_broken = True

ruanmei_eidolon_cap = 1
firefly_eidolon_cap = 2
whereabouts_superimpose_cap = 1

htb_break_effect = 200.0

lc_atk_base = 529.2
lc_be = 0.0
lc_atk_bonus = 0.64
lc_vulnerability = 0.0

relic_atk_flat = 352.0 + (19.05 * 5)
## Hands + 5x 1 mid rolls atk substat
relic_atk_bonus = 0.432 + 0.432 + (0.0389 * 2 * 4)
## Body + Sphere + 4x 2 mid-rolls atk% substat
relic_be_bonus = 64.8 + 16.0 + 40.0 + (5.83 * 2 * 5)
## Rope + 2pc Iron Cavalry + 2pc Kalpagni Lantern + 5x 2 mid-rolls BE substat ##
relic_def_ignore = 0.1 + 0.15
## 4pc Iron Cavalry

buff_atk_flat = 0.0
buff_atk_bonus = 0.0
buff_be_bonus = 0.0
buff_vulnerability = 0.0

results = []

class RuanMei:
  def __init__(self, eidolon=0, res_pen=0.25, def_ignore=0.0, break_efficiency=0.5, break_effect=20.0, atk=0.0, enemies_broken=False):
    self.__eidolon = eidolon
    self.__res_pen = res_pen
    self.__def_ignore = def_ignore
    self.__break_efficiency = break_efficiency
    self.__break_effect = break_effect
    self.__atk = atk
    self.__enemies_broken = enemies_broken

  def enemies_broken(self):
    self.__enemies_broken = True
    
  @property
  def eidolon(self):
    return self.__eidolon
  @eidolon.setter
  def eidolon(self, eidolon):
    self.__eidolon = eidolon
    if eidolon >= 1:
      self.__def_ignore = 0.2
    if eidolon >= 3:
      self.__res_pen = 0.27

  def res_pen(self):
    return self.__res_pen
  def def_ignore(self):
    return self.__def_ignore
  def break_efficiency(self):
    return self.__break_efficiency
  def break_effect(self):
    return self.__break_effect
  def atk(self):
    return self.__atk
    
class Firefly():
  def __init__(self, eidolon=0, res_pen=0.0, def_ignore=0.0, break_efficiency=0.5, break_effect=37.3, atk_base=523.91, vulnerability=0.2):
    self.__eidolon = eidolon
    self.__res_pen = res_pen
    self.__def_ignore = def_ignore
    self.__break_efficiency = break_efficiency
    self.__break_effect = break_effect
    self.__atk_base = atk_base
    self.__vulnerabity = vulnerability

  @property
  def eidolon(self):
    return self.__eidolon
  @eidolon.setter
  def eidolon(self, eidolon):
    self.__eidolon = eidolon
    if eidolon >= 1:
      self.__def_ignore = 0.15
    if eidolon >= 5:
      self.__vulnerabity = 0.22
    if eidolon >= 6:
      self.__res_pen = 0.2
      self.__break_efficiency = 0.5

  def res_pen(self):
    return self.__res_pen
  def def_ignore(self):
    return self.__def_ignore
  def break_efficiency(self):
    return self.__break_efficiency
  def break_effect(self):
    return self.__break_effect
  def atk_base(self):
    return self.__atk_base
  def vulnerability(self):
    return self.__vulnerabity
    
class Whereabouts():
  def __init__(self, superimpose=1, atk_base=476.28, break_effect=60.0, atk_bonus=0.0, vulnerability=0.24):
    self.__superimpose = superimpose
    self.__atk_base = atk_base
    self.__break_effect = break_effect
    self.__atk_bonus = atk_bonus
    self.__vulnerability = vulnerability

  @property
  def superimpose(self):
    return self.__superimpose
  @superimpose.setter
  def superimpose(self, superimpose):
    self.__superimpose = superimpose
    if self.__superimpose > 0:
      self.__break_effect = 60+(10*(superimpose-1))
      self.__vulnerability = 0.24+(0.04*(superimpose-1))
  
  def atk_base(self):
    return self.__atk_base
  def break_effect(self):
    return self.__break_effect
  def atk_bonus(self):
    return self.__atk_bonus
  def vulnerability(self):
    return self.__vulnerability

for i in range(0, ruanmei_eidolon_cap + 2):
  ruanmei = RuanMei()
  if enemies_broken:
    ruanmei.enemies_broken()
  ruanmei.eidolon = i
  if ruanmei.eidolon == ruanmei_eidolon_cap + 1:
    ruanmei = RuanMei(404, 0.0, 0.0, 0, 0, 0.0, False)
  #### Ruan Mei Test ####
  # print(ruanmei.eidolon)
  # print(ruanmei.res_pen())
  # print(ruanmei.def_ignore())
  # print(ruanmei.break_efficiency())
  # print(ruanmei.break_effect())
  # print(ruanmei.atk())
  # print('--------------------')
  #### Ruan Mei Test ####
  for j in range(0, firefly_eidolon_cap + 1):
    firefly = Firefly()
    firefly.eidolon = j
    #### Firefly Test ####
    # print(firefly.eidolon)
    # print(firefly.res_pen())
    # print(firefly.def_ignore())
    # print(firefly.break_efficiency())
    # print(firefly.vulnerability())
    # print('--------------------')
    #### Firefly Test ####
    for k in range(1, whereabouts_superimpose_cap + 2):
      whereabouts = Whereabouts()
      whereabouts.superimpose = k
      if whereabouts.superimpose == whereabouts_superimpose_cap + 1:
        whereabouts = Whereabouts(0, lc_atk_base, lc_be, lc_atk_bonus, lc_vulnerability)
      #### Whereabouts Test ####
      # print(whereabouts.superimpose)
      # print(whereabouts.atk_base())
      # print(whereabouts.break_effect())
      # print(whereabouts.atk_bonus())
      # print(whereabouts.vulnerability())
      # print('--------------------')
      #### Whereabouts Test ####
      total_atk = (firefly.atk_base() + whereabouts.atk_base()) * (1 + (relic_atk_bonus + whereabouts.atk_bonus() + buff_atk_bonus)) + relic_atk_flat + buff_atk_flat
      
      atk_be_conversion = 0.0
      if(total_atk > 1800):
        atk_be_conversion = math.floor((total_atk - 1800)/10) * 0.8

      htb_be_buff = 33.0 + 30 + ((33.0 + 30 + htb_break_effect + ruanmei.break_effect()) * 0.15)
      ## Ult + Watchmaker + E4 ##
      
      total_break_effect = firefly.break_effect() + whereabouts.break_effect() + atk_be_conversion + relic_be_bonus + buff_be_bonus + htb_be_buff

      total_def_ignore = relic_def_ignore + ruanmei.def_ignore() + firefly.def_ignore()

      total_toughness = toughness * (1 + (ruanmei.break_efficiency() +  firefly.break_efficiency()))
      total_blast_toughness = toughness_blast * (1 + (ruanmei.break_efficiency() +  firefly.break_efficiency()))

      total_res_pen = ruanmei.res_pen() + firefly.res_pen()

      total_vulnerability = buff_vulnerability + firefly.vulnerability() + whereabouts.vulnerability()
      
      super_break_dmg = round(3767.5533 * ((level+20)/((enemies_level+20)*(1-total_def_ignore)+(level+20))) * (total_toughness/30) * (1+(total_break_effect/100)) * (1+(0.6 - ((enemies - 1) * 0.1))) * (1-(enemies_res - total_res_pen)) * (1 + total_vulnerability),2)
      super_break_dmg_blast = round(3767.5533 * ((level+20)/((enemies_level+20)*(1-total_def_ignore)+(level+20))) * (total_blast_toughness/30) * (1+(total_break_effect/100)) * (1+(0.6 - ((enemies - 1) * 0.1))) * (1-(enemies_res - total_res_pen)) * (1 + total_vulnerability),2)
      
      if enemies == 2:
        super_break_dmg = super_break_dmg + super_break_dmg_blast
      if enemies > 2:
        super_break_dmg = super_break_dmg + (super_break_dmg_blast * 2)
      if firefly.eidolon >= 2:
        super_break_dmg = round(super_break_dmg * (1 + (break_in_enhanced/actions_in_enhanced)),2)

      result = [firefly.eidolon, ruanmei.eidolon, whereabouts.superimpose, super_break_dmg]
      results.append(result)
sorted_results = sorted(results, key=lambda x: x[3], reverse=True)

for l in sorted_results:
  firefly_eidolon = 'E' + str(l[0]) + ' Firefly'
  ruanmei_eidolon = 'no Ruan Mei' if l[1] == 404 else 'E' + str(l[1]) + ' Ruan Mei'
  whereabouts_superimpose = 'S5 AeonFall' if l[2] == 0 else 'S' + str(l[2]) + ' Whereabouts'
  superbreak_dmg = str(l[3]) + ' DMG'
  print(f'{firefly_eidolon} | {ruanmei_eidolon} | {whereabouts_superimpose} | {superbreak_dmg}')
# for l in sorted_results:
#   print('E' + str(l[0]) + ' Firefly' + ' | E' + str(l[1]) + ' Ruan Mei' + ' | S' + str(l[2]) + ' Whereabouts' + ' | ' + str(l[3]) + ' DMG')