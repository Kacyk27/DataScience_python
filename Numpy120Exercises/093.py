import numpy as np


np.set_printoptions(linewidth=160, suppress=True)

wig_games = np.array([['Profile', 'Time', 'Course', 'Open', 'Low', 'High', 'Turn', 'Share'],
       ['11B(11BIT)', '17kwi17:01', '391.00', '383.50', '383.00', '394.00', '4994874', '19.034%'],
       ['CDR(CDPROJEKT)', '17kwi17:01', '339.50', '338.30', '337.00', '344.20', '79245368', '39.618%'],
       ['CIG(CIGAMES)', '17kwi17:03', '0.742', '0.772', '0.730', '0.772', '971459', '1.855%'],
       ['PLW(PLAYWAY)', '17kwi17:03', '387.50', '374.00', '373.00', '388.00', '12661786', '10.638%'],
       ['TEN(TSGAMES)', '17kwi17:02', '349.50', '332.00', '330.00', '353.50', '13697060', '28.855%']], dtype='<U14')

np.savetxt(fname='wig_games.csv', X=wig_games, fmt='%s', delimiter=',')
wig_games_new = np.loadtxt(fname='wig_games.csv', delimiter=',', dtype=str)
print(wig_games_new)


