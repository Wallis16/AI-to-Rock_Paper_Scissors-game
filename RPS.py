# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import random

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    guess = "R"
    if len(opponent_history) > 2:
        guess = opponent_history[-2]

    return guess

def markov1(prev_play, opponent_history=[], dict_markov1={
              "R": [0,0,0],
              "P": [0,0,0],
              "S": [0,0,0]}):

    opponent_history.append(prev_play)

    dict_aux = {"R":0,"P":1,"S":2}
    dict_resp = {0:"P",1:"S",2:"R"}

    if len(opponent_history) > 2:

        ind = dict_aux[opponent_history[-1]]
        dict_markov1[opponent_history[-2]][ind] += 1

        max_ = max(dict_markov1[opponent_history[-1]])

        index = random.choice([i for i in range(len(dict_markov1[opponent_history[-1]])) if dict_markov1[opponent_history[-1]][i] == max_])

        guess = dict_resp[index]

    else:

      guess = dict_resp[random.randint(0,2)]

    return guess


def markov2(prev_play, opponent_history=[], dict_markov2={
              "RR": [0,0,0],
              "RP": [0,0,0],
              "RS": [0,0,0],
              "PR": [0,0,0],
              "PP": [0,0,0],
              "PS": [0,0,0],
              "SR": [0,0,0],
              "SP": [0,0,0],
              "SS": [0,0,0],
          }):

    opponent_history.append(prev_play)

    dict_aux = {"R":0,"P":1,"S":2}
    dict_resp = {0:"P",1:"S",2:"R"}

    if len(opponent_history) > 3:

        ind = dict_aux[opponent_history[-1]]
        ind_m2 = opponent_history[-3] + opponent_history[-2]
        ind_d2 = opponent_history[-2] + opponent_history[-1]

        dict_markov2[ind_m2][ind] += 1

        max_ = max(dict_markov2[ind_d2])

        index = random.choice([i for i in range(len(dict_markov2[ind_d2])) if dict_markov2[ind_d2][i] == max_])

        guess = dict_resp[index]

    else:

      guess = dict_resp[random.randint(0,2)]

    return guess

def markov3(prev_play, opponent_history=[], dict_markov3={
              "RRR": [0,0,0],
              "RRP": [0,0,0],
              "RRS": [0,0,0],
              "RPR": [0,0,0],
              "RPP": [0,0,0],
              "RPS": [0,0,0],
              "RSP": [0,0,0],
              "RSR": [0,0,0],
              "RSS": [0,0,0],
              "PRR": [0,0,0],
              "PRS": [0,0,0],
              "PRP": [0,0,0],
              "PPR": [0,0,0],
              "PPP": [0,0,0],
              "PPS": [0,0,0],
              "PSR": [0,0,0],
              "PSP": [0,0,0],
              "PSS": [0,0,0],
              "SRR": [0,0,0],
              "SRP": [0,0,0],
              "SRS": [0,0,0],
              "SPR": [0,0,0],
              "SPP": [0,0,0],
              "SPS": [0,0,0],
              "SSR": [0,0,0],
              "SSP": [0,0,0],
              "SSS": [0,0,0],
          }):

    try:

      opponent_history.append(prev_play)

      dict_aux = {"R":0,"P":1,"S":2}
      dict_resp = {0:"P",1:"S",2:"R"}

      if len(opponent_history) > 4:

          ind = dict_aux[opponent_history[-1]]
          ind_m2 = opponent_history[-4] + opponent_history[-3] + opponent_history[-2]
          ind_d2 = opponent_history[-3] + opponent_history[-2] + opponent_history[-1]

          dict_markov3[ind_m2][ind] += 1

          index = dict_markov3[ind_d2].index(max(dict_markov3[ind_d2]))

          guess = dict_resp[index]

      else:

        guess = dict_resp[1]

      return guess

    except:

      opponent_history = []
      dict_markov3 = {"RRR": [0,0,0], "RRP": [0,0,0],
              "RRS": [0,0,0], "RPR": [0,0,0],
              "RPP": [0,0,0], "RPS": [0,0,0],
              "RSP": [0,0,0], "RSR": [0,0,0],
              "RSS": [0,0,0], "PRR": [0,0,0],
              "PRS": [0,0,0], "PRP": [0,0,0],
              "PPR": [0,0,0], "PPP": [0,0,0],
              "PPS": [0,0,0], "PSR": [0,0,0],
              "PSP": [0,0,0], "PSS": [0,0,0],
              "SRR": [0,0,0], "SRP": [0,0,0],
              "SRS": [0,0,0], "SPR": [0,0,0],
              "SPP": [0,0,0], "SPS": [0,0,0],
              "SSR": [0,0,0], "SSP": [0,0,0],
              "SSS": [0,0,0],}

      opponent_history.append(prev_play)

      dict_aux = {"R":0,"P":1,"S":2}
      dict_resp = {0:"P",1:"S",2:"R"}

      if len(opponent_history) > 4:

          ind = dict_aux[opponent_history[-1]]
          ind_m2 = opponent_history[-4] + opponent_history[-3] + opponent_history[-2]
          ind_d2 = opponent_history[-3] + opponent_history[-2] + opponent_history[-1]

          dict_markov3[ind_m2][ind] += 1

          index = dict_markov3[ind_d2].index(max(dict_markov3[ind_d2]))

          guess = dict_resp[index]

      else:

        guess = dict_resp[1]

      return guess

