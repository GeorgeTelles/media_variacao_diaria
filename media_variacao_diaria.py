"""
Esse codigo plota um grafico mostrando a média de variação diaria
de um ativo (VARIAÇÃO DO VALOR OU PONTOS). ele pega as informações do MT5

By: George Telles
+55 11 93290-7425
"""

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
print(data)

dados_analisados = pd.Series(data["variacao"])
figure(figsize = (10, 6), dpi = 80)
dados_analisados.plot.hist(grid=True, bins=100, rwidth=0.9, color = "#607c8e")

plt.title("Variação de pontos desde a abertura, o ponto 0.0 representa abertura do pregão")
plt.xlabel("Quantidade de pregões")
plt.ylabel("Variação de pontos desde a abertura")
plt.show()
