import pandas as pd


# Leer un archivo excel, csv, json, etc
def read():
    polizas = pd.read_csv("./data/cartera_polizas.csv", parse_dates=["fecha_inicio"])
    siniestros = pd.read_csv("./data/siniestros.csv")
    return [polizas, siniestros]


def convertir(polizas):
    polizas["fecha_inicio"] = pd.to_datetime(polizas["fecha_inicio"], errors="coerce")
    return polizas


def join(df1, df2):
    df = df1.merge(
        df2[["id_poliza", "producto", "suma_asegurada", "edad"]],
        on="id_poliza",
        how="left",
    )
    return df


def freq(df):
    frecuencia = df.groupby("id_poliza").size().rename("n_siniestros")
    return frecuencia


def rangos(df):
    cortes = [18, 30, 40, 50, 60, 120]
    labels = ["18-29", "30-39", "40-49", "50-59", "60+"]
    df["banda_edad"] = pd.cut(df["edad"], bins=cortes, labels=labels)
    return df


def main():
    polizas = read()[0]
    siniestros = read()[1]
    polizas = convertir(polizas)
    tabla_unida = join(siniestros, polizas)
    tabla_freq = freq(tabla_unida)
    tabla_final = rangos(tabla_unida)
    print(tabla_final)


if __name__ == "__main__":
    main()