def markov4(prev_play, opponent_history=[], dict_markov4={
              "RRRR": [0,0,0],
              "RRRS": [0,0,0],
              "RRRP": [0,0,0],
              "RRPR": [0,0,0],
              "RRPS": [0,0,0],
              "RRPP": [0,0,0],
              "RRSR": [0,0,0],
              "RRSS": [0,0,0],
              "RRSP": [0,0,0],
              "RPRR": [0,0,0],
              "RPRS": [0,0,0],
              "RPRP": [0,0,0],
              "RPPR": [0,0,0],
              "RPPS": [0,0,0],
              "RPPP": [0,0,0],
              "RPSR": [0,0,0],
              "RPSS": [0,0,0],
              "RPSP": [0,0,0],
              "RSPR": [0,0,0],
              "RSPS": [0,0,0],
              "RSPP": [0,0,0],
              "RSRR": [0,0,0],
              "RSRS": [0,0,0],
              "RSRP": [0,0,0],
              "RSSR": [0,0,0],
              "RSSS": [0,0,0],
              "RSSP": [0,0,0],
              "PRRR": [0,0,0],
              "PRRS": [0,0,0],
              "PRRP": [0,0,0],
              "PRSR": [0,0,0],
              "PRSS": [0,0,0],
              "PRSP": [0,0,0],
              "PRPR": [0,0,0],
              "PRPS": [0,0,0],
              "PRPP": [0,0,0],
              "PPRR": [0,0,0],
              "PPRS": [0,0,0],
              "PPRP": [0,0,0],
              "PPPR": [0,0,0],
              "PPPS": [0,0,0],
              "PPPP": [0,0,0],
              "PPSR": [0,0,0],
              "PPSS": [0,0,0],
              "PPSP": [0,0,0],
              "PSRR": [0,0,0],
              "PSRS": [0,0,0],
              "PSRP": [0,0,0],
              "PSPR": [0,0,0],
              "PSPS": [0,0,0],
              "PSPP": [0,0,0],
              "PSSR": [0,0,0],
              "PSSS": [0,0,0],
              "PSSP": [0,0,0],
              "SRRR": [0,0,0],
              "SRRS": [0,0,0],
              "SRRP": [0,0,0],
              "SRPR": [0,0,0],
              "SRPS": [0,0,0],
              "SRPP": [0,0,0],
              "SRSR": [0,0,0],
              "SRSS": [0,0,0],
              "SRSP": [0,0,0],
              "SPRR": [0,0,0],
              "SPRS": [0,0,0],
              "SPRP": [0,0,0],
              "SPPR": [0,0,0],
              "SPPS": [0,0,0],
              "SPPP": [0,0,0],
              "SPSR": [0,0,0],
              "SPSS": [0,0,0],
              "SPSP": [0,0,0],
              "SSRR": [0,0,0],
              "SSRS": [0,0,0],
              "SSRP": [0,0,0],
              "SSPR": [0,0,0],
              "SSPS": [0,0,0],
              "SSPP": [0,0,0],
              "SSSR": [0,0,0],
              "SSSS": [0,0,0],
              "SSSP": [0,0,0],
          }):

    try:

      opponent_history.append(prev_play)

      dict_aux = {"R":0,"P":1,"S":2}
      dict_resp = {0:"P",1:"S",2:"R"}

      if len(opponent_history) > 5:

          ind = dict_aux[opponent_history[-1]]
          ind_m2 = opponent_history[-5] + opponent_history[-4] + opponent_history[-3] + opponent_history[-2]
          ind_d2 = opponent_history[-4] + opponent_history[-3] + opponent_history[-2] + opponent_history[-1]

          dict_markov4[ind_m2][ind] += 1

          max_ = max(dict_markov4[ind_d2])

          index = random.choice([i for i in range(len(dict_markov4[ind_d2])) if dict_markov4[ind_d2][i] == max_])

          guess = dict_resp[index]

      else:

        guess = dict_resp[random.randint(0,2)]

      return guess

    except:
      pass


def multi_IA_123(prev_play, opponent_history=[],
    m1_history=[],m2_history=[],m3_history=[]):

    m1 = markov1(prev_play)
    m2 = markov2(prev_play)
    m3 = markov3(prev_play)

    opponent_history.append(prev_play)
    m1_history.append(m1)
    m2_history.append(m2)
    m3_history.append(m3)

    #print(m3_history,opponent_history)

    return m3
