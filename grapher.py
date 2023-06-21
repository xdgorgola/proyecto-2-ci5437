import pandas as pd
import plotly.express as px
from math import log
# 17
negamax_min_max = \
  [ {"value":-4, "expanded":0, "generated":0, "seconds":1.00024e-06, "generated/second":0}
  , {"value":-4, "expanded":1, "generated":1, "seconds":6.99982e-06, "generated/second":142861}
  , {"value":-4, "expanded":3, "generated":4, "seconds":2.99979e-06, "generated/second":1.33343e+06}
  , {"value":-2147483648, "expanded":1, "generated":0, "seconds":9.99775e-07, "generated/second":0}
  , {"value":4, "expanded":6, "generated":7, "seconds":4.99981e-06, "generated/second":1.40005e+06}
  , {"value":4, "expanded":7, "generated":8, "seconds":3.00026e-06, "generated/second":2.66644e+06}
  , {"value":4, "expanded":49, "generated":66, "seconds":1.89999e-05, "generated/second":3.4737e+06}
  , {"value":4, "expanded":98, "generated":130, "seconds":4.10001e-05, "generated/second":3.17073e+06}
  , {"value":2, "expanded":575, "generated":754, "seconds":0.000197, "generated/second":3.82741e+06}
  , {"value":2, "expanded":2361, "generated":3173, "seconds":0.000832, "generated/second":3.8137e+06}
  , {"value":2, "expanded":6244, "generated":7959, "seconds":0.002108, "generated/second":3.77562e+06}
  , {"value":2, "expanded":37532, "generated":48266, "seconds":0.013115, "generated/second":3.68021e+06}
  , {"value":2, "expanded":222933, "generated":287306, "seconds":0.077227, "generated/second":3.72028e+06}
  , {"value":2, "expanded":1781833, "generated":2263734, "seconds":0.621852, "generated/second":3.64031e+06}
  , {"value":-10, "expanded":6548613, "generated":8358060, "seconds":2.26065, "generated/second":3.69719e+06}
  , {"value":-3, "expanded":44595493, "generated":57894111, "seconds":15.4569, "generated/second":3.74551e+06}
  , {"value":-3, "expanded":436519885, "generated":574629641, "seconds":152.546, "generated/second":3.76693e+06}
  , {"value":-3, "expanded":2805093090, "generated":3708262376, "seconds":996.899, "generated/second":3.7198e+06}
  ]

