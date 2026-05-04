#importation des packages utillisé.
import matplotlib.pyplot as plt
import pandas as pd

def QA1():
    """
        Retourne les variables présentes dans le dataframe "vdq-arbrerepertorie.csv" en liste.

        variables :
        df(dataframe) : Lecture du dataframe "vdq-arbrerepertorie.csv"

        Retourne :
        List : Les variables dans le dataframe principal

        Exemple d'utilisation :
        QA1()
    """
    df=pd.read_csv("vdq-arbrerepertorie.csv")
    return df.columns.to_list()
def QA2():
    """
        Retourne  Le nom de la topographie où se trouve l'arbre avec le tronc le plus gros.

        variables :
        df(dataframe) :Lecture du dataframe "vdq-arbrerepertorie.csv".
        grostronc(dataframe) :dataframe triée en ordre décroisant selon le diamètre.

        Retourne :
        str : le nom topographique de l'arbre avec le tronc le plus gros.

        Exemple d'utilisation :
        QA2()
    """
    df=pd.read_csv("vdq-arbrerepertorie.csv")
    grostronc=df.sort_values(by='DIAMETRE',ascending=False)
    return grostronc.iloc[0]['NOM_TOPOGRAPHIE']
def QA3():
    """
        Retourne le dénombrement d'espèces différentes chez les feuillus et les conifères

        variables :
        df(dataframe) :Lecture du dataframe "vdq-arbrerepertorie.csv".
        feuillu(dataframe) :filtrage des feuillus selon le nombre d'espèce différentes de feuillu
        feuillu(dataframe) :filtrage des conifère selon le nombre d'espèce différentes de conifère

        Retourne :
        feuillu,conifère(tuple) : le nombre d'espèce différentes de feuillu et de conifère

        Exemple d'utilisation :
        QA3()
    """
    df=pd.read_csv("vdq-arbrerepertorie.csv")
    feuillu=df[df['TYPE_ARBRE']=='Feuillu']['NOM_LATIN'].nunique()
    conifère=df[df['TYPE_ARBRE']=='Conifère']['NOM_LATIN'].nunique()
    return feuillu,conifère
def QA4():
    """
         Retourne les espèces d'arbres en français que l'on retrouve dans le Parc Aimée-Miville trié alphabétiquement.

         variables :
         df(dataframe) :Lecture du dataframe "vdq-arbrerepertorie.csv", lavé si il manque des valeurs dans le nom topographique ou le nom francais.
         parc(dataframe) :filtrage de df si le noms topographique contiennent les strings (Parc Aimée-Miville).
         especes(dataframe) :le nom francais des arbres sans dupe en ordre alphabétique.

         Retourne :
         especes(list): liste des nom francais des arbres dans le parc Aimée-Miville.

         Exemple d'utilisation :
         QA4()
     """
    df=pd.read_csv("vdq-arbrerepertorie.csv")
    df=df.dropna(subset=["NOM_TOPOGRAPHIE", "NOM_FRANCAIS"])
    parc=df[df['NOM_TOPOGRAPHIE'].str.contains('Parc Aimée-Miville')]
    especes=parc["NOM_FRANCAIS"].drop_duplicates().sort_values()
    return especes.to_list()
def QA5():
    """
        Retourne le nom francais de l'arbre avec le tronc le plus gros.

        variables :
        df(dataframe) :Lecture du dataframe "vdq-arbrerepertorie.csv".
        grostronc(dataframe) :dataframe triée en ordre décroisant selon le diamètre.

        Retourne :
        str : le nom francais de l'arbre avec le tronc le plus gros.

        Exemple d'utilisation :
        QA5()
    """
    df=pd.read_csv("vdq-arbrerepertorie.csv")
    grostronc=df.sort_values(by='DIAMETRE', ascending=False)
    return grostronc.iloc[0]['NOM_FRANCAIS']
