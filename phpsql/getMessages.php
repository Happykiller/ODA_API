<?php
namespace Oda;
//--------------------------------------------------------------------------
//Header
require("../php/header.php");

//--------------------------------------------------------------------------
//Build the interface
$params = new OdaPrepareInterface();
$params->interface = "API/phpsql/getMessages";
$params->arrayInput = array();
$ODA_INTERFACE = new OdaLibInterface($params);

//--------------------------------------------------------------------------
// API/phpsql/getMessages.php?milis=123450&ctrl=ok
    
//--------------------------------------------------------------------------
$params = new OdaPrepareReqSql();
$params->sql = "Select * 
    FROM `api_tab_messages` a
    WHERE 1=1
    ORDER BY a.`id` desc
    LIMIT 0, 10
;";
$params->typeSQL = OdaLibBd::SQL_GET_ALL;
$retour = $ODA_INTERFACE->BD_ENGINE->reqODASQL($params);

//---------------------------------------------------------------------------
$params = new \stdClass();
$params->label = "messages";
$params->retourSql = $retour;
$ODA_INTERFACE->addDataReqSQL($params);