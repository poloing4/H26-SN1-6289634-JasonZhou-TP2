import pandas as pd
def QA1VariablePresente():
    df=pd.read_csv("vdq-arbrerepertorie.csv")
    return df.columns.to_list()
def QA2NomTopographique():
    df=pd.read_csv("vdq-arbrerepertorie.csv")
    grostronc=df.sort_values(by='DIAMETRE',ascending=False)
    return(grostronc.iloc[0]['NOM_TOPOGRAPHIE'])
def QA3NombreFeuilluConifere():
    df=pd.read_csv("vdq-arbrerepertorie.csv")
    feuillu=df[df['TYPE_ARBRE']=='Feuillu']['NOM_LATIN'].nunique()
    conifère=df[df['TYPE_ARBRE']=='Conifère']['NOM_LATIN'].nunique()
    return (feuillu,conifère)
def QA4ArbreAimemivile():
    df=pd.read_csv("vdq-arbrerepertorie.csv")
    df=df.dropna(subset=["NOM_TOPOGRAPHIE", "NOM_FRANCAIS"])
    parc=df[df['NOM_TOPOGRAPHIE'].str.contains('Parc Aimée-Miville')]
    especes=parc["NOM_FRANCAIS"].drop_duplicates().sort_values()
    return especes.to_list()
def QA5Especegros():
    df=pd.read_csv("vdq-arbrerepertorie.csv")
    grostronc=df.sort_values(by='DIAMETRE', ascending=False)
    return (grostronc.iloc[0]['NOM_LATIN'])
print(QA5Especegros())