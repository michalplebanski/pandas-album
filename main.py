import pandas as pd
df = pd.read_excel('original-data.xlsx')
df_copy = df.copy()

new_headers = {
    'TITLE': 'TYTUŁ',
    'ARTIST': 'ARTYSTA',
    'YEAR': 'ROK',
    'HIGH POSN': 'MAX POZ'
}

#shows the most popular artist
band_columns = 'ARTIST'
band_values = df[band_columns].value_counts()
most_popular_band = band_values.index[0]
print(f"Najczęściej występujący zespół to: {most_popular_band}")

#rename columns
df_copy.rename(columns=new_headers, inplace=True)

#delete column MAX POZ
if "MAX POZ" in df_copy.columns:
    df_copy.drop(columns=["MAX POZ"], inplace=True)

#change font size of column
df_copy.rename(columns=lambda x: x.title(), inplace=True)

#most popular albums
album_counts_by_year = df_copy["Rok"].value_counts()
max_albums_years = album_counts_by_year[album_counts_by_year == album_counts_by_year.max()]
print(f"Najwięcej albumów zostało wydanych w roku(latach): {max_albums_years}")

#filters albums in specific years
albums_between_1960_and_1990 = df_copy[
    (df_copy["Rok"] >= 1960) & (df_copy["Rok"] <= 1990)
]

num_albums_between_1960_and_1990 = albums_between_1960_and_1990.shape[0]
print(f"Liczba albumów wydanych między 1960 a 1990 rokiem (włącznie): {num_albums_between_1960_and_1990}")

#youngest album
youngest_album_year = df_copy["Rok"].max()
print(f"Najmłodszy album na liście został wydany w roku: {youngest_album_year}")

#earliest albums
earliest_albums = df_copy.groupby("Artysta")["Rok"].min().reset_index()

print(f"Najwcześniej wydane albumy każdego artysty:{earliest_albums}")

writer = pd.ExcelWriter('new-data.xlsx', engine='openpyxl')
df_copy.to_excel(writer, index=False)

writer.close()
