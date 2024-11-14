times=('Palmeiras','Gremio','Atletico-MG','Flamengo','Botafogo','Bragantino','Fluminense','Atletico-PR','Internacional','Fortaleza','Sao Paulo','Cuiaba','Corintians',
       'Cruzeiro','Vasco da Gama','Bahia','Santos','Goias','Coritiba','America-MG')
print(f"os cinco primeiros são {times[0:5]}")
print(f"os quatro ultimos são {times[-4:len(times)]}")
print(f"em ordem alfabetica fica {sorted(times)}")
print(f"Coritiba está na posição {times.index('Coritiba')+1}")