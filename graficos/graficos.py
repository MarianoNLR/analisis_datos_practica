import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./supermarket_sales.csv')

# Eliminar filas con valores nulos.
df_limpio = df.dropna()

# Configuracion del estilo visual de seaborn
sns.set_theme(style='darkgrid')


# 1. Numero de Ventas por ciudad.
# plt.figure(figsize=(10,6))
# sns.countplot(data=df_limpio, x='City', order=df_limpio['City'].value_counts().index, palette='pastel', hue='City', legend=True)
# plt.title('Ventas por Ciudad')
# plt.xlabel('Ciudad')
# plt.ylabel('Numero de ventas')
# plt.show()

# 2. Ingreso total de Ventas por ciudad
# ventas_totales_por_ciudad = df_limpio.groupby('City')['Total'].sum().reset_index()
# plt.figure(figsize=(10,6))
# sns.barplot(x='City', y='Total', data=ventas_totales_por_ciudad)
# plt.title('Total de Ventas por Ciudad')
# plt.xlabel('Ciudad')
# plt.ylabel('Total de ventas')
# plt.show()

# 3. Distribucion de precios unitarios
# plt.figure(figsize=(10,6))
# sns.histplot(df_limpio['Unit price'], kde=True, bins=30, element='step', alpha=0.4)
# plt.title('Distribucion de Precio Unitario')
# plt.xlabel('Precio de Producto')
# plt.ylabel('Frecuencia')
# plt.show()

# 4. Ventas por genero de cliente
# plt.figure(figsize=(10,6))
# sns.countplot(data=df_limpio, x='Gender', palette='pastel', order=df_limpio['Gender'].value_counts().index, hue='Gender', legend=True)
# plt.title('Ventas por genero de cliente')
# plt.xlabel('Género')
# plt.ylabel('Numero de ventas')
# plt.show()

# 5. Ventas por línea de producto
# plt.figure(figsize=(10,6))
# sns.countplot(data=df_limpio, x='Product line', palette='rainbow', order=df_limpio['Product line'].value_counts().index, hue='Product line', legend=True)
# plt.title('Ventas por línea de producto')
# plt.xlabel('Categoria')
# plt.xticks(rotation=45)
# plt.ylabel('Numero de Ventas')
# plt.show()

# 6. Distribucion de ventas por hora del dia
# df_hora_venta = df_limpio
# df_hora_venta['Hour'] = pd.to_datetime(df_limpio['Time'], format='%H:%M').dt.hour
# print(df_hora_venta.head())
# plt.figure(figsize=(10,6))
# sns.histplot(df_hora_venta['Hour'], bins=24)
# plt.title('Ventas por hora del dia.')
# plt.xlabel('Hora')
# plt.ylabel('Número de ventas')
# plt.xticks(range(0,24))
# plt.show()

# 7. Ventas por forma de pago
# plt.figure(figsize=(10,6))
# sns.countplot(data=df_limpio, x='Payment', palette='rainbow', order=df_limpio['Payment'].value_counts().index, hue='Payment', legend=True)
# plt.xlabel('Forma de pago')
# plt.ylabel('Cantidad de Ventas')
# plt.xticks(rotation=45)
# plt.show()

# 8. Distribucion de ventas por dia de la semana
# df_dia_venta = df_limpio
# df_dia_venta['Day of week'] = pd.to_datetime(df_limpio['Date'], format='%m/%d/%Y').dt.day_name()
# sns.countplot(data=df_dia_venta, x='Day of week', order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
# plt.title('Ventas dia de la semana.')
# plt.xlabel('Dia')
# plt.ylabel('Número de ventas')
# plt.xticks(rotation=45)
# plt.show()

# df_limpio['FechaHora'] = pd.to_datetime(df_limpio['Date'].astype(str) + ' ' + df_limpio['Time'].astype(str))
# print(df_limpio)