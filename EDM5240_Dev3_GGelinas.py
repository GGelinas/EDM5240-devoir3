
# coding: utf-8

# ## Interroger une base de données (accès à l'information)

# <font color="#F5B041" > <I>Importation des modules pandas et matplotlib.</font></I><br>

# In[2]:


import pandas as pan


# In[209]:


get_ipython().magic('matplotlib inline')
import matplotlib as mp
import matplotlib.pyplot as plt


# <font color="#F5B041" > <I>Afficher les nombres sans notation scientifiques.</font></I><br>

# In[3]:


pan.set_option("display.float_format", lambda x : "%.2f" % x)


# <font color="#F5B041" > <I>Lecture du fichier csv avec le module panda.</font></I><br>

# In[4]:


acces = pan.read_csv("ati.csv", low_memory=False)


# <font color="#F5B041" > <I>Affichage de notre fichier csv dans un tableau.</font></I><br>

# In[5]:


acces


# <font color="#F5B041" > <I>Afficher le nombre de rangées et de colonnes que contient notre tableau. </font></I><br>

# In[6]:


acces.shape


# <font color="#F5B041" > <I>Francisation des titres des colonnes du tableau.</font></I><br>

# In[7]:


acces.columns


# In[8]:


acces.columns = ['annee', 'mois', 'numerodelarequete', 'resume_ang', 'resume_fr',
       'disposition', 'pages', 'acronyme_org', 'titrecompletDelorganistion']


# In[9]:


acces.columns


# In[10]:


acces


# <font color="#F5B041" > <I> Afficher les types de variables qui constituent notre tableau.</font></I><br>

# In[12]:


acces.dtypes


# <font color="#F5B041" > <I> Affichage du nombre de demandes par année.</font></I><br>

# In[222]:


acces.annee.value_counts()


# <font color="#F5B041" > <I> Affichage des différentes organisations qui ont reçu des demandes d'accès à l'information.</font></I><br>

# In[19]:


acces.titrecompletDelorganistion.value_counts()


# <b> Question 1:</b> <font color="navy" > <I> Combien de demandes d'accès à l'information ont été faites pour le ministère de la Défense nationale et combien de ces demandes n'avaient aucun document à fournir et combien avaient une communication totale?</I>

# <font color="#F5B041" > <I> Recherche des demandes concernant la Défense nationale sur l'ensemble total des demandes du fichier.</font></I><br>

# In[18]:


Defense = acces.titrecompletDelorganistion == "National Defence | Défense nationale"
acces[Defense]


# <font color="#F5B041" > <I> Affichage des différentes dispositions qui ont été prises concernant les demandes de la Défense nationale.</font></I><br>

# In[19]:


acces[Defense].disposition.value_counts()


# <font color="#F5B041" > <I> Aperçu des résumés en français des demandes concernant la Défense nationale. </font></I><br>

# In[20]:


acces[Defense].resume_fr.value_counts()


# <font color="#F5B041" > <I> Compte total des demandes qui concernent la Défense nationale.</font></I><br>

# In[21]:


test1 = acces.titrecompletDelorganistion.str.contains("National Defence | Défense nationale")
test1
len(acces[test1])


# <font color="#F5B041" > <I> Recherche des demandes, concernant la Défense nationale, qui ont les mentions "aucun document existe".</font></I><br>

# In[22]:


aucun = acces[test1].disposition == "Does not exist / Aucun document existe"
aucun2 = acces[test1].disposition == "Does not exist / Aucun Document Existe"
aucun3 = acces[test1].disposition == "Does not exist Aucun document existe"
aucun4 = acces[test1].disposition == "Does not exist/Aucun document existe"
acces[test1][aucun + aucun2 + aucun3 + aucun4]


# <font color="#F5B041" > <I> Compte total du nombre de demandes qui ont reçu aucun document.</font></I><br>

# In[23]:


len(acces[test1][aucun + aucun2 + aucun3 + aucun4])


# <font color="#F5B041" > <I> Recherche des demandes, concernant la Défense nationale, qui ont les mentions "Communication totale" et "Communication Totale".</font></I><br>

# In[24]:


totale = acces[test1].disposition == "All disclosed / Communication totale"
totale1 = acces[test1].disposition == "All disclosed / Communication Totale"
acces[test1][totale + totale1]


# <font color="#F5B041" > <I> Compte total du nombre de demandes qui ont eu une "communication totale".</font></I><br>

# In[25]:


len(acces[test1][totale + totale1])


