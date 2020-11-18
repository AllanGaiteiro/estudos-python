### tuplas


### sao imutaveis

cord = (-23.588254, -46.632477)
print(type(cord))

### da pra usar [para achar]
#print(cord[1])

### 'imutaveis'

cord += ('calor',)### presisa da virgula

### tuplas ocupam menos espaço da memoria



print(cord)
### melhorando 
from collections import namedtuple

Cordenadas = namedtuple('Cordenadas', ['latidude','longitude'])
cord2 = Cordenadas(2.23233,-12.2332)

print(cord2)