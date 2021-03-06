import sys
import os
import glob
import shutil
import errno
import MyLogger
import codecs
import json

#Procedure de copy
def copytree(src, dst, remplace, p_inventaire, p_param):
    try:
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                MyLogger.logger.debug("Directory:"+s)
                if not (os.path.isdir(d)):
                    os.mkdir(d)
                    MyLogger.logger.debug("Dossier créé.")
                    copytree(s, d, remplace, p_inventaire, p_param)
                else:
                    MyLogger.logger.debug("Dossier déjà présent.")
                    copytree(s, d, remplace, p_inventaire, p_param)
            else:
                MyLogger.logger.debug("Fichier:"+s)
                if os.path.isfile(d):
                    if remplace:
                        if not isIn(s, p_inventaire, p_param):
                            os.remove(d)
                            shutil.copy2(s, d)
                            MyLogger.logger.debug("Remplacement réussi.")
                        else:
                            MyLogger.logger.debug("Ignore réussi.")
                    else:
                        MyLogger.logger.debug("Fichier déjà présent.")
                else :
                  shutil.copy2(s, d)
                  MyLogger.logger.debug("Copie réussi.")
    except OSError as exc:
        MyLogger.logger.error("Erreur pendant la copie. (Fichier/Dossier peu-être déjà existant ?):"+format(exc))
        sys.exit("Erreur")

#Edit file
def editFile(file, mapping):
    fichier = open(file,'r')
    fichier2 = open(file+'~','w')  
    lignes = fichier.readlines()                
    for ligne in lignes:
        ligneFinale = ligne
        for correspondance in mapping:
            ligneFinale = ligneFinale.replace(correspondance["key"],correspondance["value"])            
        fichier2.write(ligneFinale)  
    fichier.close()                     
    fichier2.close()                    
    os.remove(file)
    os.rename(file+'~',file)

def isIn(p_file, p_inventaire, p_param):
    try:
        bolRetour = False;

        if ((p_inventaire == "") and (p_path == "")):
            return bolRetour

        for cur_fichier in p_inventaire:
            if(p_file.replace("\\","/") == (p_param["cheminWWW"]+p_param["cheminAPI"]+"deploy/"+cur_fichier["chemin"] + cur_fichier["nom"])):
                bolRetour = True
                break

        return bolRetour         
    except Exception as e:
        MyLogger.logger.error("Erreur pendant isIn : ("+format(e)+")")
        sys.exit("Erreur")

#Procedure chargement du fichier config JSON
def charger_config(p_fileJson) :
    try:
        MyLogger.logger.debug("Début chargement configuration")
        v_config=codecs.open(p_fileJson, 'r','utf-8')
        v_config_json = json.load(v_config)
        MyLogger.logger.debug("Chargement configuration réussi")
        return v_config_json
    except ValueError as exc:
        MyLogger.logger.error("Erreur pendant le chargement du fichier de configuration : " + arguments["param"])
        sys.exit("Erreur")
