<?php
namespace Oda;
class OdaRetourInterface {
    /**
     *
     * @var string 
     */
    public $strErreur = "";
    /**
     *
     * @var string 
     */
    public $data = "";
    /**
     *
     * @var int 
     */
    public $statut = OdaLibInterface::STATE_INIT;
    /**
     *
     * @var int 
     */
    public $id_transaction = 0;
    /**
     *
     * @var array 
     */
    public $metro = [];
}