import pandas as pd
import matplotlib.pyplot as plt

plt.close('all')

peak_energy_demand = pd.read_excel('pk_demand_temperature.xlsm', sheet_name='Peak Demand')
# peak_demand_df = pd.DataFrame(peak_demand, index=pd.to_datetime(peak_demand['Date']), columns=['FY17'])
# peak_demand_df = pd.DataFrame(peak_demand, index=pd.date_range('7/1/2016', periods=365), columns=['FY17', 'FY18', 'FY19', 'FY20'])
# peak_demand_df.set_index(index=pd.date_range('7/1/2016', periods=365), inplace=True)
# peak_demand_df = peak_demand_df.cumsum()
# peak_demand_time = pd.DataFrame(peak_demand, columns=['Date'])

peak_energy_demand['Date'] = peak_energy_demand['Date'].apply(pd.to_datetime)
peak_energy_demand.set_index('Date', inplace=True)
peak_energy_demand['FY17'].plot()
peak_energy_demand['FY18'].plot()
peak_energy_demand['FY19'].plot()
peak_energy_demand['FY20'].plot()

# peak_demand_df['Date'] = pd.to_datetime(peak_demand_df['Date'], infer_datetime_format=True)
# peak_demand_df.plot()
plt.title('Peak Energy Demand FY17-FY20')
plt.xlabel('Date')
plt.ylabel('Energy Demand')
plt.show()

peak_temperature = pd.read_excel('pk_demand_temperature.xlsm', sheet_name='High Temperature')
peak_temperature['Date'] = peak_temperature['Date'].apply(pd.to_datetime)
peak_temperature.set_index('Date', inplace=True)
peak_temperature['FY17'].plot()
peak_temperature['FY18'].plot()
peak_temperature['FY19'].plot()
peak_temperature['FY20'].plot()

plt.title('Peak Temperature FY17-FY20')
plt.xlabel('Date')
plt.ylabel('Degrees Farenheit')
plt.show()

# plt.scatter(pd.date_range('7/1/2016', periods=365), pd['FY17'], s=100, c='red')

# high_temperature = pd.read_excel('pk_demand_temperature.xlsm', sheet_name='High Temperature')
# high_temperature_df = pd.DataFrame(high_temperature, columns=['FY17'])

# high_temperature_df.plot()
# plt.show()