# <b> Réponse 1:</b> <font color="navy" > <I> La Défense nationale a fourni aucun document à 335 demandes, mais a fourni une communication totale à 285 demandes.</I>

#  <b> Question 2:</b> <font color="maroon" > <I> Combien de demandes d'accès à l'information ont été faites concernant Mégantic dans les dernières années?</I> 

# <font color="#F5B041" > <I> Recherche, dans les résumés en anglais et en français, des demandes faites avec les mentions de "Megantic"/"megantic" et "Mégantic"/"mégantic".</font></I><br>

# In[49]:


megantic = acces.resume_ang.str.contains("Megantic")==True
megantic1 = acces.resume_ang.str.contains("megantic")==True
megantic2 = acces.resume_fr.str.contains("Mégantic")==True
megantic3 = acces.resume_fr.str.contains("mégantic")==True
acces[(megantic|megantic1|megantic2| megantic3)]


# <font color="#F5B041" > <I> Compte total du nombre de demandes faites avec les mentions de "Megantic"/"megantic" et "Mégantic"/"mégantic".</font></I><br>

# In[50]:


len(acces[(megantic|megantic1|megantic2| megantic3)])


# <font color="#F5B041" > <I> Faire le compte par organisation du nombre de demandes qu'elles ont obtenues.</font></I><br>

# In[51]:


acces[(megantic|megantic1|megantic2| megantic3)].titrecompletDelorganistion.value_counts()


# <font color="#F5B041" > <I> Isoler les résumés en français des douze demandes. </font></I><br>

# In[53]:


acces[(megantic|megantic1|megantic2|megantic3)].resume_fr.value_counts()


# <b> Réponse 2:</b> <font color="maroon" > <I> Douze demandes d'acces à l'information ont concerné Mégantic en 2016-2017. Ces demandes ont été adressées à quatre organisations gouvernementales.</font></I><br>
# <br>
# 7 demandes pour<br>
# Transport Canada | Transports Canada<br>
# <br>
# 2 demandes pour<br>
# Public Safety Canada | Sécurité publique Canada<br>
# <br>
# 2 demandes pour<br>
# Transportation Safety Board of Canada | Bureau de la sécurité des transports du Canada<br>
# <br>
# 1 demande pour<br>
# Environment and Climate Change Canada | Environnement et Changement climatique Canada<br>
# 
# <font color="maroon" > <I>Voici les 12 résumés de ces demandes:</font></I><br>
# <br>
# 1) Documents préparés par Georges Long, ECCC, et concernant le déraillement à Lac-Mégantic.<br> 
# 2) Note d’information : Réévaluation par le Bureau de la sécurité des transports des recommandations formulées à la suite du déraillement à Lac-Mégantic.<br> 
# 3) Toutes les notes d'information à l'intention du ministre sur une voie de contournement ferroviaire à Lac-Mégantic, du 1er octobre 2015 au 22 mars 2016.<br> 
# 4) R13D0054- analyse de la géométrie des rails de MMA pour les endroits entre l'aiguille de voie d'évitement de l'ouest à la station de train Nantes et l'aiguillage de triage de l'est à Lac Mégantic tel que réalisé suite au déraillement en juillet 2013.<br> 
# 5) Dossiers sur la contribution du gouvernement fédéral au fonds d’indemnisation pour les victimes et les survivants du désastre ferroviaire de Lac-Mégantic entre le 1er septembre 2015 et le 18 avril 2016. Exclure les documents possiblement confidentiels du Cabinet.<br> 
# 6) R13D0054 - documents relatifs à l'enregistreur d'événement de la locomotive MMA's 5017, données téléchargés le 6 juillet 2013 à l'est du lac megantic, dépôt de rails (rail yard) après que les locomotives impliquées dans l'incident se sont immobilisées.<br> 
# 7) Demandes de paiement soumises concernant l’accident ferroviaire dans la ville de Lac-Mégantic<br> 
# 8) Notes d'information : Options de mise en œuvre d'une voie de contournement ferroviaire à Lac-Mégantic; enregistreurs audio-vidéo dans les cabines de locomotives; accélérer le calendrier de modernisation des anciens wagons-citernes DOT-111.<br> 
# 9) Information qui fait référence à l'entente d'assistance financière découlant du sinistre survenu dans la ville de Lac-Mégantic.<br> 
# 10) Note d'information : Évaluation indépendante des voies ferrées à Lac­Mégantic, commandée par la Central Maine et Québec Railway.<br> 
# 11) Intervention du ministre à la suite du déraillement de train survenu le 6 juillet 2013, à Lac-Mégantic.<br> 
# 12) Rapports d'inspection de la voie ferrée à Lac-Mégantic, du 1er juillet 2013 au 3 septembre 2015.<br> 
# 