# 10
negamax_alpha_beta = \
  [  {"value":-4, "expanded":0, "generated":0, "seconds":9.99775e-07, "generated/second":0}
  ,  {"value":-4, "expanded":1, "generated":1, "seconds":1.99955e-06, "generated/second":500113      }
  ,  {"value":-4, "expanded":3, "generated":4, "seconds":2.00002e-06, "generated/second":1.99998e+06 }
  ,  {"value":-2147483648, "expanded":1, "generated":0, "seconds":9.99775e-07, "generated/second":0  }
  ,  {"value":4, "expanded":6, "generated":7, "seconds":2.00002e-06, "generated/second":3.49997e+06  }
  ,  {"value":4, "expanded":7, "generated":8, "seconds":2.00002e-06, "generated/second":3.99997e+06}
  ,  {"value":4, "expanded":17, "generated":20, "seconds":4.00003e-06, "generated/second":4.99996e+06}
  ,  {"value":4, "expanded":25, "generated":29, "seconds":6.00005e-06, "generated/second":4.8333e+06}
  ,  {"value":2, "expanded":147, "generated":178, "seconds":3.3e-05, "generated/second":5.39394e+06}
  ,  {"value":2, "expanded":381, "generated":472, "seconds":8.40002e-05, "generated/second":5.61904e+06}
  ,  {"value":2, "expanded":999, "generated":1200, "seconds":0.000198, "generated/second":6.06062e+06}
  ,  {"value":2, "expanded":3631, "generated":4374, "seconds":0.000786, "generated/second":5.56489e+06}
  ,  {"value":2, "expanded":6728, "generated":8158, "seconds":0.001448, "generated/second":5.63398e+06}
  ,  {"value":2, "expanded":61859, "generated":74137, "seconds":0.025632, "generated/second":2.89236e+06}
  ,  {"value":-10, "expanded":88527, "generated":107371, "seconds":0.038983, "generated/second":2.7543e+06}
  ,  {"value":-3, "expanded":173194, "generated":210616, "seconds":0.075911, "generated/second":2.77451e+06}
  ,  {"value":-3, "expanded":1029920, "generated":1270471, "seconds":0.475626, "generated/second":2.67116e+06}
  ,  {"value":-3, "expanded":1535491, "generated":1892683, "seconds":0.698836, "generated/second":2.70834e+06}
  ,  {"value":-3, "expanded":16194511, "generated":20352253, "seconds":7.4296, "generated/second":2.73935e+06}
  ,  {"value":-3, "expanded":34643976, "generated":43661622, "seconds":16.6768, "generated/second":2.6181e+06}
  ,  {"value":-4, "expanded":69179931, "generated":87176788, "seconds":32.5574, "generated/second":2.67763e+06}
  ,  {"value":-4, "expanded":320632162, "generated":404741432, "seconds":173.038, "generated/second":2.33903e+06}
  ,  {"value":0, "expanded":3224251, "generated":5129464, "seconds":676.026, "generated/second":7587.68}
  ,  {"value":-2, "expanded":3464038517, "generated":67948849, "seconds":1938.65, "generated/second":35049.6}
  ,  {"value":-2, "expanded":1879244970, "generated":3497406762, "seconds":3454.18, "generated/second":1.01251e+06  }
  ]

#11
scout = \
  [ {"value":4, "expanded":0, "generated":0, "seconds":1.99955e-06, "generated/second":0}
  , {"value":-4, "expanded":1, "generated":1, "seconds":5.00027e-06, "generated/second":199989}
  , {"value":4, "expanded":2, "generated":4, "seconds":2.99979e-06, "generated/second":1.33343e+06}
  , {"value":0, "expanded":1, "generated":0, "seconds":1.00024e-06, "generated/second":0}
  , {"value":0, "expanded":8, "generated":9, "seconds":6.99982e-06, "generated/second":1.28575e+06}
  , {"value":0, "expanded":9, "generated":10, "seconds":6.99982e-06, "generated/second":1.42861e+06}
  , {"value":0, "expanded":13, "generated":18, "seconds":8.99937e-06, "generated/second":2.00014e+06}
  , {"value":0, "expanded":28, "generated":53, "seconds":2.50004e-05, "generated/second":2.11996e+06}
  , {"value":0, "expanded":151, "generated":305, "seconds":0.000121, "generated/second":2.52066e+06}
  , {"value":-6, "expanded":175, "generated":411, "seconds":0.000171, "generated/second":2.40351e+06}
  , {"value":6, "expanded":749, "generated":1743, "seconds":0.000681, "generated/second":2.55947e+06}
  , {"value":0, "expanded":467, "generated":1168, "seconds":0.000493, "generated/second":2.36917e+06}
  , {"value":0, "expanded":2940, "generated":6901, "seconds":0.002946, "generated/second":2.3425e+06}
  , {"value":0, "expanded":12583, "generated":31349, "seconds":0.013398, "generated/second":2.33983e+06}
  , {"value":0, "expanded":53642, "generated":138714, "seconds":0.057635, "generated/second":2.40677e+06}
  , {"value":0, "expanded":78268, "generated":199997, "seconds":0.087097, "generated/second":2.29626e+06}
  , {"value":0, "expanded":209350, "generated":566373, "seconds":0.315409, "generated/second":1.79568e+06}
  , {"value":0, "expanded":537207, "generated":1389809, "seconds":0.647099, "generated/second":2.14775e+06}
  , {"value":0, "expanded":2526372, "generated":6900309, "seconds":3.35677, "generated/second":2.05564e+06}
  , {"value":0, "expanded":4136289, "generated":11348148, "seconds":5.35708, "generated/second":2.11835e+06}
  , {"value":0, "expanded":18027214, "generated":52158453, "seconds":23.9705, "generated/second":2.17594e+06}
  , {"value":0, "expanded":38740608, "generated":111332522, "seconds":50.2478, "generated/second":2.21567e+06}
  , {"value":0, "expanded":520878670, "generated":1483565490, "seconds":648.2, "generated/second":2.28875e+06}
  , {"value":0, "expanded":1131568553, "generated":3193588664, "seconds":1450.82, "generated/second":2.20123e+06 }
  ]

