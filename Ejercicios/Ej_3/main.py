from lib.func import Poliza


def main():
    df1 = Poliza().get_data("cartera_polizas.csv")
    df2 = Poliza().get_data("siniestros.csv")
    df_join = Poliza()
    df_join.df=df1.join(df2)
    total=df_join.total("pago")
    sinisesto = df_join.siniestralidad()
    print(f"Array unido: \n {df_join.df} \n\nPago total: {total:,.2f} \n\nSiniestralidad por poliza: \n {sinisesto}")
if __name__ == "__main__":
    main()