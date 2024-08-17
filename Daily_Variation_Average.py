import matplotlib.pyplot as plt
import MetaTrader5 as mt5
import pandas as pd
from matplotlib.pyplot import figure

symbol = "PETR4"

if not mt5.initialize():
    print(f"initialize() failed, error code = {mt5.last_error()} ")

selected=mt5.symbol_select(symbol,True)
if not selected:
    print(f"Failed to select, error code = {mt5.last_error()} ")
else:
    symbol_info=mt5.symbol_info(symbol)
    print(symbol_info.name)
    print()

data = pd.DataFrame(mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_D1, 0, 2000))
data["time"] = pd.to_datetime(data["time"], unit = "s")
data["variacao"] = data["close"] - data["open"]


dados_analisados = pd.Series(data["variacao"])
figure(figsize = (10, 6), dpi = 80)
dados_analisados.plot.hist(grid=True, bins=100, rwidth=0.9, color = "#607c8e")

print(dados_analisados.describe())

plt.title("Variação de pontos desde a abertura")
plt.xlabel("Quantidade de pregões")
plt.ylabel("Variação de pontos desde a abertura")
plt.show()