def QA6():
    """
         Retourne le diamètre moyen du tronc des feuillus et des conifères dans à l'Université Laval

         variables :
         df(dataframe) :Lecture du dataframe "vdq-arbrerepertorie.csv", lavé si il manque des valeurs dans le nom topographique,le type d'arbre ou le diamètre.
         unifeuillu(dataframe) :filtrage de df si le noms topographique contiennent les strings (Université de Laval) ET que le type d'arbre soit un feuillu.
         uniconifère(dataframe) :filtrage de df si le noms topographique contiennent les strings (Université de Laval) ET que le type d'arbre soit un conifère.
         uni(dic) :dictionnaie contenant la valeur moyenne des diamètres pour les conifères et les feuillus.

         Retourne :
         Uni(dictionnaire): Dictionnaire des diamètres moyenne des feuillus et des conifères dans l'université de Laval.

         Exemple d'utilisation :
         QA6()
     """
    df=pd.read_csv("vdq-arbrerepertorie.csv")
    df=df.dropna(subset=["NOM_TOPOGRAPHIE","TYPE_ARBRE","DIAMETRE"])
    unifeuillu=df[(df["NOM_TOPOGRAPHIE"]=="Université Laval")&(df["TYPE_ARBRE"]=="Feuillu")]
    uniconfiere=df[(df["NOM_TOPOGRAPHIE"]=="Université Laval")&(df["TYPE_ARBRE"]=="Conifère")]
    uni={}
    uni['diametre_feuillus']=unifeuillu['DIAMETRE'].mean()#On ajoute diametre_feuillus comme key et le diamètre moyen des feuillus comme valeur.
    uni['diametre_coniferes']=uniconfiere['DIAMETRE'].mean()
    return uni
def QASommaire():
    """
         Ouvre un fichier texte pour enregistrer les réponses du questionnaire.

         Exemple d'utilisation :
         QASommaire()
     """
    with open("sommaire.txt", "w", encoding="utf-8") as f:
            Q1=', '.join(QA1()) #transforme la liste renvoyée par QA1() en une seule chaîne de caractères, où chaque élément est séparé par une virgule et un espace.

            f.write(f"#1 - Quelles sont les variables présentes dans le jeu de données?\n")
            f.write(f"Réponse: {Q1}\n")

            Q2=''.join(QA2())

            f.write(f"#2 - Le nom de la topographie où se trouve l'arbre avec le tronc le plus grand?\n")
            f.write(f"Réponse: {Q2}\n")

            f.write(f"#3 - Combien dénombre-t-on d'espèces différentes chez les feuillus et les conifères?\n")
            f.write(f"Réponse: {QA3()[0]} Feuillus et {QA3()[1]} Conifère\n") # QA3()[1] renvoi la valeur du tuple de la question 3 selon l'index 0 et 1

            Q4=', '.join(QA4())

            f.write(f"#4 - Quelles sont les espèces d'arbres (en français) que l'on retrouve dans le Parc Aimée-Miville?Alphabétiquement?\n")
            f.write(f"Réponse: {Q4} \n")

            Q5=''.join(QA5())

            f.write(f"#5 - De quelle espèce est l'arbre avec le tronc le plus gros? (en français)\n")
            f.write(f"Réponse: {Q5}\n")

            f.write(f"#6 - Quel est le diamètre moyen du tronc des feuillus dans à l'Université Laval? Des conifères?\n")
            f.write(f"Réponse: Le diamètre moyen du tronc des feuillus à l'Université Laval? est de {QA6()['diametre_feuillus']} et celui des conifères est de {QA6()['diametre_coniferes']}\n ") #QA6()['diametre_feuillus'] renvoi la valeur selon la clé utillsé pour le dictionnaire
def Fig1():
    """
         Sauvegarde une image PNG de la figure produite de la localisation et type des arbres répertoriés à la Ville de Québec.

         variables :
         df(dataframe) :Lecture du dataframe "vdq-arbrerepertorie.csv", suprime les rows dans les collone avec des valeur manquante de latitude,le type d'arbre ou la longitude.
         feuillu(dataframe) :filtrage de df si le type d'arbre soit un feuillu.
         conifère(dataframe) :filtrage de df si le type d'arbre soit un conifère.


         Exemple d'utilisation :
         Fig1()
     """
    df=pd.read_csv("vdq-arbrerepertorie.csv")
    df.dropna(subset=["TYPE_ARBRE","LATITUDE","LONGITUDE"])
    feuillu=df[df['TYPE_ARBRE']=='Feuillu']
    conifère=df[df['TYPE_ARBRE']=='Conifère']
    plt.figure()
    plt.scatter(x=feuillu["LONGITUDE"],y=feuillu["LATITUDE"],s=0.01)
    plt.scatter(x=conifère["LONGITUDE"],y=conifère["LATITUDE"],s=0.01)
    plt.title("Localisation et type des arbres répertoriés à la Ville de Québec")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.legend(title="Type d'arbre",labels=['feuillu','conifère'],markerscale=50)
    plt.savefig("figure1.png")
