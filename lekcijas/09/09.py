import pandas as pd

def read_csv_file(url):
    df = pd.read_csv(url, sep=';')
    return df

csv = 'https://data.gov.lv/dati/dataset/e909312a-61c9-4cde-a72a-0a09dd75ef43/resource/d01a32c6-add8-4b8d-a013-0c35a3879564/download/eis_e_iepirkumi_rezultati_2021.csv'

df = read_csv_file(csv)

df.columns

# Iznemt kolonnas nosaukumus

df = df[['Iepirkuma_ID', ' Iepirkuma_nosaukums',
       ' Iepirkuma_identifikacijas_numurs', ' Pasutitaja_nosaukums',
       ' Pasutitaja_registracijas_numurs',
       ' Pasutitaja_registracijas_numura_veids', ' Pasutitaja_PVS_ID',
       ' Augstak_stavosa_organizacija', ' Iepirkuma_statuss',
       ' Regulejasais_tiesibu_akts', ' Proceduras_veids',
       ' Hipersaite_EIS_kura_pieejams_zinojums',
       ' Hipersaite_uz_IUB_publikaciju', ' Ir_dalijums_dalas',
       ' Iepirkuma_dalas_nr', ' Iepirkuma_dalas_nosaukums',
       ' Iepirkuma_dalas_statuss', ' Uzvaretaja_nosaukums',
       ' Uzvaretaja_registracijas_numurs']]

df.columns = df.columns.str.strip()


df.map(lambda x: x.replace('=',''))