#9
negascout = \
  [ {"value":-4, "expanded":0, "generated":0, "seconds":2.00002e-06, "generated/second":0}
  , {"value":-4, "expanded":1, "generated":1, "seconds":4.00003e-06, "generated/second":249998}
  , {"value":-4, "expanded":3, "generated":4, "seconds":3.9998e-06, "generated/second":1.00005e+06     }
  , {"value":-200, "expanded":1, "generated":0, "seconds":1.00001e-06, "generated/second":0}
  , {"value":-200, "expanded":9, "generated":9, "seconds":5.00004e-06, "generated/second":1.79999e+06  }
  , {"value":-200, "expanded":10, "generated":10, "seconds":7.99983e-06, "generated/second":1.25003e+06}
  , {"value":-200, "expanded":11, "generated":11, "seconds":9.00007e-06, "generated/second":1.22221e+06}
  , {"value":-200, "expanded":38, "generated":42, "seconds":1.90001e-05, "generated/second":2.21051e+06}
  , {"value":-200, "expanded":213, "generated":244, "seconds":9.5e-05, "generated/second":2.56842e+06  }
  , {"value":-200, "expanded":264, "generated":318, "seconds":0.000127, "generated/second":2.50394e+06}
  , {"value":-200, "expanded":477, "generated":564, "seconds":0.000279, "generated/second":2.02151e+06}
  , {"value":-200, "expanded":1096, "generated":1286, "seconds":0.000692, "generated/second":1.85838e+06}
  , {"value":-200, "expanded":1762, "generated":2063, "seconds":0.00095, "generated/second":2.17158e+06}
  , {"value":-5, "expanded":22528, "generated":26779, "seconds":0.011225, "generated/second":2.38566e+06}
  , {"value":-6, "expanded":29874, "generated":35766, "seconds":0.021321, "generated/second":1.6775e+06}
  , {"value":-6, "expanded":52428, "generated":62336, "seconds":0.028755, "generated/second":2.16783e+06}
  , {"value":-6, "expanded":205413, "generated":248175, "seconds":0.106787, "generated/second":2.32402e+06}
  , {"value":-6, "expanded":381374, "generated":460706, "seconds":0.2136, "generated/second":2.15686e+06}
  , {"value":-6, "expanded":3380066, "generated":4190261, "seconds":1.94793, "generated/second":2.15114e+06}
  , {"value":-2, "expanded":16992650, "generated":21220286, "seconds":10.0145, "generated/second":2.11895e+06}
  , {"value":-2, "expanded":54098487, "generated":66662224, "seconds":32.1805, "generated/second":2.07151e+06}
  , {"value":-2, "expanded":97552015, "generated":120694553, "seconds":58.3955, "generated/second":2.06685e+06}
  , {"value":-8, "expanded":816134204, "generated":1005264618, "seconds":478.144, "generated/second":2.10243e+06       }
  , {"value":-8, "expanded":1319457904, "generated":1638389048, "seconds":779.431, "generated/second":2.10203e+06}
  , {"value":-8, "expanded":1888020125, "generated":2348800529, "seconds":1123.22, "generated/second":2.09113e+06      }
  , {"value":-8, "expanded":2499872789, "generated":3109932267, "seconds":1505.92, "generated/second":2.06513e+06  }
  ]


