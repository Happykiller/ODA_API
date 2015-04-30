# ODA_API

# Full project
WEB client (Html, Jquery, Jquery Mobile) + REST API (Php)

Install
1- Get all the sources in ./yourProject/API/
2- Create json conf (ex : in API/install/Scripts/exemple.config.api.oda.json)
3- Run cmd (ex : python API/install/Scripts/script_ODA_API.py ../../../../exemple.config.api.oda.json install)
4- Config (include/config.js and include/config.php)

Update
Run cmd (ex : python API/install/Scripts/script_ODA_API.py ../../../../exemple.config.api.oda.json update)

# Composer 
(For use the php class, WEB REST feature)
https://packagist.org/packages/happykiller/oda_api

Ex : file.php
<pre>
/**
 * CONFIG PART
 */
$config = \Oda\SimpleObject\OdaConfig::getInstance();
$config->domaine = "http://localhost/project/";

//for bd engine
$config->BD_ENGINE->base = 'base';
$config->BD_ENGINE->mdp = 'pass';

/**
 * BUILD INTERFACE
 */
$params = new \Oda\SimpleObject\OdaPrepareInterface();
$params->arrayInput = array("param_name");
$ODA_INTERFACE = new \Oda\OdaLibInterface($params);

/**
 * USE BD
 */
//Build query
$params = new \Oda\SimpleObject\OdaPrepareReqSql();
$params->sql = "SELECT *
    FROM `api_tab_parametres` a
    WHERE 1=1
    AND a.`param_name` = :param_name
;";
$params->bindsValue = [
    "param_name" => $ODA_INTERFACE->inputs["param_name"]
];
$params->typeSQL = \Oda\OdaLibBd::SQL_GET_ONE;
$retour = $ODA_INTERFACE->BD_ENGINE->reqODASQL($params);

//Add result to interface
$params = new \stdClass();
$params->label = "resultat_get_one";
$params->retourSql = $retour;
$ODA_INTERFACE->addDataReqSQL($params);
</pre>


