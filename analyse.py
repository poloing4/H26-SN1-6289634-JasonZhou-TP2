import pandas as pd
def QA1():
    df=pd.read_csv("vdq-arbrerepertorie.csv")
    return df.columns.to_list()
def QA2():
    df=pd.read_csv("vdq-arbrerepertorie.csv")
    grostronc=df.sort_values(by='DIAMETRE',ascending=False)
    return(grostronc.iloc[0]['NOM_TOPOGRAPHIE'])
def QA3():
    df=pd.read_csv("vdq-arbrerepertorie.csv")
    feuillu=df[df['TYPE_ARBRE']=='Feuillu']['NOM_LATIN'].nunique()
    conifère=df[df['TYPE_ARBRE']=='Conifère']['NOM_LATIN'].nunique()
    return (feuillu,conifère)
def QA4():
    df=pd.read_csv("vdq-arbrerepertorie.csv")
    df=df.dropna(subset=["NOM_TOPOGRAPHIE", "NOM_FRANCAIS"])
    parc=df[df['NOM_TOPOGRAPHIE'].str.contains('Parc Aimée-Miville')]
    especes=parc["NOM_FRANCAIS"].drop_duplicates().sort_values()
    return especes.to_list()
def QA5():
    df=pd.read_csv("vdq-arbrerepertorie.csv")
    grostronc=df.sort_values(by='DIAMETRE', ascending=False)
    return (grostronc.iloc[0]['NOM_LATIN'])
def QA6():
    df=pd.read_csv("vdq-arbrerepertorie.csv")
    df = df.dropna(subset=["NOM_TOPOGRAPHIE","TYPE_ARBRE","DIAMETRE"])
    unifeuillu=df[(df["NOM_TOPOGRAPHIE"].str.contains("Université Laval"))&(df["TYPE_ARBRE"]=="Feuillu")]
    uniconfiere=df[(df["NOM_TOPOGRAPHIE"].str.contains("Université Laval"))&(df["TYPE_ARBRE"]=="Conifère")]
    uni={}
    uni['diametre_feuillus']=unifeuillu['DIAMETRE'].mean()
    uni['diametre_coniferes']=uniconfiere['DIAMETRE'].mean()
    return uni
def QASommaire():
        with open("sommaire.txt", "w", encoding="utf-8") as f:
            Q1=', '.join(QA1())
            f.write(f"#1 - Quelles sont les variables présentes dans le jeu de données? Reponse:{Q1} \n")
            Q2=''.join(QA2())
            f.write(f"#2 - Le nom de la topographie où se trouve l'arbre avec le tronc le plus grand? Reponse:{Q2} \n")
            Q3V=QA3().values()
            Q3VX=''.join(Q3V)
            Q3K=''.join(QA3().keys())
            f.write(f"#3 - Combien dénombre-t-on d'espèces différentes chez les feuillus et les conifères? Reponse:{Q3VX} \n")
QASommaire()