def Fig2():
    """
         Sauvegarde une image PNG de la figure produite du nombre d'arbres répértoriés aux Parc Jean-Marc-Gauthier.

         variables :
         df(dataframe) :Lecture du dataframe "vdq-arbrerepertorie.csv", suprime les rows dans les collone avec des valeur manquante de nom topographique ou de nom francais.
         parc(dataframe) :filtrage de df avec le nom topographique contenant les strings de Parc Jean-Marc-Gauthier.
         nombre(série) : regroupe les nom francais et compte le nombre de nom francais.


         Exemple d'utilisation :
         Fig2()
     """
    df=pd.read_csv("vdq-arbrerepertorie.csv")
    df = df.dropna(subset=["NOM_FRANCAIS", "NOM_TOPOGRAPHIE"])
    parc=df[df['NOM_TOPOGRAPHIE'].str.contains('Parc Jean-Marc-Gauthier')]
    nombre=parc.groupby("NOM_FRANCAIS")["NOM_FRANCAIS"].count()
    plt.figure()
    nombre.plot(kind="bar")
    plt.xticks(rotation=45,ha="right")
    plt.ylabel("Nombre d'arbres répertoriés")
    plt.grid(axis="y",linestyle="--")
    plt.title("Nombre d'arbres répértoriés à \n Parc Jean-Marc-Gauthier")
    plt.savefig("figure2.png")
def Fig3():
    """
         Sauvegarde une image PNG de la figure produite de la localisation des espèces d'arbres dans le Parc Jean-Marc-Gauthier.

         variables :
         df(dataframe) :Lecture du dataframe "vdq-arbrerepertorie.csv", suprime les rows dans les collone avec des valeur manquante de la latitude,le type d'arbre, la longitude et le nom francais.
         parc(dataframe) :filtrage de df avec le nom topographique contenant les strings de Parc Jean-Marc-Gauthier.

         Exemple d'utilisation :
         Fig3()
     """
    df=pd.read_csv("vdq-arbrerepertorie.csv")
    df=df.dropna(subset=["NOM_FRANCAIS", "NOM_TOPOGRAPHIE","LONGITUDE","LATITUDE"])
    parc=df[df['NOM_TOPOGRAPHIE'].str.contains('Parc Jean-Marc-Gauthier')]
    plt.figure()
    for index,row in parc.groupby("NOM_FRANCAIS"):
        plt.scatter(x=row['LONGITUDE'],y=row['LATITUDE'],s=15)
    plt.legend(title="Type d'arbre",labels=parc["NOM_FRANCAIS"].drop_duplicates(),markerscale=0.6,loc="lower left",fontsize=6)
    plt.grid(linestyle="--")
    plt.title("Localisation des espèces d'arbres dans le \n Parc Jean-Marc-Gauthier")
    plt.savefig("figure3.png")
def Fig4():
    """
         Sauvegarde une image PNG de la figure produite de la localisation des espèces d'arbres dans le Parc Jean-Marc-Gauthier.

         variables :
         df(dataframe) :Lecture du dataframe "vdq-arbrerepertorie.csv", suprime les rows dans les collone avec des valeur manquante du nom topographique, du nom francais et du diamètre.
         chene(dataframe) :filtrage de df avec le nom topographique contenant les strings de Parc et le nom francais chêne rouge.
         top10(série) :reprouge les noms topogrpahique et compte le diamètre en ordre décroissant des noms topographique. On transforme ensuite la série en liste.
         parc(dataframe) :filtrage de df selon le nom topographique dans la liste de top10
         Exemple d'utilisation :
         Fig4()
     """
    df=pd.read_csv("vdq-arbrerepertorie.csv")
    df=df.dropna(subset=["NOM_TOPOGRAPHIE","NOM_FRANCAIS","DIAMETRE"])
    chene=df[(df['NOM_TOPOGRAPHIE'].str.contains('Parc')) & (df["NOM_FRANCAIS"]=="chêne rouge")]
    top10=(chene.groupby("NOM_TOPOGRAPHIE")["DIAMETRE"].count().sort_values(ascending=False).head(10))
    top10=top10.index.tolist()
    parc=chene[chene["NOM_TOPOGRAPHIE"].isin(top10)]
    plt.figure()
    parc.boxplot(by="NOM_TOPOGRAPHIE",column="DIAMETRE")
    plt.xticks(rotation=45,ha="right")
    plt.title("Taille des diamètres de l'espèce ""chêne rouge""\n dans les 10 parcs en possédant le plus")
    plt.suptitle("")
    plt.grid(linestyle="--")
    plt.savefig("figure4.png")