#algorithms = ["negamax_min_max","negamax_alpha_beta","scout","negascout"]
algorithms = [1,5,9,13]


def pad(n : int,pad_element):
  def _pad(xs):
    return xs + [pad_element for _ in range(n - len(xs))]
  return _pad

data = pd.DataFrame({
  'moves' : [i for i in range(1,35)],
  'negamax_min_max_expanded': pad(34,float("inf"))(list(map(lambda x: log(1+x["expanded"]),negamax_min_max))),
  'negamax_min_max_generated': pad(34,float("inf"))(list(map(lambda x: log(1+x["generated"]),negamax_min_max))),
  'negamax_min_max_seconds': pad(34,float("inf"))(list(map(lambda x: log(1+x["seconds"]),negamax_min_max))),
  'negamax_min_max_generated/second': pad(34,float("inf"))(list(map(lambda x: log(1+x["generated/second"]),negamax_min_max))),

  'negamax_alpha_beta_expanded': pad(34,float("inf"))(list(map(lambda x: log(1+x["expanded"]),negamax_alpha_beta))),
  'negamax_alpha_beta_generated': pad(34,float("inf"))(list(map(lambda x: log(1+x["generated"]),negamax_alpha_beta))),
  'negamax_alpha_beta_seconds': pad(34,float("inf"))(list(map(lambda x: log(1+log(1+x["seconds"])),negamax_alpha_beta))),
  'negamax_alpha_beta_generated/second': pad(34,float("inf"))(list(map(lambda x: log(1+x["generated/second"]),negamax_alpha_beta))),

  'scout_expanded': pad(34,float("inf"))(list(map(lambda x: log(1+x["expanded"]),scout))),
  'scout_generated': pad(34,float("inf"))(list(map(lambda x: log(1+x["generated"]),scout))),
  'scout_seconds': pad(34,float("inf"))(list(map(lambda x: log(1+x["seconds"]),scout))),
  'scout_generated/second': pad(34,float("inf"))(list(map(lambda x: log(1+x["generated/second"]),scout))),

  'negascout_expanded': pad(34,float("inf"))(list(map(lambda x: log(1+x["expanded"]),negascout))),
  'negascout_generated': pad(34,float("inf"))(list(map(lambda x: log(1+x["generated"]),negascout))),
  'negascout_seconds': pad(34,float("inf"))(list(map(lambda x: log(1+x["seconds"]),negascout))),
  'negascout_generated/second': pad(34,float("inf"))(list(map(lambda x: log(1+x["generated/second"]),negascout))),
})

expanded_slice  = slice(1,17,4)
generated_slice = slice(2,17,4)
seconds_slice   = slice(3,17,4)
generated_per_second_slice = slice(4,17,4)

print([algorithm + 0 for algorithm in algorithms])
print(data.columns[expanded_slice])


fig_expanded = px.line(data, 
  x='moves', 
  y=data.columns[expanded_slice],
  title="Log of Expanded Nodes per PV level",
  labels={'x':"PV level", 'y':"log(Nodes)"}
  )

fig_generated = px.line(data, 
  x='moves', 
  y=data.columns[generated_slice],
  title="Log of Generated Nodes per PV level",
  labels={'x':"PV level", 'y':"log(Nodes)"}
  )


fig_seconds = px.line(data, 
  x='moves', 
  y=data.columns[seconds_slice],
  title="Log of Seconds spent per PV level",
  labels={'x':"PV level", 'y':"log(seconds)"}
  )

fig_generated_second = px.line(data, 
  x='moves', 
  y=data.columns[seconds_slice],
  title="Log of Generated Nodes per Seconds per PV level",
  labels={'x':"PV level", 'y':"log(Generated/seconds)"}
  )

# Show plot 
fig_expanded.show()
fig_generated.show()
fig_seconds.show()
fig_generated_second.show()


