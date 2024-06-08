enemies = 1
enemies_broken = True
ruanmei_eidolon_cap = 6
firefly_eidolon_cap = 6
whereabouts_superimpose_cap = 5
lc_atk_base = 529.2
lc_atk_bonus = 0.64
lc_be = 0
relic_atk_bonus = 0.5
relic_be_bonus = 40

class RuanMei:
  def __init__(self, eidolon=0, res_pen=0.25, def_ignore=0.0, break_efficiency=0.5, 
               break_effect=20, atk=0.0, enemies_broken=False):
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
      self.__def_ignore += 0.2
    if eidolon >= 2 and self.__enemies_broken:
      self.__atk += 0.4
    if eidolon >= 3:
      self.__res_pen += 0.02

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
  def __init__(self, eidolon=0, res_pen=0.0, def_ignore=0.0, break_efficiency=0.5, 
               break_effect=37.3, atk_base=523.91):
    self.__eidolon = eidolon
    self.__res_pen = res_pen
    self.__def_ignore = def_ignore
    self.__break_efficiency = break_efficiency
    self.__break_effect = break_effect
    self.__atk_base = atk_base

  @property
  def eidolon(self):
    return self.__eidolon
  @eidolon.setter
  def eidolon(self, eidolon):
    self.__eidolon = eidolon
    if eidolon >= 1:
      self.__def_ignore += 0.15
    if eidolon >= 6:
      self.__res_pen += 0.2
      self.__break_efficiency += 0.5

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
    
class Whereabouts():
  de

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
    print(firefly.eidolon)
    print(firefly.res_pen())
    print(firefly.def_ignore())
    print(firefly.break_efficiency())
    print('--------------------')
    #### Firefly Test ####