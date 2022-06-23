from NEIScraper import *
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

source = importHTML('StateElectricityGenerationFuelShares.html')
sourcedata = getdata(source)
data = sourcedata[0]
headers = sourcedata[1]

width=0.65

state = []
nuclear = []
coal = []
gas = []
petroleum = []
hydro = []
geothermal = []
solar = []
wind = []
other = []

k=0
for i in data:
	k += 1

	state.append(i[0])
	nuclear.append(i[1])
	coal.append(i[2])
	gas.append(i[3])
	petroleum.append(i[4])
	hydro.append(i[5])
	geothermal.append(i[6])
	solar.append(i[7])
	wind.append(i[8])
	other.append(i[9])

	state_np = np.array(state)
	nuclear_np = np.array(nuclear)
	coal_np = np.array(coal)
	gas_np = np.array(gas)
	petroleum_np = np.array(petroleum)
	hydro_np = np.array(hydro)
	geothermal_np = np.array(geothermal)
	solar_np = np.array(solar)
	wind_np = np.array(wind)
	other_np = np.array(other)

plt.style.use('seaborn-dark-palette')

fig, ax = plt.subplots()

plt.bar(state,nuclear_np, width, label = 'nuclear', color = 'darkgreen')
plt.bar(state,coal_np, width, label = 'coal', bottom =(nuclear_np), color = 'black')
plt.bar(state,gas_np, width, label = 'gas', bottom = (nuclear_np + coal_np), color = 'cadetblue')
plt.bar(state,petroleum_np, width, label = 'petroleum', bottom = (nuclear_np + coal_np + gas_np), color = 'brown')
plt.bar(state,hydro_np, width, label = 'hydro', bottom =(nuclear_np + coal_np + gas_np + petroleum_np), color = 'blue')
plt.bar(state,geothermal_np, width, label = 'geothermal', bottom = (nuclear_np + coal_np + gas_np + petroleum_np + hydro_np), color = 'darkred')
plt.bar(state,solar_np, width, label = 'solar', bottom = (nuclear_np + coal_np + gas_np + petroleum_np + hydro_np + geothermal_np), color = 'olive')
plt.bar(state,wind_np, width, label = 'wind', bottom = (nuclear_np + coal_np + gas_np + petroleum_np + hydro_np + geothermal_np + solar_np), color = 'seagreen')
plt.bar(state,other_np, width, label = 'other', bottom = (nuclear_np + coal_np + gas_np + petroleum_np + hydro_np + geothermal_np + solar_np + wind_np), color = 'grey')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.xticks(rotation = 85)
plt.show()