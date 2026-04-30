from tokenize import group

import matplotlib.pyplot as plt
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
    df=df.dropna(subset=["NOM_TOPOGRAPHIE","TYPE_ARBRE","DIAMETRE"])
    unifeuillu=df[(df["NOM_TOPOGRAPHIE"].str.contains("Université Laval"))&(df["TYPE_ARBRE"]=="Feuillu")]
    uniconfiere=df[(df["NOM_TOPOGRAPHIE"].str.contains("Université Laval"))&(df["TYPE_ARBRE"]=="Conifère")]
    uni={}
    uni['diametre_feuillus']=unifeuillu['DIAMETRE'].mean()
    uni['diametre_coniferes']=uniconfiere['DIAMETRE'].mean()
    return uni
def QASommaire():
    with open("sommaire.txt", "w", encoding="utf-8") as f:
            Q1=', '.join(QA1())
            f.write(f"#1 - Quelles sont les variables présentes dans le jeu de données?\n")
            f.write(f"Réponse: {Q1}\n")
            Q2=''.join(QA2())
            f.write(f"#2 - Le nom de la topographie où se trouve l'arbre avec le tronc le plus grand?\n")
            f.write(f"Réponse: {Q2}\n")
            f.write(f"#3 - Combien dénombre-t-on d'espèces différentes chez les feuillus et les conifères?\n")
            f.write(f"Réponse: {QA3()[0]} Feuillus et {QA3()[1]} Conifère\n")
            Q4=', '.join(QA4())
            f.write(f"#4 - Quelles sont les espèces d'arbres (en français) que l'on retrouve dans le Parc Aimée-Miville?Alphabétiquement?\n")
            f.write(f"Réponse: {Q4} \n")
            Q5=''.join(QA5())
            f.write(f"#5 - De quelle espèce est l'arbre avec le tronc le plus gros? (en français)\n")
            f.write(f"Réponse: {Q5}\n")

            f.write(f"#6 - Quel est le diamètre moyen du tronc des feuillus dans à l'Université Laval? Des conifères?\n")

            f.write(f"Réponse: Le diamètre moyen du tronc des feuillus à l'Université Laval? est de {QA6()['diametre_feuillus']} et celui des conifères est de {QA6()['diametre_coniferes']}\n ")
def Fig1():
    df=pd.read_csv("vdq-arbrerepertorie.csv")
    df.dropna(subset=["TYPE_ARBRE","LATITUDE","LONGITUDE"])
    feuillu=df[df['TYPE_ARBRE']=='Feuillu']
    conifère=df[df['TYPE_ARBRE']=='Conifère']
    plt.scatter(x=feuillu["LONGITUDE"],y=feuillu["LATITUDE"],s=0.01)
    plt.scatter(x=conifère["LONGITUDE"], y=conifère["LATITUDE"],s=0.01)
    plt.title("Localisation et type des arbres répertoriés à la Ville de Québec")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.legend(title="Type d'arbre",labels=['feuillu','conifère'],markerscale=50)
    plt.savefig("figure1.png")
def Fig2():
    df=pd.read_csv("vdq-arbrerepertorie.csv")
    df = df.dropna(subset=["NOM_FRANCAIS", "NOM_TOPOGRAPHIE"])
    parc=df[df['NOM_TOPOGRAPHIE'].str.contains('Parc Jean-Marc-Gauthier')]
    nombre=parc.groupby("NOM_FRANCAIS")["NOM_FRANCAIS"].count()
    nombre.plot(kind="bar")
    plt.xticks(rotation=45,ha="right")
    plt.ylabel("Nombre d'arbres répertoriés")
    plt.grid(axis="y",linestyle="--")
    plt.title("Nombre d'arbres répértoriés à \n Parc Jean-Marc-Gauthier")
    plt.savefig("figure2.png")
def Fig3():
    df=pd.read_csv("vdq-arbrerepertorie.csv")
    df=df.dropna(subset=["NOM_FRANCAIS", "NOM_TOPOGRAPHIE","LONGITUDE","LATITUDE"])
    parc=df[df['NOM_TOPOGRAPHIE'].str.contains('Parc Jean-Marc-Gauthier')]
    especes=parc["NOM_FRANCAIS"]
    print(parc.groupby("NOM_FRANCAIS"))

Fig3()