# <b> Question 3:</b> <font color="darkgreen" > <I> Combien de demandes d'accès à l'information ont eu pour sujet "allégations sexuelles" et "inconduites sexuelles" et à quelles organisations s'adressaient-elles?</font></I><br>

# <font color="#F5B041" > <I> Recherche des mots "agressions sexuelles" dans les résumés en français de toutes les demandes.</font></I><br>

# In[39]:


asexual1= acces.resume_fr.str.contains("agressions sexuelles", na=False)
acces[asexual1]


# <font color="#F5B041" > <I> Recherche des mots "agression sexuelle" dans les résumés en français de toutes les demandes.</font></I><br>

# In[101]:


asexual2= acces.resume_fr.str.contains("agression sexuelle", na=False)
acces[asexual2]


# <font color="#F5B041" > <I> Recherche des mots "inconduites sexuelles" dans les résumés en français de toutes les demandes.</font></I><br>

# In[102]:


asexual3= acces.resume_fr.str.contains("inconduites sexuelles", na=False)
acces[asexual3]


# <font color="#F5B041" > <I> Recherche des mots "inconduite sexuelle" dans les résumés en français de toutes les demandes.</font></I><br>

# In[103]:


asexual4= acces.resume_fr.str.contains("inconduite sexuelle", na=False)
acces[asexual4]


# <font color="#F5B041" > <I> Compte des demandes qui ont la mention "agressions sexuelles"/"agression sexuelle" et "inconduites sexuelles"/"inconduite sexuelle".</font></I><br>

# In[109]:


len(acces[(asexual1|asexual2|asexual3|asexual4)])


# <font color="#F5B041" > <I> Formation d'un tableau avec la fonction .describe() pour mieux visualiser les données à partir des noms des organisations.</font></I><br>

# In[110]:


acces[(asexual1|asexual2|asexual3|asexual4)].groupby("titrecompletDelorganistion").resume_fr.describe()


# <font color="#F5B041" > <I> Tentative de création d'un graphique à partir des données obtenues à la question 3 avec la fonction .plot(kind='line').</font></I><br>

# In[221]:


acces[(asexual1|asexual2|asexual3|asexual4)].groupby("titrecompletDelorganistion").resume_fr.describe().plot(kind='line')


# <font color="#F5B041" > <I> Tentative de création d'un graphique à partir des données obtenues à la question 3.</font></I><br>

# In[219]:


graphique = pan.DataFrame(columns=['dataFor','total'])
graphique['dataFor'] = [("Agence des services frontaliers du Canada"),("Agence du revenu du Canada"),("Patrimoine canadien"),("Ministère de la Justice"),("Affaires autochtones et du Nord Canada"),("Innovation, Sciences et Développement économique Canada"),("Défense nationale"),(" Commission des libérations conditionnelles du Canada"),("Sécurité publique Canada"),("Gendarmerie royale du Canada"),("Statistique Canada"),("Condition féminine Canada")]
graphique['total'] = [2,1,1,5,2,1,16,1,1,30,6,1]

plt.figure(figsize=(20,10))
#plt.plot(graphique.dataFor, graphique.total, linewidth=5)
plt.plot(graphique.dataFor,graphique.total, '*', linewidth=5, markersize=20, color='red')
plt.xticks(fontsize=10, fontweight='bold',rotation=90)
plt.yticks(fontsize=20, fontweight='bold')
plt.xlabel("Nom de l'organisation", fontsize=15, fontweight='bold')
plt.ylabel('Nb de demandes',fontsize=15, fontweight='bold')
plt.title('Nombre de demandes avec mention "agressions sexuelles" et "inconduites sexuelles" par organisation',fontsize=20, fontweight='bold')
#plt.tight_layout()

graphique


# <b> Réponse 3:</b> <font color="darkgreen" > <I> 67 demandes d'accès à l'information ont eu pour sujet "allégations sexuelles" et "inconduites sexuelles" et elles s'adressaient à douze organisations différentes.<br> La Gendarmerie royale du Canada et la Défense nationale ont reçues le plus grand nombre de demandes, soit 30 pour la Gendarmerie et 16 pour la Défense.</font></I><br>
